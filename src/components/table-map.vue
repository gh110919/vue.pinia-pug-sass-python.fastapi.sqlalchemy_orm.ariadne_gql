<script setup lang="ts">
import { ref } from "vue";
import { useFormStore } from "../stores/form";
import { useInputStore } from "../stores/inputs";

const props = defineProps<{
    label: string;
    array: {
        name: string;
        field: string;
        placeholder: string;
        pattern: string;
    }[];
}>();

const { setInputsStore } = useInputStore();
const { setFormStore } = useFormStore();

const formRef = ref<HTMLFormElement | null>(null);

const handleFormChange = () => {
    setFormStore({ valid: formRef.value?.checkValidity() });
};

const handleInputChange = (e: Event, field: string) => {
    const target = e.target as HTMLInputElement;
    setInputsStore({ [field]: target.value });
};
</script>

<template lang="pug">
section.container
    div(style="display: flex; flex-direction: column; gap: 16px")
        p {{ props.label }}
        form.form(action, ref="formRef", @change="handleFormChange")
            ul.list
                li.item(v-for="(e, i) in props.array", :key="i")
                    label.label(:for="e.field") {{ e.name }}
                    input.input(
                        required, 
                        type="text", 
                        :id="e.field", 
                        :placeholder="e.placeholder", 
                        :pattern="e.pattern", 
                        @input="(event) => handleInputChange(event, e.field)"
                        )
</template>

<style scoped lang="sass">
.container
    display: flex
    gap: 16px
.wrapper
    display: flex
    flex-direction: column
    gap: 16px
.form
    display: flex
.list
    display: grid
    grid-template-columns: repeat(1, 1fr)
    gap: 8px
.item
    display: flex
    gap: 16px
.label
    display: flex
    justify-content: center
    width: 100%
    padding: 8px
    outline: 1px solid
.input
    padding: 8px
    &:invalid
        border-color: red
</style>
