import Vue from "../../node_modules/vue";
import VueRouter from "../../node_modules/vue-router";
import Main from "../BrandiService/Main/Main.vue";
import Detail from "../BrandiService/Detail/Detail.vue";
import Login from "../BrandiService/Login/Login.vue";

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
      component: Login,
    },
    {
      path: "/",
      redirect: "/main",
    },
  ],
});
