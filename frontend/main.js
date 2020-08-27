import Vue from "vue";
import App from "./src/App.vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";

Vue.use(Vuetify);

import { router } from "./src/router/index.js";

new Vue({
  vuetify: new Vuetify(),
  render: (h) => h(App),
  router,
}).$mount("#root");
