import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import serviceStore from "./modules/serviceStore";
import adminStore from "./modules/adminStore";

const store = new Vuex.Store({
  modules: {
    serviceStore: serviceStore,
    adminStore: adminStore,
  },
});

export default store;
