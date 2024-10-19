import {
  ApolloClient,
  createHttpLink,
  InMemoryCache,
} from "@apollo/client/core";

export const apolloClient = new ApolloClient({
  link: createHttpLink({
    uri: "http://127.0.0.2:80/gql",
  }),
  cache: new InMemoryCache(),
});
