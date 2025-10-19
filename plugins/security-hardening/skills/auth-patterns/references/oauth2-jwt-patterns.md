# OAuth2 & JWT Authentication Patterns

## OAuth2 Flow Patterns

### 1. Authorization Code Flow (Most Secure)

**When to use:**
- Web applications with backend
- Mobile apps with secure storage
- Server-to-server communication

**Implementation:**
```typescript
// Step 1: Redirect to authorization server
app.get('/auth/login', (req, res) => {
  const authUrl = `${AUTH_SERVER}/authorize?` +
    `client_id=${CLIENT_ID}&` +
    `redirect_uri=${REDIRECT_URI}&` +
    `response_type=code&` +
    `scope=openid profile email&` +
    `state=${generateState()}`;
  
  res.redirect(authUrl);
});

// Step 2: Handle callback with authorization code
app.get('/auth/callback', async (req, res) => {
  const { code, state } = req.query;
  
  // Verify state to prevent CSRF
  if (!verifyState(state)) {
    return res.status(400).send('Invalid state');
  }
  
  // Exchange code for tokens
  const tokens = await exchangeCodeForTokens(code);
  
  // Store tokens securely (httpOnly cookies or secure session)
  res.cookie('access_token', tokens.access_token, {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    maxAge: tokens.expires_in * 1000
  });
  
  res.redirect('/dashboard');
});
```

### 2. JWT Token Structure

**Anatomy of a JWT:**
```
header.payload.signature

Example:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Header:**
```json
{
  "alg": "RS256",  // Use RS256 (asymmetric) not HS256 for production
  "typ": "JWT"
}
```

**Payload (Claims):**
```json
{
  "sub": "user_id_123",           // Subject (user ID)
  "iss": "https://auth.myapp.com", // Issuer
  "aud": "https://api.myapp.com",  // Audience
  "exp": 1735689600,               // Expiration (Unix timestamp)
  "iat": 1735686000,               // Issued at
  "nbf": 1735686000,               // Not before
  "jti": "unique_token_id",        // JWT ID
  "scope": "read:profile write:posts",
  "email": "user@example.com",
  "role": "admin"
}
```

### 3. Secure JWT Implementation

**Token Generation (Node.js):**
```typescript
import jwt from 'jsonwebtoken';
import fs from 'fs';

// Use RS256 with public/private key pair
const privateKey = fs.readFileSync('private.key');

function generateAccessToken(userId: string, scope: string[]): string {
  const payload = {
    sub: userId,
    iss: 'https://auth.myapp.com',
    aud: 'https://api.myapp.com',
    scope: scope.join(' '),
    exp: Math.floor(Date.now() / 1000) + (15 * 60), // 15 minutes
    iat: Math.floor(Date.now() / 1000)
  };
  
  return jwt.sign(payload, privateKey, { 
    algorithm: 'RS256',
    keyid: 'key-2024-01' // Key version for rotation
  });
}

function generateRefreshToken(userId: string): string {
  return jwt.sign(
    { 
      sub: userId,
      type: 'refresh',
      jti: generateUniqueId() // For revocation tracking
    },
    privateKey,
    { 
      algorithm: 'RS256',
      expiresIn: '7d' 
    }
  );
}
```

**Token Verification:**
```typescript
const publicKey = fs.readFileSync('public.key');

function verifyAccessToken(token: string): JWTPayload {
  try {
    const decoded = jwt.verify(token, publicKey, {
      algorithms: ['RS256'],
      issuer: 'https://auth.myapp.com',
      audience: 'https://api.myapp.com'
    });
    
    return decoded as JWTPayload;
  } catch (err) {
    if (err.name === 'TokenExpiredError') {
      throw new AuthError('Token expired', 401);
    }
    if (err.name === 'JsonWebTokenError') {
      throw new AuthError('Invalid token', 401);
    }
    throw err;
  }
}
```

### 4. Refresh Token Pattern

**Implementation:**
```typescript
app.post('/auth/refresh', async (req, res) => {
  const refreshToken = req.cookies.refresh_token;
  
  if (!refreshToken) {
    return res.status(401).json({ error: 'No refresh token' });
  }
  
  try {
    // Verify refresh token
    const decoded = jwt.verify(refreshToken, publicKey, {
      algorithms: ['RS256']
    });
    
    // Check if token is revoked (redis/database lookup)
    const isRevoked = await checkTokenRevocation(decoded.jti);
    if (isRevoked) {
      return res.status(401).json({ error: 'Token revoked' });
    }
    
    // Generate new access token
    const newAccessToken = generateAccessToken(
      decoded.sub,
      decoded.scope.split(' ')
    );
    
    res.cookie('access_token', newAccessToken, {
      httpOnly: true,
      secure: true,
      sameSite: 'strict',
      maxAge: 15 * 60 * 1000 // 15 minutes
    });
    
    res.json({ message: 'Token refreshed' });
  } catch (err) {
    res.status(401).json({ error: 'Invalid refresh token' });
  }
});
```

## Security Best Practices

### 1. Token Storage

**❌ NEVER:**
```javascript
// DON'T store in localStorage (XSS vulnerable)
localStorage.setItem('token', accessToken);

