import Vue from "vue";
import App from "./src/App.vue";

import { router } from "./src/router/index.js";

new Vue({
  render: (h) => h(App),
  router,
}).$mount("#root");
j;
