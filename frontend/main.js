import Vue from "vue";
import App from "./src/App.vue";
import { store } from "./src/BrandiAdmin/Store/store";
import { router } from "./src/router/index.js";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";

Vue.use(Vuetify);

new Vue({
  icons: {
    iconfont: "mdi", // default - only for display purposes
  },
  vuetify: new Vuetify(),
  render: (h) => h(App),
  router,
  store,
}).$mount("#root");
