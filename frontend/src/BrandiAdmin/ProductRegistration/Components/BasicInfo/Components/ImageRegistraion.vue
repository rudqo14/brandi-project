<template>
  <div class="imageRegistration">
    <div class="inputName">
      <div>이미지 등록</div>
      <div class="requiredMark">*</div>
    </div>
    <div class="inputPlace">
      <div class="imageContainer">
        <div class="imgWraaper">
          <div class="imgBox">
            <v-img
              width="100%"
              height="100%"
              :src="imageURL1"
              alt="img"
            ></v-img>
          </div>
          <input
            ref="imageURL1"
            type="file"
            multiple="multiple"
            hidden
            @change="(e) => onChangeImages1(e, 1)"
          />
          <v-btn type="button" normal @click="onClickImageUpload1">
            <span class="firstImgText">*대표 이미지</span>
            선택
          </v-btn>
          <div
            class="deleteBtnBox"
            @click="imageDelete1"
            v-if="this.imageURL1.length > 1"
          >
            <v-btn type="button" normal color="error">
              <span class="deleteImg">삭제</span>
            </v-btn>
          </div>
        </div>
        <div class="imgWraaper">
          <div class="imgBox">
            <v-img
              width="100%"
              height="100%"
              :src="imageURL2"
              alt="img"
            ></v-img>
          </div>
          <input
            ref="imageInput2"
            type="file"
            hidden
            @change="(e) => onChangeImages2(e)"
          />
          <v-btn type="button" normal @click="onClickImageUpload2">
            이미지
            <span>선택</span>
          </v-btn>
          <div
            class="deleteBtnBox"
            @click="imageDelete2"
            v-if="this.imageURL2.length > 1"
          >
            <v-btn type="button" normal color="error">
              <span class="deleteImg">삭제</span>
            </v-btn>
          </div>
        </div>
        <div class="imgWraaper">
          <div class="imgBox">
            <v-img
              width="100%"
              height="100%"
              :src="imageURL3"
              alt="img"
            ></v-img>
          </div>
          <input
            ref="imageInput3"
            type="file"
            hidden
            @change="(e) => onChangeImages3(e)"
          />
          <v-btn type="button" normal @click="onClickImageUpload3">
            이미지
            <span>선택</span>
          </v-btn>
          <div
            class="deleteBtnBox"
            @click="imageDelete3"
            v-if="this.imageURL3.length > 1"
          >
            <v-btn type="button" normal color="error">
              <span class="deleteImg">삭제</span>
            </v-btn>
          </div>
        </div>
        <div class="imgWraaper">
          <div class="imgBox">
            <v-img
              width="100%"
              height="100%"
              :src="imageURL4"
              alt="img"
            ></v-img>
          </div>
          <input
            ref="imageInput4"
            type="file"
            hidden
            @change="(e) => onChangeImages4(e)"
          />
          <v-btn type="button" normal @click="onClickImageUpload4">
            이미지
            <span>선택</span>
          </v-btn>
          <div
            class="deleteBtnBox"
            @click="imageDelete4"
            v-if="this.imageURL4.length > 1"
          >
            <v-btn type="button" normal color="error">
              <span class="deleteImg">삭제</span>
            </v-btn>
          </div>
        </div>
        <div class="imgWraaper">
          <div class="imgBox">
            <v-img
              width="100%"
              height="100%"
              :src="imageURL5"
              alt="img"
            ></v-img>
          </div>
          <input
            ref="imageInput5"
            type="file"
            hidden
            @change="(e) => onChangeImages5(e)"
          />
          <v-btn type="button" normal @click="onClickImageUpload5">
            이미지
            <span>선택</span>
          </v-btn>
          <div
            class="deleteBtnBox"
            @click="imageDelete5"
            v-if="this.imageURL5.length > 1"
          >
            <v-btn type="button" normal color="error">
              <span class="deleteImg">삭제</span>
            </v-btn>
          </div>
        </div>
      </div>
      <div class="alertText">
        <i class="fas fa-exclamation-triangle"></i> 640 * 720 사이즈 이상 등록
        가능하며 확장자는 jpg 만 등록 가능합니다.
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import { mapMutations, mapState } from "vuex";

