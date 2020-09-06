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
            <div class="rowTitle">2020081300000005000</div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">주문 일시 :</div>
            <div class="rowTitle">2020-08-13 17:08:28</div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">총 결제 금액 :</div>
            <div class="rowTitle">22,120원</div>
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
            <div class="rowTitle">8202008130000501</div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">주문 상태 :</div>
            <div class="rowTitle">결제완료</div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">결제 일시 :</div>
            <div class="rowTitle">2020-08-13 17:08:28</div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">연락처 :</div>
            <div class="rowTitle">
              01088884444
              <v-btn class="redBtn" color="error" small>변경</v-btn>
            </div>
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
            <div>17289703(17312396)</div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">상품명 :</div>
            <div>[오늘출발] 루시 퍼프 플리츠 롱 원피스 3color_플렉스룸</div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">상품 판매가 :</div>
            <div class="rowTitle">
              28,000 원
              <strong class="redColor">(할인가 22,120원)</strong>
            </div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">옵션정보 :</div>
            <div class="rowTitle">바이올렛/FREE</div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">구매수량 :</div>
            <div class="rowTitle">1개</div>
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
            <div class="rowTitle">비회원</div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">수령자명:</div>
            <div class="rowTitle">박민정</div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">연락처 :</div>
            <div class="rowTitle">
              01088884444
              <div>
                <template>
                  <div class="text-center">
                    <v-dialog v-model="dialog" width="500">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn small color="red lighten-2" dark v-bind="attrs" v-on="on">변경</v-btn>
                      </template>

                      <v-card>
                        <v-card-title class="headline green lighten-2"></v-card-title>
                        <v-card-title class="headline white lighten-2">수취자 연락처1 변경</v-card-title>
                        <v-divider></v-divider>

                        <div class="phoneNumContainer">
                          <div>
                            <span>수취자 연락처1:</span>
                            <span>01088887777</span>
                          </div>
                          <div>
                            <span>변경할 핸드폰 번호:</span>
                            <span>
                              <v-text-field width="40" placeholder="전화번호"></v-text-field>
                            </span>
                          </div>
                        </div>

                        <v-divider></v-divider>

                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn color="success" dark @click="dialog = false">변경요청</v-btn>
                          <v-btn @click="dialog = false">취소</v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                  </div>
                </template>
              </div>
            </div>
          </div>
        </div>
        <div class="infoBorder" />
        <div class="orderInfoContent">
          <div class="infoRow">
            <div class="rowTitle">배송지 :</div>
            <div class="rowTitle">서울 강남구 테헤란로 32길 26 2층 브랜디 (06223)</div>
          </div>
          <div class="infoRow">
            <div class="rowTitle">배송시 요청사항 :</div>
            <div class="rowTitle">경비(관리실)에 맡겨주세요.</div>
            <v-btn small color="primary">배송지 변경</v-btn>
          </div>
        </div>
      </div>
      <div class="saveContainer">
        <v-btn color="success" class="saveBtn">저장</v-btn>
        <v-btn class="saveBtn">취소</v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";
import axios from "axios";
import { gonhoIp } from "../../../config";
import { VueDaumPostcode } from "vue-daum-postcode";

export default {
  created() {},
  data() {
    return {
      dialog: false,
    };
  },
  watch: {},
  methods: {},
  components: { VueDaumPostcode },
};
</script>

<style lang="scss">
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
