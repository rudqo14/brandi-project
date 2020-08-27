import Vue from "vue";
import VueRouter from "vue-router";
import Main from "../BrandiService/Main/Main.vue";
import Detail from "../BrandiService/Detail/Detail.vue";
import Login from "../BrandiService/Login/Login.vue";
import VueAgile from "vue-agile";
import AdminFrame from "../BrandiAdmin/Components/AdminFrame.vue";
import Order from "../BrandiService/Order/order.vue";
import Footer from "../BrandiService/Components/Footer.vue";

Vue.use(VueAgile);
Vue.use(VueRouter);

export const router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/footer",
      component: Footer,
    },
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
      path: "/order",
      component: Order,
    },
    {
      //초기 url을 main으로 적용
      path: "/",
      redirect: "/main",
    },
    {
      path: "/admin",
      component: AdminFrame,
    },
    {
      path: "/footer",
      component: Footer,
    },
  ],
});
