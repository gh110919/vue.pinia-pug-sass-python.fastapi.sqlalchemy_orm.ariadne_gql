<script setup lang="ts">
import gql from "graphql-tag";
import { apolloClient } from "../utils/apollo-client";
import { useDataStore } from "../stores/data";

const { storeData, setDataStore } = useDataStore();

apolloClient
    .query({
        query: gql`
            query GetAllData {
                getAllData {
                    id
                }
            }
        `,
    })
    .then((r) => {
        if (r.data.getAllData) {
            setDataStore({
                ids: r.data.getAllData.map((e: any) => ({ id: e.id })),
            });
        }
    });

const handleClick = (id: string) => {
    apolloClient
        .query({
            query: gql`
                query GetData($id: ID!) {
                    getData(data: { id: $id }) {
                        id
                        name
                        value
                    }
                }
            `,
            variables: { id },
        })
        .then((r) => {
            if (r.data.getData) {
                setDataStore({ item: r.data.getData });
            }
        });
};
</script>

<template lang="pug">
section.container
    ul.list
        li.item(v-for="(e, i) in storeData.ids" :key="i")
            button.btn(@click="handleClick(e.id)") {{ e.id }}
    div.data
        p {{ storeData.item?.id }}
        p {{ storeData.item?.name }}
        p {{ storeData.item?.value }}
</template>

<style scoped lang="sass">
.container
    display: flex
    flex-direction: column
    align-items: center
    gap: 16px
.list
    display: grid
    grid-template-columns: repeat(5, 1fr)
    gap: 8px
.item
    outline: 1px solid blue
    display: flex
    justify-content: center
    align-items: center
.btn
    padding: 4px
    background: transparent
.data
    display: flex
    flex-direction: column
    gap: 4px
</style>
