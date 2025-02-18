import {
  ApolloClient,
  createHttpLink,
  InMemoryCache,
} from "@apollo/client/core";

export const apolloClient = new ApolloClient({
  link: createHttpLink({
    uri: "https://127.0.0.2:443/gql",
  }),
  cache: new InMemoryCache(),
});
