import { createPinia } from "pinia";
import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import entryPoint from "./app/entry-point.vue";
import { routes } from "./app/routes";

const state = createPinia();
const router = createRouter({ routes, history: createWebHistory() });

createApp(entryPoint).use(router).use(state).mount("#app");
