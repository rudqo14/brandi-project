<template>
  <main>
    <article class="ProductInfo">
      <agile class="agile" :dots="false">
        <div class="imgContainer" v-for="(item, index) in detailData.image_list" v-bind:key="index">
          <img alt="product  image" :src="item" />
        </div>
        <div class="prevBtn" slot="prevButton"></div>
        <div class="nextBtn" slot="nextButton"></div>
      </agile>
      <div class="detailInfoContainer">
        <p class="title">{{ detailData.name }}</p>
        <div class="priceContainer">
          <span v-if="detailData.discount_rate" class="percent">{{ detailData.discount_rate }}%</span>
          <span class="price">
            {{
            (
            Math.round((detailData.price -
            detailData.price * (detailData.discount_rate / 100))/10)*10
            ).toLocaleString(5) + "원"
            }}
          </span>
          <span class="cost">
            {{
            Math.floor(detailData.price).toLocaleString(5) + "원"
            }}
          </span>
        </div>
        <hr />
        <div v-on:click="onColorClick" class="option">
          <div>{{ colorToggleData }}</div>
          <div class="imgContainer">
            <img src="https://www.brandi.co.kr/static/3.49.1/images/ic-arrow-bl-down@3x.png" />
          </div>
          <div
            v-bind:class="{
              toggleOn: isColorToggle,
              toggleOff: !isColorToggle,
            }"
          >
            <div class="defaultToggle">[색상]을 선택하세요.</div>
            <div
              v-for="(item, index) in detailData.colors"
              class="colorToggle"
              v-bind:key="index"
              @click="colorClickHandler(item)"
            >{{ item.color_name }}</div>
          </div>
        </div>
        <!-- 사이즈 옵션 -->
        <div v-on:click="onSizeClick" class="option">
          <div
            v-bind:class="{
              optionTitle: disabledSizeToggle,
              none: !disabledSizeToggle,
            }"
          >{{ sizeToggleData }}</div>
          <div class="imgContainer">
            <img src="https://www.brandi.co.kr/static/3.49.1/images/ic-arrow-bl-down@3x.png" />
          </div>
          <div
            v-bind:class="{
              toggleOn: isSizeToggle,
              toggleOff: !isSizeToggle,
            }"
          >
            <div class="defaultToggle">[사이즈]를 선택하세요.</div>
            <div
              v-for="(item, index) in colorData"
              class="colorToggle"
              v-bind:key="index"
              @click="optionSizeHandler(colorData, index)"
            >{{ item.size }}</div>
          </div>
        </div>
        <div
          v-bind:class="{
            selectedOptions: isPurchaseBox,
            noneOptions: !isPurchaseBox,
          }"
        >
          <div class="selectTitle">
            <p>{{ purchaseColor }} / {{ purchaseSize }}</p>
            <div @click="removeSelectHandler()" class="imgContainer">
              <img src="https://www.brandi.co.kr/static/3.49.1/images/img_icon_x.png" />
            </div>
          </div>
          <div class="selectPrice">
            <div class="caculatar">
              <button class="numberBtn" name="minus" @click="calculationHandler">-</button>
              <span class="border"></span>
              <input class="productNumber" :value="input" readonly />
              <span class="border"></span>
              <button class="numberBtn" name="plus" @click="calculationHandler">+</button>
            </div>
            <p>
              {{
              (
              (detailData.price -
              detailData.price * (detailData.discount_rate / 100)) *
              input
              ).toLocaleString(5) + "원"
              }}
            </p>
          </div>
        </div>
        <div class="detailpriceContainer">
          <p>총 {{ input }}개의 상품</p>
          <p class="totalPrice">
            총 금액
            <strong>
              {{
              (
              (detailData.price -
              detailData.price * (detailData.discount_rate / 100)) *
              input
              ).toLocaleString(5) + "원"
              }}
            </strong>
          </p>
        </div>
        <button @click="buyNowHandler" class="purchaseBtn">바로 구매하기</button>
      </div>
    </article>
    <article class="detailProduct">
      <div class="categoryContainer">
        <div class="productDetail">상품정보</div>
        <div>
          <!-- <div class="detailHtml" v-html="detailHtml" /> -->
        </div>
      </div>
    </article>
  </main>
</template>

<script>
import { gonhoIp } from "../../../config.js";
import axios from "axios";
import { VueAgile } from "vue-agile";

