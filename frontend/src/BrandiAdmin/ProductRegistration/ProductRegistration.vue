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
        <v-btn depressed color="error" @click="registCansleHandler">
          <span>취소</span>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapActions, mapMutations, mapState, mapGetters } from "vuex";
import BasicInfo from "./Components/BasicInfo/BasicInfo";
import OptionInfo from "./Components/OptionInfo";
import SellingInfo from "./Components/SellingInfo";
import { ADMIN_API_URL } from "../../../config";

const AdminStore = "adminStore";

export default {
  created() {},
  computed: {},

  components: {
    BasicInfo,
    OptionInfo,
    SellingInfo,
  },

  data() {
    return {
      mainCategory: [],
      stateData: this.$store.state.adminStore,
    };
  },

  methods: {
    ...mapGetters(AdminStore, ["getData"]),
    ...mapMutations(AdminStore, ["registration"]),

    // 상품 등록 실행 메소드
    registrationHandler() {
      const productDatas = this.getData();

      const registOk = confirm("상품 등록을 하시겠습니까?");
      if (registOk === true) {
        const form = new FormData();
        form.append("sellYn", productDatas.sellYn);
        form.append("exhibitionYn", productDatas.exhibitionYn);
        form.append("productName", productDatas.productName);
        form.append("simpleDescription", productDatas.simpleDescription);
        form.append("product_image_1", productDatas.product_image_1);
        form.append("product_image_2", productDatas.product_image_2);
        form.append("product_image_3", productDatas.product_image_3);
        form.append("product_image_4", productDatas.product_image_4);
        form.append("product_image_5", productDatas.product_image_5);
        form.append("detailInformation", productDatas.detailInformation);

        // AdminStore 전체 데이터 확인용 메소드
        this.registration();

        // 상품 등록 데이터 POST 로 서버에 보내기
        axios
          .post(`${ADMIN_API_URL}/admin/product`, form, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          })
          .then((res) => {
            console.log("res: ", res);
            if (res) {
              alert("등록이 완료 되었습니다.");
              this.$router.push("admin/productManagement");
            }
          })
          .catch((error) => {
            console.log(error);
            alert("필수사항을 올바르게 입력해 주세요.");
          });
      }
    },

    registCansleHandler() {
      const registCancleOk = confirm("정말로 상품 등록을 취소하시겠습니까?");
      if (registCancleOk === true) {
        this.$router.push("/admin/productManagement");
      }
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
