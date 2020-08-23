import Vue from "vue";
import VueRouter from "vue-router";
import Main from "../BrandiService/Main.vue";
import Detail from "../BrandiService/Detail.vue";
import SignIn from "../BrandiService/SignIn/SignIn.vue";
// import ClientId from "../../config.js";
// import { LoaderPlugin } from "vue-google-login";

// Vue.use(LoaderPlugin, {
//   Client_id: ClientId,
// });

// Vue.GoogleAuth.then((auth2) => {
//   console.log(auth2.isSignedIn.get());
//   console.log(auth2.currentUser.get());
// });

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
      redirect: "/login",
    },
  ],
});