// DON'T store in regular cookies without flags
res.cookie('token', accessToken);
```

**✅ ALWAYS:**
```javascript
// DO use httpOnly, secure cookies
res.cookie('access_token', accessToken, {
  httpOnly: true,  // Prevents JavaScript access (XSS protection)
  secure: true,    // HTTPS only
  sameSite: 'strict', // CSRF protection
  maxAge: 900000   // 15 minutes
});

// OR use Authorization header with short-lived tokens
// Client stores in memory only (lost on page refresh)
```

### 2. Token Expiration Strategy

```typescript
const TOKEN_STRATEGY = {
  accessToken: {
    expiresIn: '15m',     // Short-lived
    storage: 'httpOnly cookie or memory'
  },
  refreshToken: {
    expiresIn: '7d',      // Long-lived
    storage: 'httpOnly cookie',
    rotation: true        // Rotate on each use
  }
};
```

### 3. Scope-Based Authorization

```typescript
function requireScope(requiredScope: string) {
  return (req, res, next) => {
    const token = extractToken(req);
    const decoded = verifyAccessToken(token);
    
    const userScopes = decoded.scope.split(' ');
    
    if (!userScopes.includes(requiredScope)) {
      return res.status(403).json({ 
        error: 'Insufficient permissions',
        required: requiredScope,
        has: userScopes
      });
    }
    
    req.user = decoded;
    next();
  };
}

// Usage
app.get('/api/admin/users', 
  requireScope('admin:read'),
  async (req, res) => {
    // Only users with admin:read scope can access
  }
);
```

### 4. Rate Limiting & Token Revocation

```typescript
// Rate limit token generation
import rateLimit from 'express-rate-limit';

const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts
  message: 'Too many authentication attempts'
});

app.post('/auth/login', authLimiter, async (req, res) => {
  // Login logic
});

// Token revocation (Redis example)
import redis from 'redis';
const redisClient = redis.createClient();

async function revokeToken(jti: string, expiresIn: number) {
  // Store revoked token JTI in Redis with expiration
  await redisClient.setex(`revoked:${jti}`, expiresIn, '1');
}

async function checkTokenRevocation(jti: string): Promise<boolean> {
  const result = await redisClient.get(`revoked:${jti}`);
  return result !== null;
}

// Logout endpoint
app.post('/auth/logout', async (req, res) => {
  const token = extractToken(req);
  const decoded = jwt.decode(token);
  
  // Revoke refresh token
  if (decoded.jti) {
    await revokeToken(decoded.jti, decoded.exp - Math.floor(Date.now() / 1000));
  }
  
  res.clearCookie('access_token');
  res.clearCookie('refresh_token');
  res.json({ message: 'Logged out' });
});
```

## Common Pitfalls

### ❌ Using HS256 with shared secrets in distributed systems
**Problem:** All services need the secret; compromise spreads everywhere.
**Solution:** Use RS256 with public/private keys.

### ❌ Storing sensitive data in JWT payload
**Problem:** JWT payload is base64 encoded, not encrypted.
**Solution:** Store only necessary claims. Keep sensitive data in database.

### ❌ No token expiration or very long expiration
**Problem:** Stolen tokens valid forever.
**Solution:** Use short-lived access tokens (15min) with refresh tokens.

### ❌ Not validating issuer and audience
**Problem:** Tokens from other services accepted.
**Solution:** Always validate `iss` and `aud` claims.

### ❌ Accepting algorithm from token header
**Problem:** "None" algorithm attack.
**Solution:** Explicitly specify allowed algorithms in verification.

## Testing Checklist

- [ ] Access token expires correctly (15 minutes)
- [ ] Refresh token rotation works
- [ ] Expired tokens are rejected
- [ ] Revoked tokens are rejected
- [ ] Invalid signatures are rejected
- [ ] Scope enforcement works correctly
- [ ] Rate limiting prevents brute force
- [ ] httpOnly cookies prevent XSS access
- [ ] CSRF protection (state parameter) works
- [ ] Tokens are not logged or exposed in errors

