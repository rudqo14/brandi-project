<template>
  <div>
    <article class="sellingInfo">
      <div class="sellingtitle">
        <i class="fas fa-pencil-alt fa-xs"></i>
        <span class="menuName">판매 정보</span>
      </div>
      <div class="sellingPrice">
        <div class="inputName">
          <div>판매가</div>
          <span class="requiredMark">*</span>
        </div>
        <div class="inputPlace">
          <div>
            <input @input="getInputPrice" placeholder="0" />
            <div class="price">원</div>
          </div>
          <div class="alertMessage">
            <i class="fas fa-exclamation-triangle"></i>
            <span
              >판매가는 원화기준 10원 이상이며 가격 입력 시 10원 단위로 입력해
              주세요.</span
            >
          </div>
        </div>
      </div>
      <div class="discountInfoInput">
        <div class="inputName">
          <div>할인 정보</div>
        </div>
        <div class="inputPlace">
          <div class="optionTable">
            <table>
              <tr>
                <td class="tableName">할인율</td>
                <td class="tableInput">할인가</td>
              </tr>
              <tr>
                <td class="tableName">
                  <div>
                    <input @input="getInputRate" placeholder="0" />
                    <div class="percent">%</div>
                  </div>
                </td>
                <td class="tableInput">
                  <div class="discountPrice">
                    <div class="priceContainer">
                      <div>{{ this.numberWithCommas(this.discountPrice) }}</div>
                      <button @click="getDiscountSellingPrice">
                        할인판매가적용
                      </button>
                    </div>
                    <div>원</div>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="tableName">할인판매가</td>
                <td class="tableInput">
                  <div class="discountSellingPrice">
                    <div>
                      {{ this.numberWithCommas(this.discountSellingPrice) }}
                    </div>
                    <span>원</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="tableName">
                  <div class="discountPeriod">할인기간</div>
                </td>
                <td class="tableInput">
                  <div class="discountPeriod">
                    <div>
                      <input
                        type="radio"
                        value="1"
                        name="discountPeriod"
                        v-model="discountPeriodRadio"
                      />
                      <label>무기한</label>
                    </div>
                    <div>
                      <input
                        type="radio"
                        value="2"
                        name="discountPeriod"
                        v-model="discountPeriodRadio"
                      />
                      <label>기간설정</label>
                    </div>
                  </div>
                  <div v-if="this.discountPeriodRadio === '2'">
                    <a-range-picker
                      :show-time="{ format: 'HH:mm' }"
                      format="YYYY-MM-DD HH:mm"
                      :placeholder="['클릭해주세요', '클릭해주세요']"
                      @change="onChange"
                    />
                    <div class="periodInfo">
                      <div>
                        * 할인기간을 설정시 기간만료되면 자동으로 정상가로 변경
                        됩니다.
                      </div>
                      <div>
                        * 할인기간을 설정시 시작일과 종료일은 필수입니다.
                      </div>
                    </div>
                  </div>
                </td>
              </tr>
            </table>

            <div class="alertMessage">
              <div>
                <i class="fas fa-exclamation-triangle"></i>
                <span>할인판매가 = 판매가 * 할인률</span>
              </div>
              <div>
                <i class="fas fa-exclamation-triangle"></i>
                <span
                  >할인 판매가 적용 버튼을 클릭 하시면 판매가 정보가 자동
                  계산되어집니다.</span
                >
              </div>
              <div>
                <i class="fas fa-exclamation-triangle"></i>
                <span
                  >할인 판매가는 원화기준 10원 단위로 자동 반올림됩니다.</span
                >
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="minQuantity">
        <div class="inputName">
          <div>최소판매수량</div>
        </div>
        <div class="inputPlace">
          <div>
            <div>
              <div class="inputContainer">
                <input
                  v-model="minQuantityRadio"
                  type="radio"
                  value="1"
                  name="minQuantity"
                />
                <label>1개 이상</label>
              </div>
              <div class="inputContainer">
                <input
                  v-model="minQuantityRadio"
                  type="radio"
                  value="inputQuantity"
                  name="minQuantity"
                />
                <label
                  ><input
                    v-model="inputMin"
                    class="quantity"
                    :disabled="this.minQuantityRadio === '1'"
                    @input="getMinQuantity"
                    @keypress="numberHandler"
                  />
                  <span>개 이상</span>
                  <span class="alertMessage"
                    >(20개를 초과하여 설정하실 수 없습니다)</span
                  >
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="maxQuantity">
        <div class="inputName">
          <div>최대판매수량</div>
        </div>
        <div class="inputPlace">
          <div id="maxQuantity">
            <div>
              <div class="inputContainer">
                <input
                  v-model="maxQuantityRadio"
                  type="radio"
                  value="20"
                  name="maxQuantity"
                  checked
                />
                <label>20개</label>
              </div>
              <div class="inputContainer">
                <input
                  v-model="maxQuantityRadio"
                  type="radio"
                  value="inputQuantity"
                  name="maxQuantity"
                />
                <label
                  ><input
                    v-model="inputMax"
                    class="quantity"
                    :disabled="this.maxQuantityRadio === '20'"
                    @input="getMaxQuantity"
                    @keypress="numberHandler"
                  />
                  <span>개 이하</span>
                  <span class="alertMessage"
                    >(20개를 초과하여 설정하실 수 없습니다)</span
                  >
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
import { mapMutations, mapGetters } from "vuex";

