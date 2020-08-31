const serviceStore = {
  namespaced: true,
  state: {
    accessToken: "",
  },
  getters: {
    getToken(state) {
      if (state.accessToken) {
        return true;
      }
      return false;
    },
  },
};

export default serviceStore;
