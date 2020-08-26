<template>
  <div>
    <Header />
    <main>
      <article class="orderContainer">
        <h1 class="orderTitle">주문하기</h1>
        <h2 class="orderSubTitle">브랜디 배송 상품</h2>
        <div class="category">
          <div class="categoryTitle">더데이즈</div>
          <div class="priceOrder">주문금액</div>
        </div>
        <div class="product">
          <div class="productInfoContainer">
            <div class="imgContainer">
              <img src="/Images/18944946_1597391611_image1_S.jpg" />
            </div>
            <div class="optionContainer">
              <h3>상큼 단가라 박시티 4col_더데이즈</h3>
              <p class="option">흰색</p>
              <p class="option">1개</p>
            </div>
          </div>
          <div class="price">14,490원</div>
        </div>
        <p class="totalPrice">
          총 주문금액
          <strong>14,490원</strong>
        </p>
      </article>
      <article class="orderInfo">
        <h1>주문자 정보</h1>
        <div class="orderInfoContainer">
          <span class="name">이름</span>
          <input class="nameInput" placeholder="이름" />
        </div>
        <div class="orderInfoContainer">
          <span class="name">휴대폰</span>
          <input class="phoneNumber" />
          <p>-</p>
          <input class="phoneNumber" />
          <p>-</p>
          <input class="phoneNumber" />
        </div>
        <div class="orderInfoContainer">
          <span class="name">이메일</span>
          <input class="email" />
          <p>@</p>
          <input class="email" />
        </div>
      </article>
      <article class="orderInfo">
        <div class="deliveredContainer">
          <span>배송지 정보</span>
          <span class="deliveredBtn">
            <label class="checkboxLable">
              <input class="checkboxBtn" type="checkbox" />
              주문자 정보와 동일
            </label>
          </span>
        </div>
        <div class="orderInfoContainer">
          <span class="name">이름</span>
          <input class="nameInput" placeholder="이름" disabled />
        </div>
        <div class="orderInfoContainer">
          <span class="name">휴대폰</span>
          <input class="phoneNumber" disabled />
          <p>-</p>
          <input class="phoneNumber" disabled />
          <p>-</p>
          <input class="phoneNumber" disabled />
        </div>
        <div class="addressInfoContainer">
          <span class="name">배송주소</span>
          <div>
            <input class="address" disabled />
            <button class="findAddress">우편번호 찾기</button>
            <br />
            <input class="address" disabled />
            <input class="address" disabled />
            <p class="shippingMemo">* 제주도, 도서 산간 지역 등은 배송이 하루 이상 추가 소요될 수 있습니다</p>
          </div>
        </div>
        <div class="orderInfoContainer">
          <span class="name">배송메모</span>
          <div class="orderMemoContainer">
            <p class="orderMemo">배송시 요청사항을 선택해주세요.</p>
            <div class="imgContainer" />
          </div>
        </div>
      </article>
      <article class="orderInfo">
        <h1>최종 결제 금액</h1>
        <div class="priceContainer">
          <div class="detailPrice">
            <span>총 상품 금액</span>
            <span>14,490원</span>
          </div>
          <div class="detailPrice">
            <span class="totalPrice">결제 예상 금액</span>
            <span class="totalPrice">
              <strong>14,490원</strong>
            </span>
          </div>
        </div>
      </article>
      <div class="paymentContainer">
        <button class="paymentBtn">결제하기</button>
      </div>
    </main>
  </div>
</template>

<script>
import { ip } from "../../../config.js";
import axios from "axios";
import { VueAgile } from "vue-agile";
import Header from "../Components/Header.vue";

export default {
  data() {
    return {};
  },
  components: { Header },
  methods: {},
};
</script>