const AdminStore = "adminStore";

export default {
  data() {
    return {
      imageURL1: "",
      imageURL2: "",
      imageURL3: "",
      imageURL4: "",
      imageURL5: "",
    };
  },

  computed: {
    ...mapState(AdminStore, {
      productImage1: (state) => state.productImages.product_image_1,
      productImage2: (state) => state.productImages.product_image_2,
      productImage3: (state) => state.productImages.product_image_3,
      productImage4: (state) => state.productImages.product_image_4,
      productImage5: (state) => state.productImages.product_image_5,
    }),
  },
  methods: {
    ...mapMutations(AdminStore, [
      "getProductImage1",
      "getProductImage2",
      "getProductImage3",
      "getProductImage4",
      "getProductImage5",
      "deleteProductImage1",
      "deleteProductImage2",
      "deleteProductImage3",
      "deleteProductImage4",
      "deleteProductImage5",
    ]),

    onClickImageUpload1() {
      this.$refs.imageURL1.click();
    },
    onChangeImages1(e) {
      const file = e.target.files[0];
      this.imageURL1 = URL.createObjectURL(file);

      // mapMutations 를 사용해서 this.$store.commit("getProductImage1", file) 대신 아래처럼 짧아진 코드
      this.getProductImage1(file);
    },
    imageDelete1() {
      this.imageURL1 = "null";
      this.deleteProductImage1(null);
    },
    onClickImageUpload2() {
      this.$refs.imageInput2.click();
    },
    onChangeImages2(e) {
      const file = e.target.files[0];
      this.imageURL2 = URL.createObjectURL(file);
      this.getProductImage2(file);
    },
    imageDelete2() {
      this.imageURL2 = "null";
      this.deleteProductImage2(null);
    },
    onClickImageUpload3() {
      this.$refs.imageInput3.click();
    },
    onChangeImages3(e) {
      const file = e.target.files[0];
      this.imageURL3 = URL.createObjectURL(file);
      this.getProductImage3(file);
    },
    imageDelete3() {
      this.imageURL3 = "null";
      this.deleteProductImage3(null);
    },
    onClickImageUpload4() {
      this.$refs.imageInput4.click();
    },
    onChangeImages4(e) {
      const file = e.target.files[0];
      this.imageURL4 = URL.createObjectURL(file);
      this.getProductImage4(file);
    },
    imageDelete4() {
      this.imageURL4 = "null";
      this.deleteProductImage4(null);
    },
    onClickImageUpload5() {
      this.$refs.imageInput5.click();
    },
    onChangeImages5(e) {
      const file = e.target.files[0];
      this.imageURL5 = URL.createObjectURL(file);
      this.getProductImage5(file);
    },
    imageDelete5() {
      this.imageURL5 = "null";
      this.deleteProductImage5(null);
    },
    // handleChange: function (e) {
    //   const file = e.target.files[0];
    //   if (file && file.type.match(/^image\/(png|jpeg)$/)) {
    //     this.preview = window.URL.createObjectURL(file);
    //   }
    // },
  },
};
</script>

<style lang="scss" scoped>
.imageRegistration {
  display: flex;
  height: 350px;
  border-bottom: 1px solid lightgray;

  .inputName {
    display: flex;
    align-items: center;
    width: 302px;
    height: 100%;
    padding-left: 15px;
    border-right: 1px solid lightgray;
    font-size: 15px;

    .requiredMark {
      margin-left: 4px;
      color: red;
    }
  }

  .inputPlace {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 10px;

    .alertText {
      color: #1e90ff;
      margin: 2px 0;
      font-size: 14px;
      margin-top: 30px;
    }

    .imageContainer {
      display: flex;

      .imgWraaper {
        display: flex;
        flex-direction: column;
        margin-right: 15px;

        .v-btn__content {
          .firstImgText {
            font-size: 15px;
            font-weight: bold;
            color: #1e90ff;
          }
        }
        .imgBox {
          width: 200px;
          height: 200px;
          border: 1px solid lightgray;
        }

        .deleteBtnBox {
          width: 100%;
          margin-top: 5px;
        }
      }
    }
  }
}
</style>
