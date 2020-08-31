const adminStore = {
  state: {
    sellYn: false,
    exhibitionYn: true,
    productName: "",
    simpleDescription: "",
    productImages: {
      product_image_1: "",
      product_image_2: "",
      product_image_3: "",
      product_image_4: "",
      product_image_5: "",
    },
  },

  getters: {},

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
      state.productImages.product_image_1 = productImage1;
    },
    deleteProductImage1(state, productImage1) {
      state.productImages.product_image_1 = productImage1;
    },
    getProductImage2(state, productImage2) {
      state.productImages.product_image_2 = productImage2;
    },
    deleteProductImage2(state, productImage2) {
      state.productImages.product_image_2 = productImage2;
    },
    getProductImage3(state, productImage3) {
      state.productImages.product_image_3 = productImage3;
    },
    deleteProductImage3(state, productImage3) {
      state.productImages.product_image_3 = productImage3;
    },
    getProductImage4(state, productImage4) {
      state.productImages.product_image_4 = productImage4;
    },
    deleteProductImage4(state, productImage4) {
      state.productImages.product_image_4 = productImage4;
    },
    getProductImage5(state, productImage5) {
      state.productImages.product_image_5 = productImage5;
    },
    deleteProductImage5(state, productImage5) {
      state.productImages.product_image_5 = productImage5;
    },
    postProductImages(state) {
      let formData = new FormData();
      formData.append("imageFile", state.productImages);

      // 데이터 확인 콘솔
      // console.log("imageFile:", ...formData)
      // new Response(formData).text().then(console.log);
      // for (var pair of formData.entries()) {
      //   console.log(pair[0] + ", " + pair[1]);
      // }
    },

    registration(state) {
      console.log("state.sellYn: ", state.sellYn);
      console.log("state.exhibitionYn: ", state.exhibitionYn);
      console.log("state.productName: ", state.productName);
      console.log("state.simpleDescription: ", state.simpleDescription);
      console.log(
        "state.productImages.product_image_2: ",
        state.productImages.product_image_2
      );
      console.log(
        "state.productImages.product_image_3: ",
        state.productImages.product_image_3
      );
      console.log(
        "state.productImages.product_image_4: ",
        state.productImages.product_image_4
      );
      console.log(
        "state.productImages.product_image_5: ",
        state.productImages.product_image_5
      );
      console.log(
        "state.productImages.product_image_1: ",
        state.productImages.product_image_1
      );
    },
  },

  actions: {},
};
