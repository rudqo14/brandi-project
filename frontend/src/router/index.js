import Vue from "./node_modules/vue";
import VueRouter from "./node_modules/vue-router";
import Main from "../BrandiService/Main.vue";
import Detail from "../BrandiService/Detail.vue";
import SignIn from "../BrandiService/SignIn/SignIn.vue";

Vue.use(VueRouter);

export const router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/main",
      component: Main,
    },
    {
      path: "/detail",
      component: Detail,
    },
    {
      path: "/login",
      component: SignIn,
    },
    {
      path: "/",
      redirect: "/main",
    },
  ],
});
