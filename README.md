# Create Data

```gql
mutation {
    createData(data: { name: "Example Name", value: "Example Value" }) {
        id
        name
        value
    }
}
```

# Read Data by ID

```gql
query {
    getData(data: { id: "abc9f49c-d564-4b32-86f8-045ac5fbbb08" }) {
        id
        name
        value
    }
}
```

# Read All Data

```gql
query {
    getAllData {
        id
        name
        value
    }
}
```

# Update Data

```gql
mutation {
    updateData(
        data: {
            id: "abc9f49c-d564-4b32-86f8-045ac5fbbb08"
            name: "Updated Name"
            value: "Updated Value"
        }
    )
}
```

# Delete Data

```gql
mutation {
    deleteData(data: { id: "abc9f49c-d564-4b32-86f8-045ac5fbbb08" })
}
```
