<template>
  <div class="productDetailContainer">
    <div class="orderTitle">
      <h1>주문 상세 관리</h1>
      <h2>주문 목록/관리</h2>
    </div>
    <div class="subTitle">주문관리 > 주문 상세 페이지</div>
    <div class="detailContainer">
      <div class="detailTitle">
        <h2>주문 상세</h2>
      </div>
      <div class="orderInfoContainer">
        <div class="infoTitle yellowInfo">
          <h3>> 주문 정보</h3>
        </div>
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">주문 번호 :</div>
            <div class="rowTitle">{{ detailData.order_no }}</div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">주문 일시 :</div>
            <div class="rowTitle">{{ detailData.order_time }}</div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">총 결제 금액 :</div>
<<<<<<< HEAD
            <div class="rowTitle">{{Math.round(detailData.total_price).toLocaleString(5) + "원"}}</div>
=======
            <div class="rowTitle">
              {{ detailData.total_price.toLocaleString(5) + "원" }}
            </div>
>>>>>>> master
          </div>
          <div class="infoRow">
            <div class="rowTitle">결제 정보 :</div>
            <div class="rowTitle">네이버페이(신용카드)</div>
          </div>
        </div>
      </div>
      <div class="orderInfoContainer">
        <div class="infoTitle">
          <h3 class="titleH">> 주문 상세 정보</h3>
        </div>
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">주문 상세 번호 :</div>
            <div class="rowTitle">{{ detailData.order_detail_no }}</div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">주문 상태 :</div>
            <div class="rowTitle">{{ detailData.order_status }}</div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">결제 일시 :</div>
            <div class="rowTitle">{{ detailData.paid_time }}</div>
          </div>
        </div>
      </div>
      <div class="orderInfoContainer">
        <div class="infoTitle">
          <h3 class="titleH">> 상품 정보</h3>
        </div>
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">상품 번호:</div>
            <div>{{ detailData.product_no }}</div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">상품명 :</div>
            <div>{{ detailData.product_name }}</div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">상품 판매가 :</div>
            <div class="rowTitle">
<<<<<<< HEAD
              {{parseInt(detailData.original_price).toLocaleString(5) + "원"}}
              <strong
                class="redColor"
              >(할인가 {{parseInt(detailData.sales_price).toLocaleString(5)}}원)</strong>
=======
              {{ detailData.price.toLocaleString(5) + "원" }}
              <strong class="redColor"
                >(할인가
                {{
                  (
                    Math.round(
                      (detailData.price -
                        detailData.price * (detailData.discount_rate / 100)) /
                        10
                    ) * 10
                  ).toLocaleString(5)
                }}원)</strong
              >
