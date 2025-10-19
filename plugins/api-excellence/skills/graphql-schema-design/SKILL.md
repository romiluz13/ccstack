---
name: graphql-schema-design
description: GraphQL schema design patterns including types, queries, mutations, and resolvers. Use when working with GraphQL APIs, designing schemas, or implementing resolvers.
---

# GraphQL Schema Design

Best practices for designing scalable, maintainable GraphQL schemas.

## When to Use

- GraphQL API design
- Schema planning
- Resolver implementation
- Performance optimization

## Core Concepts

### 1. Type Design
```graphql
type User {
  id: ID!
  email: String!
  name: String
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
}
```

### 2. Queries
```graphql
type Query {
  user(id: ID!): User
  users(limit: Int, offset: Int): [User!]!
  post(id: ID!): Post
}
```

### 3. Mutations
```graphql
type Mutation {
  createUser(input: CreateUserInput!): User!
  updateUser(id: ID!, input: UpdateUserInput!): User!
  deleteUser(id: ID!): Boolean!
}
```

### 4. Input Types
```graphql
input CreateUserInput {
  email: String!
  name: String!
  password: String!
}
```

## Best Practices

- Use non-null (!) appropriately
- Pagination with connections
- Input types for mutations
- Avoid N+1 with DataLoader
- Field-level permissions
- Descriptive field names

---

**Auto-loads with GraphQL tasks.**

