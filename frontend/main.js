import Vue from "vue";
import App from "./src/App.vue";
import { router } from "./src/router/index.js";
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
Vue.use(Vuetify);

new Vue({
  vuetify: new Vuetify(),
  render: (h) => h(App),
  router,
}).$mount("#root");
