import Vue from "vue";
import App from "./src/App.vue";
import store from "./src/Store/index";
import { router } from "./src/router/index.js";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";
Vue.config.productionTip = false;

Vue.use(Antd);
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
