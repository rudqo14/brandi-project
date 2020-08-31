<template>
  <div>
    <header>
      <div class="pageTitle">
        <span class="mainName">상품 등록</span>
        <span class="subName">상품 정보 등록</span>
      </div>
      <div class="pageStateBar">
        <i class="fas fa-home"></i>
        <span>상품 관리</span>
        <i class="fas fa-angle-right"></i>
        <span>상품 관리</span>
        <i class="fas fa-angle-right"></i>
        <span>상품 등록</span>
      </div>
    </header>
    <section class="pageContents">
      <BasicInfo />
      <OptionInfo />
      <SellingInfo />
    </section>
    <div class="RegistrationContainer">
      <div class="RegistrationBtn" @click="registrationHandler">
        <v-btn depressed color="success">
          <span>등록</span>
        </v-btn>
      </div>
      <div class="CancleBtn">
        <v-btn depressed color="error">
          <span>취소</span>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations } from "vuex";
import BasicInfo from "./Components/BasicInfo/BasicInfo";
import OptionInfo from "./Components/OptionInfo";
import SellingInfo from "./Components/SellingInfo";
import { ADMIN_API_URL } from "../../../config";

const AdminStore = "adminStore";

export default {
  created() {},

  components: {
    BasicInfo,
    OptionInfo,
    SellingInfo,
  },

  data() {
    return {
      mainCategory: [],
    };
  },

  methods: {
    ...mapMutations(AdminStore, ["registration", "postProductImages"]),
    registrationHandler() {
      this.registration();
      this.postProductImages();
    },
  },
};
</script>

<style lang="scss" scoped>
header {
  width: 100%;
  .pageTitle {
    margin: 25px;

    .mainName {
      font-size: 30px;
      color: #666;
    }

    .subName {
      font-size: 14px;
      color: #888;
    }
  }

  .pageStateBar {
    display: flex;
    align-items: center;
    width: 100%;
    height: 40px;
    padding-left: 25px;
    font-size: 15px;
    background-color: #eeeeee;

    .fas {
      color: gray;
      padding: 0 8px;
    }
  }
}

.pageContents {
  margin: 10px 5px;
  background-color: #fafafa;
}

.RegistrationContainer {
  display: flex;
  justify-content: center;
  margin-top: 20px;

  span {
    font-size: 16px;
  }

  .RegistrationBtn {
    margin-right: 10px;
  }
}
</style>
