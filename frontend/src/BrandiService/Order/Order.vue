<template>
  <div>
    <main>
      <article class="orderContainer">
        <h1 class="orderTitle">주문하기</h1>
        <h2 class="orderSubTitle">브랜디 배송 상품</h2>
        <div class="category">
          <div class="categoryTitle">브랜디</div>
          <div class="priceOrder">주문금액</div>
        </div>
        <div class="product">
          <div class="productInfoContainer">
            <div class="imgContainer">
              <img :src="detailData.image_small" />
            </div>
            <div class="optionContainer">
              <h3>{{detailData.name}}</h3>
              <p class="option">{{detailData.color}}</p>
              <p class="option">{{detailData.quantity}}개</p>
            </div>
          </div>
          <div
            class="price"
          >{{Math.round((detailData.price -(detailData.price * (detailData.discount_rate / 100)))* detailData.quantity).toLocaleString(5)}}원</div>
        </div>
        <p class="totalPrice">
          총 주문금액
          <strong>{{Math.round((detailData.price -(detailData.price * (detailData.discount_rate / 100)))*detailData.quantity).toLocaleString(5)}}원</strong>
        </p>
      </article>
      <article class="orderInfo">
        <h1>주문자 정보</h1>
        <div class="orderInfoContainer">
          <span class="name">이름</span>
          <input class="nameInput" v-model="nameInput" ref="nameInput" placeholder="이름" />
        </div>
        <div class="orderInfoContainer">
          <span class="name">휴대폰</span>
          <input class="phoneNumber" v-model="orderPhoneFirst" ref="orderPhoneFirst" />
          <p>-</p>
          <input class="phoneNumber" v-model="orderPhoneSecond" ref="orderPhoneSecond" />
          <p>-</p>
          <input class="phoneNumber" v-model="orderPhoneThird" ref="orderPhoneThird" />
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
          <div class="text-center">
            <v-dialog v-model="dialog" width="500">
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="red lighten-2" ref="delivered" dark v-bind="attrs" v-on="on">입력하기</v-btn>
              </template>
              <v-card>
                <v-card-title class="headline black lighten-2"></v-card-title>
                <v-card-title class="headline white lighten-2">배송지 추가</v-card-title>
                <v-divider />
                <div class="addressContainer">
                  <div class="rowContainer">
                    <v-card-title>수령인</v-card-title>
                    <v-text-field
                      :counter="10"
                      ref="recipient"
                      label="수령인"
                      required
                      v-model="name"
                      maxlength="10"
                    />
                  </div>
                  <div class="rowContainer">
                    <v-card-title>휴대폰</v-card-title>
                    <input
                      class="phoneNumber"
                      type="tel"
                      maxlength="3"
                      placeholder="010"
                      ref="phoneNumFirst"
                      @keyup="onlyNumber"
                      v-model="phoneNumberFirst"
                    />
                    <input
                      class="phoneNumber"
                      type="tel"
                      maxlength="4"
                      @keyup="onlyNumber"
                      placeholder="0000"
                      ref="phoneNumSecond"
                      v-model="phoneNumberSecond"
                    />
                    <input
                      class="phoneNumber"
                      type="tel"
                      maxlength="4"
                      @keyup="onlyNumber"
                      placeholder="0000"
                      ref="phoneNumThird"
                      v-model="phoneNumberThird"
                    />
                  </div>
                  <div class="rowContainer">
                    <v-card-title>배송지</v-card-title>
                    <input
                      class="address"
                      style="text-align: left; padding-left: 10px"
                      type="text"
                      readonly
                      :value="sigunguCode"
                    />
                    <button @click="findAddressHandler" class="findAddress">우편번호 찾기</button>
                  </div>
                  <div class="daumContainer">
                    <vue-daum-postcode v-if="isDaumToggle" @complete="handleAddress" />
                  </div>
                  <div class="rowContainer">
                    <div class="addressSecond">{{ daumAddress }}</div>
                  </div>
                  <div class="rowContainer">
                    <input
                      class="addressThird"
                      type="text"
                      placeholder="상세 주소 입력를 입력하세요."
                      maxlength="20"
                      v-model="detailAddress"
                    />
                  </div>
                </div>
                <v-divider />
                <div class="AddContainer">
                  <v-card-actions>
                    <v-btn
                      width="100"
                      color="grey lighten-1"
                      dark
                      @click="(dialog = false), dialogCanceled()"
                    >취소</v-btn>
                    <v-btn
                      width="100"
                      color="black lighten-2"
                      dark
                      @click="deliveredCheckHandler"
                    >확인</v-btn>
                  </v-card-actions>
                </div>
              </v-card>
            </v-dialog>
          </div>
        </div>
        <div class="orderInfoContainer">
          <span class="name">이름</span>
          <input class="nameInput" placeholder="이름" disabled v-model="name" />
        </div>
        <div class="orderInfoContainer">
          <span class="name">휴대폰</span>
          <input class="phoneNumber" :value="phoneNumberFirst" disabled />
          <p>-</p>
          <input class="phoneNumber" :value="phoneNumberSecond" disabled />
          <p>-</p>
          <input class="phoneNumber" :value="phoneNumberThird" disabled />
        </div>
        <div class="addressInfoContainer">
          <span class="name">배송주소</span>
          <div>
            <input class="address" :value="sigunguCode" disabled />
            <br />
            <input class="address" :value="daumAddress" disabled />
            <input class="address" :value="detailAddress" disabled />
            <p class="shippingMemo">
              * 제주도, 도서 산간 지역 등은 배송이 하루 이상 추가 소요될 수
              있습니다
            </p>
          </div>
        </div>
        <div class="orderInfoContainer">
          <span class="name">배송메모</span>
          <div class="orderMemoBox">
            <div @click="toggleHandler" class="orderMemoContainer">
              <p class="orderMemo">{{ toggleData }}</p>
              <div class="imgContainer" />
            </div>
            <div class="directContainer" v-if="directInput === true">
              <input maxlength="50" placeholder="50자 이내로 작성해주세요." />
            </div>
            <div
              v-bind:class="{
                toggleContainer: isToggleDelivered,
                noneToggle: !isToggleDelivered,
              }"
            >
              <div class="orderChoice" @click="toggleDataHandler">배송시 요청사항을 선택해주세요.</div>
              <div class="orderChoice" @click="toggleDataHandler">문앞에 놓아주세요.</div>
              <div class="orderChoice" @click="toggleDataHandler">경비(관리)실에 맡겨주세요.</div>
              <div class="orderChoice" @click="toggleDataHandler">택배함에 넣어주세요.</div>
              <div class="orderChoice" @click="toggleDataHandler">직접 받겠습니다.</div>
              <div class="orderChoice" @click="toggleDataHandler">직접 입력</div>
            </div>
          </div>
        </div>
      </article>
      <article class="orderInfo">
        <h1>최종 결제 금액</h1>
        <div class="priceContainer">
          <div class="detailPrice">
            <span>총 상품 금액</span>
            <span>{{Math.round((detailData.price -(detailData.price * (detailData.discount_rate / 100)))*detailData.quantity).toLocaleString(5)}}원</span>
          </div>
          <div class="detailPrice">
            <span class="totalPrice">결제 예상 금액</span>
            <span class="totalPrice">
              <strong>{{Math.round((detailData.price -(detailData.price * (detailData.discount_rate / 100)))*detailData.quantity).toLocaleString(5)}}원</strong>
            </span>
          </div>
        </div>
      </article>
      <div class="paymentContainer">
        <button @click="paymentHandler" class="paymentBtn">결제하기</button>
      </div>
    </main>
  </div>
