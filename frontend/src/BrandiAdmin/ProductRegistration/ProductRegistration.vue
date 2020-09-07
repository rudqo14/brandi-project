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
import { SERVER_IP } from "../../../config";

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

      const form = new FormData();
      form.append("sellYn", productDatas.sellYn);
      form.append("exhibitionYn", productDatas.exhibitionYn);
      form.append("mainCategoryId", productDatas.mainCategoryId);
      form.append("subCategoryId", productDatas.subCategoryId);
      form.append("productName", productDatas.productName);
      form.append("simpleDescription", productDatas.simpleDescription);
      form.append("product_image_1", productDatas.product_image_1);
      form.append("product_image_2", productDatas.product_image_2);
      form.append("product_image_3", productDatas.product_image_3);
      form.append("product_image_4", productDatas.product_image_4);
      form.append("product_image_5", productDatas.product_image_5);
      form.append("detailInformation", productDatas.detailInformation);
      form.append(
        "optionQuantity",
        JSON.stringify(productDatas.optionQuantity)
      );
      form.append("price", productDatas.price);
      form.append("discountRate", productDatas.discountRate);
      form.append("discountStartDate", productDatas.discountStartDate);
      form.append("discountEndDate", productDatas.discountEndDate);
      form.append("minSalesQuantity", productDatas.minSalesQuantity);
      form.append("maxSalesQuantity", productDatas.maxSalesQuantity);

      // 필수항목들이 모두 입력 됐는지 확인하는 메소드
      const checkingData = () => {
        if (productDatas.mainCategoryId === null) {
          alert("1차 카테고리를 선택해주세요.");
        } else if (productDatas.subCategoryId === null) {
          alert("2차 카테고리를 선택해주세요.");
        } else if (productDatas.productName === null) {
          alert("상품명을 입력해주세요.");
        } else if (productDatas.product_image_1 === null) {
          alert("대표이미지를 등록해주세요.");
        } else if (productDatas.detailInformation === null) {
          alert("상세상품정보를 입력해주세요.");
        } else if (productDatas.allOptions === null) {
          alert("옵션을 선택해주세요.");
        } else if (productDatas.price === 0) {
          alert("판매가를 입력해주세요.");
        } else {
          return true;
        }
      };

      // 필수항목 입력 확인하고 상품 등록 확인
      if (checkingData()) {
        const registOk = confirm("상품 등록을 하시겠습니까?");

        if (registOk === true) {
          // AdminStore 전체 데이터 확인용 메소드
          this.registration();

          // 상품 등록 데이터 POST 로 서버에 보내기
          axios
            .post(`${SERVER_IP}/admin/product`, form, {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            })

            // 상품 등록이 완료되면 상품 관리 페이지로 이동
            .then((res) => {
              console.log("res: ", res);
              if (res) {
                alert("등록이 완료 되었습니다.");
                this.$router.push("/admin/productManagement");
              }
            })

            // 서버로 상품 등록이 제대로 되지 않을 경우 경고 메시지
            .catch((error) => {
              console.log(error);
              alert("필수사항을 올바르게 입력해 주세요.");
            });
        }
      }
    },

    // 상품 등록 취소 메소드: 취소 누르면 상품 관리 페이지로 이동
    registCansleHandler() {
      const registCancleOk = confirm("정말로 상품 등록을 취소하시겠습니까?");
      if (registCancleOk) {
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
