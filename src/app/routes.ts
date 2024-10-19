import { RouteRecordRaw } from "vue-router";
import HomePage from "../pages/home-page.vue";
import ViewPage from "../pages/view-page.vue";
import PostPage from "../pages/post-page.vue";

export const routes: RouteRecordRaw[] = [
  {
    path: "/",
    component: HomePage,
  },
  {
    path: "/post",
    component: PostPage,
  },
  {
    path: "/view",
    component: ViewPage,
  },
];