</template>

<script>
// import { ip } from "../../../config.js";
import axios from "axios";
import { VueAgile } from "vue-agile";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import { VueDaumPostcode } from "vue-daum-postcode";
import { gonhoIp } from "../../../config";

export default {
  created() {
    this.purchaseColor = localStorage.getItem("purchaseColor");
    this.purchaseSize = localStorage.getItem("purchaseSize");
    this.purchaseProductNumber = localStorage.getItem("purchaseProductNumber");
    this.purchaseId = localStorage.getItem("purchaseId");

    axios
      .get(
        `${gonhoIp}/order/checkout?product_id=${this.purchaseId}&color_id=${this.purchaseColor}&size_id=${this.purchaseSize}&quantity=${this.purchaseProductNumber}`
      )
      .then((res) => {
        this.detailData = res.data.data;
        this.daumAddress = this.detailData.address;
        this.detailAddress = this.detailData.additional_address;
        this.sigunguCode = this.detailData.zip_code;
        this.name = this.detailData.orderer_name;
        this.phoneNumberFirst = this.detailData.phone_number.substring(0, 3);
        this.phoneNumberSecond = this.detailData.phone_number.substring(3, 7);
        this.phoneNumberThird = this.detailData.phone_number.substring(7, 11);
      });
  },

  data() {
    return {
      isToggleDelivered: false,
      toggleData: "배송시 요청사항을 선택해주세요.",
      directInput: false,
      dialog: false,
      // isAddressAdd: false,
      isDaumToggle: false,
      daumAddress: "",
      sigunguCode: "",
      detailAddress: "",
      name: "",
      phoneNumberFirst: "",
      phoneNumberSecond: "",
      phoneNumberThird: "",
      purchaseColor: "",
      purchaseSize: "",
      purchaseProductNumber: "",
      purchaseId: "",
      detailData: [],
      orderPhoneFirst: "",
      orderPhoneSecond: "",
      orderPhoneThird: "",
      nameInput: "",
    };
  },
  components: { Header, Footer, VueDaumPostcode },
  methods: {
    //배송메모 토글 열고 닫기
    toggleHandler() {
      this.isToggleDelivered = !this.isToggleDelivered;
    },

    //배송지 입력 모달창에서 취소버튼 클릭시
    //모든 배송입력에 해당하는 State값 초기화하여 취소 적용
    dialogCanceled() {
      this.daumAddress = this.detailData.address;
      this.detailAddress = this.detailData.additional_address;
      this.sigunguCode = this.detailData.zip_code;
      this.name = this.detailData.orderer_name;
      this.phoneNumberFirst = this.detailData.phone_number.substring(0, 3);
      this.phoneNumberSecond = this.detailData.phone_number.substring(3, 7);
      this.phoneNumberThird = this.detailData.phone_number.substring(7, 11);
      this.isDaumToggle = false;
    },

    //클릭한 토글 데이터 보여주기
    //직접입력을 클릭한다면 인풋창 활성화
    toggleDataHandler(e) {
      if (e.target.innerText === "직접 입력") {
        this.toggleData = "";
        this.isToggleDelivered = !this.isToggleDelivered;
        this.directInput = true;
        return;
      }

      this.toggleData = e.target.innerText;
      this.isToggleDelivered = !this.isToggleDelivered;
      this.directInput = false;
    },

    //모달창의 열고닫는 상태값
    modalHandler() {
      this.isModalOn = !this.isModalOn;
    },

    //상세 주소 입력 활/비활성화
    // addAddressHandler() {
    //   this.isAddressAdd = !this.isAddressAdd;
    // },

    //다음 우편 정보 상태값 토글
    findAddressHandler() {
      this.isDaumToggle = !this.isDaumToggle;
    },

    //다음 API 사용한 주소 클릭시
    //주소와 우편에 해당하는 값을 저장하고,
    //다음 API 토글 닫기
    handleAddress(data) {
      this.daumAddress = data.address;
      this.sigunguCode = data.sigunguCode;
      this.isDaumToggle = false;
    },

    //number의 값이 아닌 텍스트가 들어가면
    //Input에 값이 들어가지 않게끔 구현
    onlyNumber() {
      this.phoneNumberFirst = this.phoneNumberFirst.replace(/[^0-9]/g, "");
      this.phoneNumberSecond = this.phoneNumberSecond.replace(/[^0-9]/g, "");
      this.phoneNumberThird = this.phoneNumberThird.replace(/[^0-9]/g, "");
    },

    deliveredCheckHandler() {
      if (!this.name) {
        alert("수령인을 입력해주세요.");
        this.$refs.recipient.focus();
        return;
      } else if (
        !this.phoneNumberFirst ||
        !this.phoneNumberSecond ||
        !this.phoneNumberThird
      ) {
        alert("휴대폰 번호를 입력해주세요.");
        !this.phoneNumberThird && this.$refs.phoneNumThird.focus();
        !this.phoneNumberSecond && this.$refs.phoneNumSecond.focus();
        !this.phoneNumberFirst && this.$refs.phoneNumFirst.focus();

        return;
      } else if (
        !this.detailAddress ||
        !this.sigunguCode ||
        !this.daumAddress
      ) {
        alert("배송지 정보를 입력해주세요.");
        return;
      }

      this.dialog = false;
    },
    paymentHandler() {
      if (!this.nameInput) {
        alert("이름을 입력해주세요.");
        this.$refs.nameInput.focus();
        return;
      }

      if (
        !this.orderPhoneFirst ||
        !this.orderPhoneSecond ||
        !this.orderPhoneThird
      ) {
        alert("핸드폰 번호를 입력해주세요.");
        this.$refs.orderPhoneThird.focus();
        this.$refs.orderPhoneSecond.focus();
        this.$refs.orderPhoneFirst.focus();
        return;
      }

      if (!this.name) {
        this.$refs.delivered.focus();
      }
    },
  },
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
      color: #1e88e5;
      cursor: pointer;
    }
  }

  .orderInfoContainer {
    border-bottom: 1px solid #929292;
    display: flex;
    align-items: center;

    .name {
      width: 250px;
      margin: 20px 10px 20px 0;
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
      margin: 10px 0;
      background-color: #f5f5f5;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;

      .orderMemo {
        margin: auto 0;
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

    .directContainer {
      margin-bottom: 10px;

      input {
        height: 40px;
        width: 100%;
        padding: 0 10px;
        background-color: #f5f5f5;
        border: none;
        outline: none;
      }
    }

    .orderMemoBox {
      position: relative;

      .noneToggle {
        display: none;
      }

      .toggleContainer,
      .noneToggle {
        background-color: white;
        border: 1px solid #dbdbdb;
        position: absolute;
        width: 100%;
        cursor: pointer;

        .orderChoice {
          padding: 10px;

          &:hover {
            color: white;
            background-color: #007fff;
          }
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
      text-align: left !important;
      padding-left: 10px;
      width: 350px;
      height: 45px;
      margin-top: 10px;
      padding-left: 10px;
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

.v-card {
  .cardCustomContainer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 200px;
    .v-card__text {
      text-align: center;
    }

    .orderImgContainer {
      width: 50px;
      height: 50px;

      img {
        width: 100%;
        height: 100%;
      }
    }
  }

  .addressContainer {
    .daumContainer {
      padding: 10px;
    }

    .rowContainer {
      margin-right: 15px;
      display: flex;
      align-items: center;

      .v-card__title {
        width: 100px;
      }

      .v-input {
        width: 50px;
      }

      .phoneNumber {
        text-align: center;
        width: 100px;
        height: 40px;
        margin-right: 5px;
        border: 1px solid #bdbdbd;
        border-radius: 5px;
      }

      .address {
        text-align: center;
        width: 250px;
        margin-right: 10px;
        height: 40px;
        border: 1px solid #bdbdbd;
        border-radius: 5px;
        outline: none;
      }

      .addressSecond {
        text-align: left;
        width: 100%;
        padding-top: 8px;
        padding-left: 10px;
        margin: 0 10px 10px 100px;
        height: 40px;
        border: 1px solid #bdbdbd;
        border-radius: 5px;
        outline: none;
      }

      .addressThird {
        width: 100%;
        margin: 0 10px 20px 100px;
        padding-left: 5px;
        height: 40px;
        border: 1px solid #bdbdbd;
        border-radius: 5px;
      }

      .findAddress {
        background-color: black;
        padding: 5px;
        border-radius: 5px;
        color: white;
      }
    }
  }
  .AddContainer {
    display: flex;
    justify-content: center;

    .addBtn {
      width: 200px;
      height: 50px;
      background-color: black;
      color: white;
      margin: 10px;
      border-radius: 5px;
    }
  }
}
</style>
