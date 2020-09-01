const adminStore = {
  namespaced: true,
  state: {
    sellYn: null,
    exhibitionYn: null,
    productName: "",
    simpleDescription: "",
    product_image_1: "",
    product_image_2: "",
    product_image_3: "",
    product_image_4: "",
    product_image_5: "",
    formDatas: null,
    detailInformation: null,
    // price
    // discountRate
    // discountStartDate
    // discountEndDate
    // minSalesQuantity
    // maxSalesQuantity
    // optionQuantity
  },

  getters: {
    getData(state) {
      return state;
    },
  },

  mutations: {
    sellYesHandler(state) {
      state.sellYn = true;
    },
    sellNoHandler(state) {
      state.sellYn = false;
    },
    exhibitionYes(state) {
      state.exhibitionYn = true;
    },
    exhibitionNo(state) {
      state.exhibitionYn = false;
    },
    updateProductName(state, productName) {
      state.productName = productName;
    },
    updateSimpleDescription(state, simpleDescription) {
      state.simpleDescription = simpleDescription;
    },
    getProductImage1(state, productImage1) {
      state.product_image_1 = productImage1;
    },
    deleteProductImage1(state, productImage1) {
      state.product_image_1 = productImage1;
    },
    getProductImage2(state, productImage2) {
      state.product_image_2 = productImage2;
    },
    deleteProductImage2(state, productImage2) {
      state.product_image_2 = productImage2;
    },
    getProductImage3(state, productImage3) {
      state.product_image_3 = productImage3;
    },
    deleteProductImage3(state, productImage3) {
      state.product_image_3 = productImage3;
    },
    getProductImage4(state, productImage4) {
      state.product_image_4 = productImage4;
    },
    deleteProductImage4(state, productImage4) {
      state.product_image_4 = productImage4;
    },
    getProductImage5(state, productImage5) {
      state.product_image_5 = productImage5;
    },
    deleteProductImage5(state, productImage5) {
      state.product_image_5 = productImage5;
    },
    detailInformation(state, detailInformation) {
      state.detailInformation = detailInformation;
    },

    // state 데이터 확인용
    registration(state) {
      state.productName;
      console.log("state.sellYn: ", state.sellYn);
      console.log("state.exhibitionYn: ", state.exhibitionYn);
      console.log("state.productName: ", state.productName);
      console.log("state.simpleDescription: ", state.simpleDescription);
      console.log("state.product_image_1: ", state.product_image_2);
      console.log("state.product_image_2: ", state.product_image_3);
      console.log("state.product_image_3: ", state.product_image_4);
      console.log("state.product_image_4: ", state.product_image_5);
      console.log("state.product_image_5: ", state.product_image_1);
      console.log("state.detailInformation: ", state.detailInformation);
    },
  },

  actions: {},
};

export default adminStore;
