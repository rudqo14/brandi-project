import Vue from "../../node_modules/vue";
import VueRouter from "../../node_modules/vue-router";
import Main from "../BrandiService/Main/Main.vue";
import Detail from "../BrandiService/Detail/Detail.vue";
import Login from "../BrandiService/Login/Login.vue";
import AdminFrame from "../BrandiAdmin/Components/AdminFrame.vue";
import Header from "../BrandiService/Components/Header.vue"

Vue.use(VueRouter);

export const router = new VueRouter({
  mode: "history",
  routes: [

    {
      path: "/header",
      component: Header,
      children: [
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
      ]
    },

    {
      //초기 url을 main으로 적용
      path: "/",
      redirect: "/main",
    },
    {
      path: "/admin",
      component: AdminFrame,
    }
  ],
});