export default {
  created() {
    axios.get(`${gonhoIp}/product/${this.$route.params.id}`).then((res) => {
      console.log(res);
      this.detailData = res.data.data;
      this.purchaseId = this.detailData.product_id;
    });
  },

  data() {
    return {
      detailData: [],
      colorToggleData: "[색상]을 선택하세요.",
      isColorToggle: false,
      sizeToggleData: "[사이즈]를 선택하세요.",
      isSizeToggle: false,
      disabledSizeToggle: false,
      input: 0,
      isPurchaseBox: false,
      purchaseColor: "",
      purchaseColorId: "",
      purchaseSize: "",
      purchaseSizeId: "",
      purchaseId: "",
      colorData: [],
      // detailHtml: detailOption.data.html,
    };
  },
  components: {
    //이미지 Caroucel
    agile: VueAgile,
  },
  methods: {
    colorClickHandler(item) {
      //중복된 통신은 한번만 처리하도록 함
      if (this.colorToggleData === item.color_name) {
        return;
      }

      this.colorToggleData = item.color_name;
      this.purchaseColorId = item.color_id;

      axios
        .get(
          `${gonhoIp}/product/${this.$route.params.id}?color_id=${item.color_id}`
        )
        .then((res) => {
          this.colorData = res.data.data;
        });
    },

    //컬러 인풋 클릭시 토글 박스 열리게하기
    onColorClick() {
      this.isColorToggle = !this.isColorToggle;

      if (this.colorToggleData !== "[색상]을 선택하세요.") {
        this.disabledSizeToggle = !this.disabledSizeToggle;
      }

      this.isSizeToggle = false;
    },

    //사이즈 인풋클릭시 토글 박스 열리게하기
    onSizeClick() {
      if (this.colorToggleData !== "[색상]을 선택하세요.") {
        this.isSizeToggle = !this.isSizeToggle;
      }
    },

    //옵션 사이즈 토글에서 원하는 사이즈 선택시 적용
    optionSizeHandler(colorData, index) {
      this.sizeToggleData = colorData[index].size;
      this.purchaseInputNumber = this.input;
      this.input = 1;
      this.purchaseColor = this.colorToggleData;
      this.purchaseSize = this.sizeToggleData;
      this.purchaseSizeId = colorData[index].size_id;
      this.colorToggleData = "[색상]을 선택하세요.";
      this.sizeToggleData = "[사이즈]를 선택하세요.";
      this.isSizeToggle = false;
      this.isPurchaseBox = true;
    },

    //상품 수량 조절하여 갯수 띄워주기
    //+와 - 버튼을 클릭하여 조절한다.
    //최소,최대값 안의 input 값이라면 +, - 동작
    calculationHandler(e) {
      const { name } = e.target;
      const isPlus = name === "plus";

      if (!isPlus && this.input === 1)
        return alert("최소 구매 수량은 1개 입니다.");

      if (this.input === 20) return alert("최대 구매 수량은 20개 입니다.");

      input: isPlus ? (this.input += 1) : (this.input -= 1);
    },

    //삭제하기 버튼 클릭시 상품 구매 박스를 안보이게 적용
    removeSelectHandler() {
      if (confirm("정말 삭제하시겠습니까?") == true) {
        this.isPurchaseBox = false;
        this.input = 0;
      } else {
        return;
      }
    },

    //상품구매하기 버튼을 클릭하여 로컬스토리지 저장후 구매하기 페이지로 이동
    //상품의 갯수가 0이라면 return
    buyNowHandler() {
      if (this.input === 0) {
        alert("상품을 선택해주세요.");
        return;
      }

      localStorage.setItem("purchaseColor", this.purchaseColorId);
      localStorage.setItem("purchaseSize", this.purchaseSizeId);
      localStorage.setItem("purchaseProductNumber", this.input);
      localStorage.setItem("purchaseId", this.purchaseId);

      this.$router.push(`/order`);
    },
  },
};
</script>