>>>>>>> master
            </div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">옵션정보 :</div>
            <div class="rowTitle">
              {{ detailData.color }}/{{ detailData.size }}
            </div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">구매수량 :</div>
            <div class="rowTitle">{{ detailData.quantity }} 개</div>
          </div>
        </div>
      </div>
      <div class="orderInfoContainer">
        <div class="infoTitle">
          <h3 class="titleH">> 수취자 정보</h3>
        </div>
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">회원번호 :</div>
            <div class="rowTitle">{{ detailData.user_no }}</div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">수령자명:</div>
            <div class="rowTitle">{{ detailData.orderer }}</div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">연락처 :</div>
            <div class="rowTitle">
              {{ recipientPhoneNum }}
              <template>
                <div class="text-center">
                  <v-dialog v-model="dialog" width="500">
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        small
                        color="red lighten-2"
                        dark
                        v-bind="attrs"
                        v-on="on"
                        >변경</v-btn
                      >
                    </template>
                    <v-card>
                      <v-card-title
                        class="headline green lighten-2"
                      ></v-card-title>
                      <v-card-title class="headline white lighten-2"
                        >수취자 연락처1 변경</v-card-title
                      >
                      <v-divider />
                      <div class="phoneNumContainer">
                        <div class="rowContainer">
                          <div class="category">수취자 연락처1:</div>
                          <div>{{ recipientPhoneNum }}</div>
                        </div>
                        <div class="rowContainer">
                          <div class="category">변경할 핸드폰 번호:</div>
                          <div>
                            <input
                              class="phoneNum"
                              maxlength="11"
                              ref="phoneNum"
                              v-model="onlyNumber"
                              placeholder="전화번호"
                            />
                          </div>
                        </div>
                      </div>
                      <v-divider />
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                          color="success"
                          dark
                          name="recipient"
                          @click="phoneNumHandler"
                          >변경요청</v-btn
                        >
                        <v-btn @click="cancelPhoneNumHandler">취소</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </div>
              </template>
            </div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">배송지 :</div>
            <div class="rowTitle">
              {{ `${daumAddress} ${detailAddress} (${sigunguCode})` }}
            </div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">배송시 요청사항 :</div>
            <div class="rowTitle">{{ detailData.delivery_request }}</div>
            <v-dialog v-model="shippingDialog" width="500">
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="primary" small dark v-bind="attrs" v-on="on"
                  >배송지 변경</v-btn
                >
              </template>
              <v-card>
                <v-card-title class="headline black lighten-2"></v-card-title>
                <v-card-title class="headline white lighten-2"
                  >배송지 변경</v-card-title
                >
                <v-divider />
                <div class="addressContainer">
                  <div class="rowContainer">
                    <v-card-title>배송지</v-card-title>
                    <input
                      class="address"
                      style="text-align: left; padding-left: 10px"
                      type="text"
                      readonly
                      :value="sigunguCode"
                    />
                    <button @click="findAddressHandler" class="findAddress">
                      우편번호 찾기
                    </button>
                  </div>
                  <div class="daumContainer">
                    <vue-daum-postcode
                      v-if="isDaumToggle"
                      @complete="handleAddress"
                    />
                  </div>
                  <div class="rowContainer">
                    <div class="addressSecond">{{ daumAddress }}</div>
                  </div>
                  <div class="rowContainer">
                    <input
                      class="addressThird"
                      type="text"
                      maxlength="30"
                      placeholder="상세 주소 입력를 입력하세요."
                      v-model="detailAddress"
                    />
                  </div>
                </div>
                <v-divider />
                <div class="addContainer">
                  <v-card-actions>
                    <v-btn
                      width="100"
                      color="grey lighten-1"
                      dark
                      @click="dialogCanceled"
                      >취소</v-btn
                    >
                    <v-btn
                      width="100"
                      color="black lighten-2"
                      dark
                      @click="deliveredCheckHandler"
                      >확인</v-btn
                    >
                  </v-card-actions>
                </div>
              </v-card>
            </v-dialog>
          </div>
        </div>
      </div>
      <div class="saveContainer">
        <v-btn @click="productDetailSaved" color="success" class="saveBtn"
          >저장</v-btn
        >
        <v-btn class="saveBtn">
          <router-link :to="`/admin/orderManagement`">취소</router-link>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";
import axios from "axios";
import { SERVER_IP } from "../../../config";
import { VueDaumPostcode } from "vue-daum-postcode";

