import { defineStore } from "pinia";
import { computed, ref } from "vue";

export type FormStore = Partial<{
    valid: boolean;
}>;

export const useFormStore = defineStore("form", () => {
    const state = ref<FormStore>({
        valid: false,
    });

    return {
        storeForm: computed(() => state.value),
        setFormStore: (payload: FormStore) => {
            state.value.valid = payload.valid;
        },
    };
});
