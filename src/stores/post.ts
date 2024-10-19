import { defineStore } from "pinia";
import { computed, ref } from "vue";

export type PostStore = Partial<{
    item: {
        __typename: string;
        id: string;
        name: string;
        value: string;
    };
}>;

export const usePostStore = defineStore("input", () => {
    const state = ref<PostStore>({
        item: undefined,
    });

    return {
        storePost: computed(() => state.value),
        setPostStore: (payload: PostStore) => {
            Object.assign(state.value, payload);
        },
    };
});
