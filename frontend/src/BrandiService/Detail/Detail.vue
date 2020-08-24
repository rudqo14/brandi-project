<template>
  <main>
    <article class="ProductInfo">
      <div class="slideImgContainer">
        <img
          alt="product  image"
          src="https://image.brandi.me/cproduct/2020/06/26/17741364_1593101362_image1_L.jpg"
        />
      </div>
      <div class="detailInfoContainer">
        <p class="title">{{ detailData.product_name }}</p>
        <div class="priceContainer">
          <span class="percent">{{detailData.discount_rate}}%</span>
          <span
            class="price"
          >{{detailData.price -((detailData.price) * (detailData.discount_rate/100))+"원"}}</span>
          <span class="cost">{{Math.floor(detailData.price).toLocaleString(5) + "원"}}</span>
        </div>
        <hr />
        <div v-on:click="onColorClick" class="optionColor">
          <div>[색상]을 선택하세요.</div>
          <div class="imgContainer">
            <img src="https://www.brandi.co.kr/static/3.49.1/images/ic-arrow-bl-down@3x.png" />
          </div>
          <div v-bind:class="{'toggleOn':isColorToggle, 'toggleOff':!isColorToggle}">
            <div class="defaultToggle">[색상]을 선택하세요.</div>
            <div
              v-for="(item,index) in detailData.option_colors"
              class="colorToggle"
              v-bind:key="index"
            >{{item}}</div>
          </div>
        </div>
        <div class="optionColor">
          <div>[사이즈]를 선택하세요.</div>
          <div class="imgContainer">
            <img src="https://www.brandi.co.kr/static/3.49.1/images/ic-arrow-bl-down@3x.png" />
          </div>
        </div>
        <div class="detailpriceContainer">
          <p>총 0개의 상품</p>
          <p class="totalPrice">
            총 금액
            <strong>0 원</strong>
          </p>
        </div>
        <button class="purchase">바로 구매하기</button>
      </div>
    </article>
    <article class="detailProduct">
      <div class="categoryContainer">
        <div class="productDetail">상품정보</div>
      </div>
      <div></div>
    </article>
  </main>
</template>

<script>
import { ip } from "../../../config.js";
import axios from "axios";
import detailData from "../../../Data/Detail.json";

export default {
  data() {
    return {
      isColorToggle: false,

      message:
        "[키작녀추천] 허리끈 찰랑 데일리 물결 하이웨스트 와이드 팬츠 (7color) _ 미니클로젯",
      detailData: detailData.data,
    };
  },
  methods: {
    onColorClick() {
      this.isColorToggle = !this.isColorToggle;
    },

    toggleOnTop() {
      this.isColorToggle = !this.isColorToggle;
    },
  },
  computed: {
    toggleActive() {
      return {
        isColorToggle: this.isColorToggle,
        toggleOn: this.isColorToggle,
        toggleOff: !this.isColorToggle,
      };
    },
  },
};
</script>

<style lang="scss" scoped>
.ProductInfo {
  width: 1235px;
  margin: 200px auto 80px;
  display: flex;

  .slideImgContainer {
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

    .optionColor {
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

      .toggleOff {
        display: none;
      }

      .toggleOn {
        width: 646px;
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

    .purchase {
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
    height: 45px;
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
  }
}
</style>
