import Vue from "../../node_modules/vue";
import VueRouter from "../../node_modules/vue-router";
import Main from "../BrandiService/Main/Main.vue";
import Detail from "../BrandiService/Detail/Detail.vue";
import Login from "../BrandiService/Login/Login.vue";
import VueAgile from "vue-agile";
import AdminFrame from "../BrandiAdmin/Components/AdminFrame.vue";
import ProductRegistration from "../BrandiAdmin/ProductRegistration/ProductRegistration.vue";
import Order from "../BrandiService/Order/order.vue";
import Footer from "../BrandiService/Components/Footer.vue";
import ProductManagement from "../BrandiAdmin/ProductRegistration/ProductManagement.vue";

Vue.use(VueAgile);
Vue.use(VueRouter);

export const router = new VueRouter({
  mode: "hash",
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
      name: AdminFrame,
      children: [
        {
          path: "productRegistration",
          component: ProductRegistration,
          name: "productRegistration",
        },
        {
          path: "ProductManagement",
          component: ProductManagement,
          name: "ProductManagement",
        },
      ],
    },
    {
      path: "/footer",
      component: Footer,
    },
  ],
});