<style lang="scss" scoped>
.orderContainer {
  margin: 0 320px;

  .orderTitle {
    width: 100%;
    margin: 60px 0 40px;
    text-align: center;
    font-size: 32px;
  }

  .orderSubTitle {
    font-size: 28px;
    font-weight: bold;
    padding-bottom: 24px;
    border-bottom: 1px solid black;
  }

  .category {
    height: 64px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 10px;
    border-bottom: 1px solid #dbdbdb;

    .categoryTitle {
      font-size: 18px;
      font-weight: bold;
    }

    .priceOrder {
      margin-right: 80px;
    }
  }

  .product {
    height: 120px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid black;

    .imgContainer {
      width: 90px;
      height: 90px;
      margin: 10px;

      img {
        width: 100%;
        height: 100%;
      }
    }

    .productInfoContainer {
      margin-left: 4px;
      display: flex;
      align-items: center;

      .optionContainer {
        margin-left: 20px;

        .option {
          margin-top: 10px;
          color: #929292;
        }
      }
    }

    .price {
      margin-right: 80px;
      font-weight: bold;
    }
  }

  .totalPrice {
    text-align: right;
    margin-top: 36px;
    font-size: 28px;
    font-weight: bold;

    strong {
      color: #ff204b;
    }
  }
}

.orderInfo {
  margin: 120px 320px 0;
  border-bottom: 1px solid black;

  h1 {
    font-size: 30px;
    padding-bottom: 20px;
    border-bottom: 1px solid black;
  }
  .deliveredContainer {
    border-bottom: 1px solid black;
    padding-bottom: 20px;
    font-size: 30px;
    display: flex;
    justify-content: space-between;

    .deliveredBtn {
      font-size: 26px;
      display: flex;
      align-items: center;

      .checkboxLable {
        cursor: pointer;

        .checkboxBtn {
          width: 20px;
          height: 20px;
          margin-right: 10px;
          cursor: pointer;
        }
      }
    }
  }

  .orderInfoContainer {
    height: 70px;
    border-bottom: 1px solid #929292;
    display: flex;
    align-items: center;

    .name {
      width: 250px;
      margin-left: 10px;
    }

    .nameInput {
      width: 500px;
      height: 45px;
      padding-left: 10px;
      border: none;
      outline: none;
      background-color: #f5f5f5;
    }

    .phoneNumber {
      width: 100px;
      height: 45px;
      padding: 0 10px;
      text-align: center;
      border: none;
      outline: none;
      background-color: #f5f5f5;
    }

    .email {
      width: 200px;
      height: 45px;
      padding: 0 10px;
      border: none;
      outline: none;
      background-color: #f5f5f5;
    }

    .memo {
      width: 700px;
      height: 45px;
      padding: 0 10px;
      border: none;
      outline: none;
      background-color: #f5f5f5;
    }

    .shippingMemo {
      text-align: center;
      width: 24px;
    }

    .orderMemoContainer {
      width: 700px;
      height: 45px;
      background-color: #f5f5f5;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;

      .orderMemo {
        margin-left: 10px;
        color: #929292;
      }

      .imgContainer {
        width: 14px;
        height: 7px;
        margin-right: 14px;
        background: url(/Images/arrow-down.png);
        background-size: 14px;

        img {
          width: 100%;
          height: 100%;
        }
      }
    }
  }

  .addressInfoContainer {
    border-bottom: 1px solid #929292;
    display: flex;
    align-items: center;

    .name {
      width: 250px;
      margin-left: 10px;
    }

    .address {
      width: 350px;
      height: 45px;
      margin-top: 10px;
      border: none;
      outline: none;
      background-color: #f5f5f5;
    }

    .findAddress {
      width: 120px;
      height: 40px;
      font-size: 16px;
      background-color: #4c4c4c;
      color: white;
      font-weight: bold;
      cursor: pointer;
    }

    p {
      margin: 16px 0;
      color: #929292;
    }
  }

  .priceContainer {
    padding: 24px;

    .detailPrice {
      display: flex;
      justify-content: space-between;
      padding: 12px 0;

      .totalPrice {
        font-size: 26px;
        font-weight: bold;

        strong {
          color: #ff204b;
        }
      }
    }
  }
}

.paymentContainer {
  margin: 60px 320px 0;
  display: flex;
  justify-content: center;

  .paymentBtn {
    width: 280px;
    height: 80px;
    font-size: 22px;
    background-color: black;
    color: white;
    margin-bottom: 60px;
    cursor: pointer;
  }
}
</style>