const AdminStore = "adminStore";

export default {
  data() {
    return {
      inputMax: "",
      inputMin: "",
      discountPeriodRadio: "1",
      minQuantityRadio: "1",
      maxQuantityRadio: "20",
      selectDiscountPeriod: 0,
      discountSellingPrice: 0,
      discountSellingPricd: 0,
      discountPrice: 0,
    };
  },
  methods: {
    ...mapMutations(AdminStore, [
      "insertSellingPrice",
      "insertDiscountRate",
      "insertDiscountPeriod",
      "insertMinQuantity",
      "insertMaxQuantity",
    ]),

    getDiscountSellingPrice() {
      const price = this.getPrice;
      if (price === 0) {
        alert("할인 적용 전에 판매가 입력이 필수입니다");
      } else {
        const discountRate = this.getDiscountRate;
        if (discountRate < 0 || discountRate > 99) {
          alert(
            "올바른 할인율을 입력해주세요 \n할인율 범위는 0~99 까지 가능합니다."
          );
        } else {
          const discountPrice = price * (discountRate / 100);
          this.discountSellingPrice =
            Math.round((price - discountPrice) / 10) * 10;
          this.discountPrice = Math.floor(discountPrice);
        }
      }
    },
    numberWithCommas(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    onChange(value, dateString) {
      this.insertDiscountPeriod(dateString);
    },
    getInputPrice(e) {
      this.insertSellingPrice(e.target.value);
    },
    getInputRate(e) {
      this.insertDiscountRate(e.target.value);
    },
    getMinQuantity(e) {
      this.insertMinQuantity(e.target.value);
    },
    getMaxQuantity(e) {
      this.insertMaxQuantity(e.target.value);
    },
    numberHandler(e) {
      if (e.keyCode < 48 || e.keyCode > 57) {
        e.preventDefault();
      }
    },
  },
  watch: {
    minQuantityRadio: {
      handler: function(value, oldvalue) {
        if (value === "1") {
          this.insertMinQuantity(1);
          this.inputMin = "";
        }
      },
      deep: true,
    },
    maxQuantityRadio: {
      handler: function(value, oldvalue) {
        if (value === "20") {
          this.insertMaxQuantity(20);
          this.inputMax = "";
        }
      },
      deep: true,
    },
    discountPeriodRadio: {
      handler: function(value, oldvalue) {
        this.insertDiscountPeriod(null);
      },
      deep: true,
    },
  },
  computed: {
    ...mapGetters(AdminStore, ["getPrice", "getDiscountRate"]),
  },
};
</script>

<style lang="scss" scoped>
.inputName {
  display: flex;
  align-items: center;
  width: 298px;
  height: 100%;
  padding-left: 15px;
  border-right: 1px solid lightgray;
  font-size: 13px;

  .requiredMark {
    margin-left: 0px;
    color: red;
  }
}

.inputPlace {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  margin-left: 10px;

  input {
    border: 1px solid lightgray;
    height: 35px;
  }
}

.sellingInfo {
  margin-top: 30px;
  border: 1px solid lightgray;
  border-radius: 5px;

  .alertMessage {
    font-size: 12.5px;
    color: #1e90ff;

    i {
      margin-right: 10px;
      width: 5px;
    }
  }

  .sellingtitle {
    display: flex;
    align-items: center;
    background-color: lightgray;
    height: 38px;
    font-size: 16px;
    padding-left: 15px;

    span {
      margin-bottom: 5px;
    }

    i {
      margin-right: 5px;
      color: rgb(85, 85, 85);
    }
  }

  .sellingPrice {
    display: flex;
    height: 70px;
    border-bottom: 1px solid lightgray;

    .inputPlace {
      .alertMessage {
        align-items: center;
        font-size: 12.5px;
        color: #1e90ff;

        i {
          margin-right: 10px;
          width: 5px;
        }
      }
      div {
        display: flex;

        input {
          padding-left: 10px;
          width: 200px;
        }

        .price {
          padding: 7px 13px;
          width: 40px;
          background-color: lightgray;
          border-top-right-radius: 5px;
          border-bottom-right-radius: 5px;
        }
      }
    }
  }

  .discountInfoInput {
    display: flex;
    height: 380px;
    border-bottom: 1px solid lightgray;

    table,
    tr,
    td {
      height: 35px;
      color: black;
      font-size: 13px;
      border: 1px solid lightgray;
    }

    .optionTable {
      table {
        margin-bottom: 20px;
      }
      .tableName {
        width: 450px;
        padding: 7px;

        div {
          display: flex;

          input {
            width: 80px;
            height: 35px;
            border-top-left-radius: 5px;
            border-bottom-left-radius: 5px;
            padding: 10px;
          }

          .percent {
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
            padding: 7px 10px;
            height: 35px;
            width: 35px;
            background-color: lightgray;
          }

          .discountPeriod {
            margin-bottom: 10px;
          }
        }
      }

      .tableInput {
        width: 200px;
        padding: 7px;

        .periodInfo {
          color: red;
          margin-top: 15px;
        }

        .discountPeriod {
          display: flex;
          margin-right: 15px;
          align-items: center;

          div {
            margin-right: 20px;
            display: flex;

            input {
              height: 20px;
              margin-right: 5px;
            }
          }
          label {
            display: flex;
            align-items: center;

            input {
              height: 15px;
              margin: 0 5px;
            }

            span {
              font-size: 15px;
            }
          }
        }

        .discountPrice {
          display: flex;
          .priceContainer {
            margin: 0 10px;
          }
          button {
            font-weight: bold;
            border-radius: 5px;
            padding: 10px;
            background-color: #428bca;
            color: white;
          }
        }

        .discountSellingPrice {
          margin: 0 10px;
          display: flex;

          div {
            width: 115px;
          }
        }
      }
    }
  }

  .minQuantity {
    display: flex;
    height: 70px;
    border-bottom: 1px solid lightgray;

    .inputPlace {
      div {
        display: flex;
        font-size: 17px;
        align-items: center;

        input {
          font-size: 14px;
          padding: 5px;
          border-radius: 5px;
          margin-right: 10px;
          width: 100px;
        }

        input:disabled {
          background: lightgray;
        }

        input[type="radio"] {
          height: 25px;
          width: 15px;
        }

        label {
          display: flex;
          align-items: center;
        }

        .inputContainer {
          margin-right: 30px;
        }
      }
    }
  }

  .maxQuantity {
    display: flex;
    height: 70px;
    border-bottom: 1px solid lightgray;

    .inputPlace {
      div {
        font-size: 17px;
        display: flex;
        align-items: center;

        input {
          font-size: 14px;
          padding: 5px;
          width: 100px;
          margin-right: 10px;
          border-radius: 5px;
        }

        input:disabled {
          background: lightgray;
        }

        input[type="radio"] {
          height: 15px;
          width: 15px;
        }

        label {
          display: flex;
          align-items: center;
        }
      }

      .inputContainer {
        margin-right: 30px;
      }
    }
  }
}
</style>