export default {
  created() {
    this.axiosConnect();
  },
  data() {
    return {
      dialog: false,
      ordererDialog: false,
      onlyNumber: "",
      recipientPhoneNum: "",
      ordererPhoneNum: "",
      shippingDialog: false,
      detailAddress: "",
      daumAddress: "",
      sigunguCode: "",
      isDaumToggle: false,
      detailData: "",
    };
  },
  watch: {
    //숫자외에는 작성되지 않게 동작
    onlyNumber() {
      return (this.onlyNumber = this.onlyNumber.replace(/[^0-9]/g, ""));
    },
  },
  methods: {
    axiosConnect() {
      axios
        .get(`${SERVER_IP}/admin/order/detail/${this.$route.params.id}`)
        .then((res) => {
          this.detailData = res.data.data;
          this.recipientPhoneNum = this.detailData.phone_number;
          this.daumAddress = this.detailData.address;
          this.detailAddress = this.detailData.additional_address;
          this.sigunguCode = this.detailData.zip_code;
        });
    },

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

    //수취자 정보 > 연락처 수정
    phoneNumHandler(e) {
      if (!this.onlyNumber) {
        this.$refs.phoneNum.focus();
        return alert("번호를 입력해주세요.");
      }
      this.dialog = false;

      this.recipientPhoneNum = this.onlyNumber;
      this.onlyNumber = "";
    },

    //주문자 정보 > 연락처 수정
    orderPhoneNumHandler() {
      if (!this.onlyNumber) {
        return alert("번호를 입력해주세요.");
      }
      this.ordererDialog = false;

      this.ordererPhoneNum = this.onlyNumber;
      this.onlyNumber = "";
    },

    //핸드폰 번호 바꾸는 모달창 취소시 동작
    //모든값을 초기화시킨다.
    cancelPhoneNumHandler() {
      this.dialog = false;
      this.ordererDialog = false;
      this.onlyNumber = "";
    },

    dialogCanceled() {
      this.shippingDialog = false;
      this.daumAddress = this.detailData.address;
      this.detailAddress = this.detailData.additional_address;
      this.sigunguCode = this.detailData.zip_code;
    },

    deliveredCheckHandler() {
      if (!this.daumAddress || !this.sigunguCode) {
        return alert("배송지를 입력해주세요.");
      } else if (!this.detailAddress) {
        return alert("상세 주소를 입력해주세요.");
      }

      this.shippingDialog = false;
    },

    //데이터 전달
    productDetailSaved() {
      if (confirm("해당 주문건에 대한 수정내역을 저장하시겠습니까?") == true) {
        console.log(this.daumAddress);
        console.log(this.detailAddress);
        console.log(this.sigunguCode);
        console.log(this.recipientPhoneNum);
        axios
          .patch(`${SERVER_IP}/admin/user/shippingDetail`, {
            address: this.daumAddress,
            additionalAddress: this.detailAddress,
            zipCode: this.sigunguCode,
            userNo: this.detailData.user_no,
            phoneNumber: this.recipientPhoneNum,
          })
          .then((res) => {});
      } else {
        return false;
      }
    },
  },
  components: { VueDaumPostcode },
};
</script>

<style lang="scss">
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
      border: 0.5px solid #bdbdbd;
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

.addContainer {
  display: flex;
  justify-content: center;
}

.phoneNumContainer {
  padding: 10px 20px;

  .rowContainer {
    display: flex;
    width: 100%;
    margin-top: 20px;
    margin-bottom: 12px;

    .category {
      width: 30%;
      display: flex;
      align-items: center;
    }

    .phoneNum {
      border: 1px solid black;
      border-radius: 5px;
      background-color: white;
      padding: 4px 10px;
    }
  }
}

.productDetailContainer {
  background-color: #fafafa;

  .orderTitle {
    margin: 10px 20px;
    font-weight: 200;
    display: flex;
    align-items: center;

    h1 {
      font-size: 26px;
    }

    h2 {
      font-size: 16px;
      color: #888888;
    }
  }

  .subTitle {
    background-color: #eeeeee;
  }

  .detailContainer {
    margin: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;

    .detailTitle {
      background-color: #eeeeee;

      h2 {
        font-size: 18px;
        padding: 4px 8px;
      }
    }

    .orderInfoContainer {
      border: 1px solid #ddd;
      border-radius: 5px;
      margin: 10px;

      .infoTitle {
        padding: 4px 16px;
        background-color: #eee;

        h3 {
          font-size: 18px;
        }
      }

      .yellowInfo {
        background-color: cornsilk;
      }

      .infoBorder {
        width: 100%;
        height: 1px;
        border: 1px solid #ddd;
      }

      .orderInfoContent {
        width: 100%;
        display: flex;
        font-size: 14px;
        padding: 10px 20px;

        .infoRow {
          width: 50%;
          display: flex;

          .rowTitle {
            min-width: 250px;
            display: flex;
            align-items: center;

            .text-center {
              margin-left: 20px;
            }

            .redBtn {
              margin-left: 20px;
            }

            .redColor {
              color: red;
              font-weight: bold;
            }
          }
        }
      }
    }

    .saveContainer {
      display: flex;
      justify-content: center;
      margin: 20px;

      .saveBtn {
        margin: 0 10px;
      }
    }
  }
}
</style>
