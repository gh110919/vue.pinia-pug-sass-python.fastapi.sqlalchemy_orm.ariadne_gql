import { defineStore } from "pinia";
import { computed, ref } from "vue";

export type DataStore = Partial<{
  ids?: { id: string }[];
  item?: {
    __typename: string;
    id: string;
    name: string;
    value: string;
  };
}>;

export const useDataStore = defineStore("input", () => {
  const state = ref<DataStore>({
    ids: [],
    item: undefined,
  });

  return {
    storeData: computed(() => state.value),
    setDataStore: (payload: DataStore) => {
      Object.assign(state.value, payload);
    },
  };
});