<style lang="scss">
.ProductInfo {
  width: 1235px;
  margin: 140px auto 80px;
  display: flex;

  .agile {
    width: 546px;
    height: 546px;
    position: relative;

    .prevBtn {
      width: 32px;
      height: 32px;
      background-position: 0 0;
      left: 10px;
      top: 240px;
      position: absolute;
      background-image: url(https://www.brandi.co.kr/static/3.49.1/images/controls.png);
    }

    .nextBtn {
      width: 32px;
      height: 32px;
      background-position: -32px 0;
      right: 10px;
      top: 240px;
      position: absolute;
      background-image: url(https://www.brandi.co.kr/static/3.49.1/images/controls.png);
    }
  }

  .imgContainer {
    width: 546px;
    height: 546px;

    img {
      width: 100%;
      height: 100%;
    }
  }

  .detailInfoContainer {
    width: 53%;
    font-family: "Spoqa Han Sans", Sans-serif;
    margin-left: 50px;

    .title {
      font-size: 24px;
      line-height: 150%;
    }

    .priceContainer {
      margin: 16px 0 30px;

      .percent {
        font-size: 26px;
        font-weight: bold;
        color: #ff204b;
      }

      .price {
        font-size: 26px;
        font-weight: bold;
      }

      .cost {
        font-size: 20px;
        font-weight: 500;
        text-decoration: line-through;
        color: #929292;
      }
    }

    #none {
      cursor: default;
    }

    .option {
      height: 48px;
      border: 1px solid #e1e1e1;
      font-size: 13px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 10px;
      padding: 0 10px;
      position: relative;
      cursor: pointer;

      .none {
        color: #929292;
        font-size: 13px;
        cursor: default;
      }

      .optionTitle {
        color: black;
        font-size: 13px;
      }

      .toggleOff {
        display: none;
      }

      .toggleOn {
        width: 639px;
        top: 46.5px;
        left: -1px;
        position: absolute;
        z-index: 99;
        font-size: 13px;
        background-color: white;
        border: 1px solid #e1e1e1;

        .defaultToggle {
          height: 42px;
          opacity: 0.35;
          padding: 13px 10px 0;
        }

        .colorToggle {
          height: 42px;
          padding: 13px 10px 0;

          &:hover {
            background-color: #f8f8f8;
          }
        }
      }

      .imgContainer {
        width: 18px;
        height: 10px;

        img {
          width: 100%;
          height: 100%;
        }
      }
    }

    .detailpriceContainer {
      display: flex;
      justify-content: space-between;
      margin-top: 30px;
      font-weight: bold;
      font-size: 16px;

      .totalPrice {
        font-size: 20px;

        strong {
          color: #ff204b;
        }
      }
    }

    .noneOptions {
      display: none;
    }

    .selectedOptions,
    .noneOptions {
      height: 120px;
      border: 1px solid #f1f1f1;
      background-color: #fafafa;
      padding: 25px 20px 0;
      margin-top: 20px;

      .selectTitle {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;

        .imgContainer {
          width: 16px;
          height: 16px;
          cursor: pointer;

          img {
            width: 100%;
            height: 100%;
          }
        }
      }

      .selectPrice {
        display: flex;
        justify-content: space-between;

        .caculatar {
          height: 28px;
          border: 1px solid #cdcdcd;

          .border {
            height: 100%;
            border: 1px solid #cdcdcd;
          }

          .numberBtn {
            width: 28px;
            height: 28px;
            border: none;
            border-radius: 0;
            background: #00ff0000;
            font-size: 15px;
            color: #5d5d5d;
            outline: none;
            cursor: pointer;
            vertical-align: top;
            margin: 0;
            padding: 0;
          }

          .productNumber {
            width: 35px;
            height: 28px;
            border: none;
            background-color: #00ff0000;
            border-width: 1px 0;
            font-size: 13px;
            color: #666;
            text-align: center;
            margin: 0;
            padding: 0;
            outline: none;
          }
        }
      }
    }

    .purchaseBtn {
      width: 180px;
      height: 50px;
      background: black;
      color: white;
      border-radius: 5px;
      margin-top: 30px;
      outline: none;
      border: none;
      cursor: pointer;
    }
  }
}

.detailProduct {
  width: 1235px;
  margin: 0px auto 100px;
  display: flex;

  .categoryContainer {
    width: 100%;
    /* height: 100%; */
    border-bottom: 2px solid #dbdbdb;

    .productDetail {
      width: 250px;
      height: 44px;
      margin-left: 30px;
      padding-top: 15px;
      border-bottom: 2px solid #ff204b;
      color: #ff204b;
      text-align: center;
    }

    .detailContents {
      margin-top: 40px;
      font-size: 14px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      text-align: center;
    }
  }
}
</style>
