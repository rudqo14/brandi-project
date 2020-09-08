const adminStore = {
  namespaced: true,
  state: {
    sellYn: 1,
    exhibitionYn: 1,
    mainCategoryId: null,
    subCategoryId: null,
    productName: null,
    simpleDescription: null,
    product_image_1: null,
    product_image_2: null,
    product_image_3: null,
    product_image_4: null,
    product_image_5: null,
    formDatas: null,
    detailInformation: null,
    optionQuantity: null,
    price: 0,
    discountRate: null,
    discountStartDate: null,
    discountEndDate: null,
    minSalesQuantity: 1,
    maxSalesQuantity: 20,
    optionQuantity: null,
  },

  getters: {
    getData(state) {
      return state;
    },
    getPrice(state) {
      return state.price;
    },
    getDiscountRate(state) {
      return state.discountRate;
    },
  },

  mutations: {
    sellYesHandler(state) {
      state.sellYn = 1;
    },
    sellNoHandler(state) {
      state.sellYn = 0;
    },
    exhibitionYes(state) {
      state.exhibitionYn = 1;
    },
    exhibitionNo(state) {
      state.exhibitionYn = 0;
    },

    getMainCategoryId(state, mainCategoryId) {
      state.mainCategoryId = mainCategoryId;
    },

    getSubCategoryId(state, subCategoryId) {
      state.subCategoryId = subCategoryId;
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
    upDateDetailInformation(state, detailInformation) {
      state.detailInformation = detailInformation;
    },
    insertSellingPrice(state, sellingPrice) {
      state.price = sellingPrice;
    },
    insertDiscountRate(state, discountRate) {
      state.discountRate = discountRate;
    },
    insertDiscountPeriod(state, date) {
      if (date === null) {
        state.discountStartDate = null;
        state.discountEndDate = null;
      } else {
        state.discountStartDate = date[0];
        state.discountEndDate = date[1];
      }
    },
    insertMinQuantity(state, value) {
      state.minSalesQuantity = value;
    },
    insertMaxQuantity(state, value) {
      state.maxSalesQuantity = value;
    },

    upDateAllOptions(state, optionQuantity) {
      state.optionQuantity = optionQuantity;
    },

    // ProductRegistration.vue 에서 state 데이터 확인용
    registration(state) {
      console.log("state.sellYn: ", state.sellYn);
      console.log("state.exhibitionYn: ", state.exhibitionYn);
      console.log("state.mainCategoryId: ", state.mainCategoryId);
      console.log("state.subCategoryId: ", state.subCategoryId);
      console.log("state.productName: ", state.productName);
      console.log("state.simpleDescription: ", state.simpleDescription);
      console.log("state.product_image_1: ", state.product_image_2);
      console.log("state.product_image_2: ", state.product_image_3);
      console.log("state.product_image_3: ", state.product_image_4);
      console.log("state.product_image_4: ", state.product_image_5);
      console.log("state.product_image_5: ", state.product_image_1);
      console.log("state.detailInformation: ", state.detailInformation);
      console.log("state.allOptions: ", state.optionQuantity);
      console.log("state.price: ", state.price);
      console.log("state.discountRate: ", state.discountRate);
      console.log("state.discountStartDate: ", state.discountStartDate);
      console.log("state.discountEndDate: ", state.discountEndDate);
      console.log("state.minSalesQuantity: ", state.minSalesQuantity);
      console.log("state.maxSalesQuantity: ", state.maxSalesQuantity);
    },
  },

  actions: {},
};

export default adminStore;
