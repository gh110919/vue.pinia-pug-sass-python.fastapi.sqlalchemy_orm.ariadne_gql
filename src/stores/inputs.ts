import { defineStore } from "pinia";
import { computed, ref } from "vue";

export type InputsStore = Partial<{
    name: string;
    value: string;
}>;

export const useInputStore = defineStore("input", () => {
    const state = ref<InputsStore>({});

    return {
        storeInputs: computed(() => state.value),
        setInputsStore: (payload: InputsStore) => {
            Object.assign(state.value, payload);
        },
    };
});
