<script setup lang="ts">
import gql from "graphql-tag";
import TableMap from "../components/table-map.vue";
import { useInputStore } from "../stores/inputs.ts";
import { apolloClient } from "../utils/apollo-client.ts";
import { useFormStore } from "../stores/form.ts";
import { ref } from "vue";

const inputs = [
    {
        name: "Имя",
        field: "name",
        placeholder: "Введите имя",
        pattern: "[A-Za-z0-9А-Яа-яЁё ]{4,64}",
    },
    {
        name: "Значение",
        field: "value",
        placeholder: "Введите значение",
        pattern: "[A-Za-z0-9А-Яа-яЁё ]{4,64}",
    },
];

const { storeInputs } = useInputStore();
const { storeForm } = useFormStore();

const postRef = ref<{
    __typename: string;
    id: string;
    name: string;
    value: string;
}>();

const handleClick = () => {
    const { name, value } = storeInputs;

    apolloClient
        .mutate({
            mutation: gql`
                mutation CreateData($name: String, $value: String) {
                    createData(data: { name: $name, value: $value }) {
                        id
                        name
                        value
                    }
                }
            `,
            variables: { name, value },
        })
        .then((r) => {
            if (r.data.createData.id) {
                postRef.value = r.data.createData;
            }
        });
};
</script>

<template lang="pug">
section.container 
    TableMap(label="Форма", :array="inputs")
    button(@click="handleClick", :disabled="!storeForm.valid") Отправить 
    div 
        p {{ postRef?.id }} 
        p {{ postRef?.name }} 
        p {{ postRef?.value }}
</template>

<style scoped lang="sass">
.container
    display: flex
    flex-direction: column
    gap: 16px

button
    padding: 8px
    outline: 1px solid blue
    &:disabled
        outline: 1px solid red
</style>
