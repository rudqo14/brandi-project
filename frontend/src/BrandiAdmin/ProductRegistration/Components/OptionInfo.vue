<template>
  <div>
    <article class="optionInfo">
      <div class="title">
        <i class="fas fa-pencil-alt"></i>
        <span class="menuName">옵션 정보</span>
      </div>
      <div class="optionSetting">
        <div class="inputName">
          <div>옵션 설정</div>
          <div class="requiredMark">*</div>
        </div>
        <div class="inputPlace">
          <div class="radioContainer">
            <v-radio-group v-model="optionDefaultValue" row>
              <v-radio label="기본옵션" value="기본옵션"></v-radio>
            </v-radio-group>
          </div>
        </div>
      </div>
      <div class="optionInfoInput">
        <div class="inputName">
          <div>옵션 정보</div>
        </div>
        <div class="inputPlace">
          <div class="optionTable">
            <table class="firstOption">
              <thead>
                <tr class="headTable">
                  <td class="header optionItem">옵션항목</td>
                  <td class="header">상품옵션명</td>
                  <td class="header optionValue">옵션값 추가/삭제</td>
                </tr>
              </thead>
              <tbody>
                <tr class="colorOpt bodyTable">
                  <td class="optionCate">색상</td>
                  <td class="colorSelectBox">
                    <select class="colorSelect"
                      >색상 옵션을 선택해 주세요
                      <option value="" selected
                        >색상 옵션을 선택해 주세요</option
                      >
                      <option
                        v-for="list in option.data.color"
                        :value="list.color_no"
                        :key="list.color_no"
                        >{{ list.name }}</option
                      >
                    </select>
                    <select class="colorSelect"
                      >색상 옵션을 선택해 주세요
                      <option value="" selected
                        >색상 옵션을 선택해 주세요</option
                      >
                      <option
                        v-for="list in option.data.color"
                        :value="list.color_no"
                        :key="list.color_no"
                        >{{ list.name }}</option
                      >
                    </select>
                    <select class="colorSelect"
                      >색상 옵션을 선택해 주세요
                      <option value="" selected
                        >색상 옵션을 선택해 주세요</option
                      >
                      <option
                        v-for="list in option.data.color"
                        :value="list.color_no"
                        :key="list.color_no"
                        >{{ list.name }}</option
                      >
                    </select>
                    <select class="colorSelect"
                      >색상 옵션을 선택해 주세요
                      <option value="" selected
                        >색상 옵션을 선택해 주세요</option
                      >
                      <option
                        v-for="list in option.data.color"
                        :value="list.color_no"
                        :key="list.color_no"
                        >{{ list.name }}</option
                      >
                    </select>
                  </td>
                  <div class="buttonBox">
                    <td class="colorAddDeleteBtn">
                      <button>+</button>
                      <button>-</button>
                    </td>
                    <td class="colorAddDeleteBtn">
                      <button>+</button>
                      <button>-</button>
                    </td>
                    <td class="colorAddDeleteBtn">
                      <button>+</button>
                      <button>-</button>
                    </td>
                    <td class="colorAddDeleteBtn">
                      <button>+</button>
                      <button>-</button>
                    </td>
                  </div>
                </tr>
                <tr class="sizeOpt bodyTable">
                  <td class="optionCate">사이즈</td>
                  <td class="sizeSelectBOx">
                    <select>
                      <option value="">사이즈 옵션을 선택해 주세요</option>
                      <option
                        v-for="list in option.data.size"
                        :key="list.size_no"
                        :value="list.size_no"
                        >{{ list.name }}</option
                      >
                    </select>
                  </td>
                  <td class="addDeleteBtn">
                    <button>+</button>
                    <button>-</button>
                  </td>
                </tr>
              </tbody>
              <tfoot>
                <tr class="footerTable">
                  <td class="optionCate">재고관리여부</td>
                  <td colspan="2">
                    <div class="radioContainer">
                      <v-radio-group v-model="stockDefaultValue" row>
                        <v-radio label="재고수량관리안함" :value="1"></v-radio>
                        <v-radio label="재고수량관리" :value="2"></v-radio>
                      </v-radio-group>
                    </div>
                  </td>
                </tr>
              </tfoot>
            </table>
            <div class="applyBtn" @click="data">
              <v-btn color="primary" large>적용</v-btn>
            </div>
            <table class="secondOption">
              <thead class="secondHeading">
                <tr>
                  <td class="pdOptionInfo" colspan="2">상품옵션정보</td>
                  <td class="normalStock" rowspan="2">일반재고</td>
                  <td class="deleteSpace" rowspan="2"></td>
                </tr>
                <tr>
                  <td class="color" rowspan="1">색상</td>
                  <td class="size" rowspan="1">사이즈</td>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td colspan="4">
                    옵션 정보를 입력 후 [적용] 버튼을 눌러주세요.
                  </td>
                </tr>
                <tr>
                  <td class="selectedColor">
                    <v-select :items="option" label="" dense solo></v-select>
                  </td>
                  <td class="selectedSize">
                    <v-select :items="option" label="" dense solo></v-select>
                  </td>
                  <td>
                    <div class="radioContainer">
                      <v-radio-group v-model="stockDefaultValue" row>
                        <v-radio label="재고수량관리안함" :value="1"></v-radio>
                        <v-radio label="재고수량관리" :value="2"></v-radio>
                      </v-radio-group>
                    </div>
                  </td>
                  <td>삭제</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
import axios from "axios";
import { ADMIN_API_URL } from "../../../../config";

export default {
  created() {
    this.getOptionData();
  },

  mounted() {},

  data() {
    return {
      optionDefaultValue: "기본옵션",
      stockDefaultValue: 1,
      option: {},
    };
  },

  methods: {
    getOptionData() {
      axios.get(`${ADMIN_API_URL}/admin/product/option`).then((res) => {
        this.option = res.data;
      });
    },
    data() {
      console.log("option: ", this.option.data.color);
    },
  },
};
</script>

<style lang="scss" scoped>
.optionInfo {
  margin-top: 30px;
  border: 1px solid lightgray;
  border-radius: 5px;

  .title {
    display: flex;
    align-items: center;
    background-color: lightgray;
    height: 38px;
    font-size: 18px;
    padding-left: 15px;
  }

  .optionSetting {
    display: flex;
    height: 50px;
    border-bottom: 1px solid lightgray;

    .inputName {
      display: flex;
      align-items: center;
      width: 300px;
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
      justify-content: center;
      width: 100%;
      margin-left: 10px;

      .radioContainer {
        display: flex;
        font-size: 16px;

        .v-input {
          font-size: 10px;
          margin: 0;
          height: 30px;
        }
      }

      .alertText {
        color: #1e90ff;
        font-size: 14px;
        margin-left: 4px;
      }
    }
  }

  .optionInfoInput {
    display: flex;
    height: 800px;
    border-bottom: 1px solid lightgray;

    .inputName {
      display: flex;
      align-items: center;
      width: 305px;
      height: 100%;
      padding-left: 15px;
      border-right: 1px solid lightgray;
      font-size: 15px;
    }

    .inputPlace {
      width: 100%;
      margin: 20px;

      .optionTable {
        table,
        td,
        tr {
          border: 1px solid lightgray;
          border-collapse: collapse;
          text-align: center;
          vertical-align: middle;
        }

        table {
          width: 100%;
        }

        .firstOption {
          .colorOpt {
          }

          .bodyTable {
            height: 60px;

            .buttonBox {
              display: flex;
              flex-direction: column;
              padding: 0 20px;

              .colorAddDeleteBtn {
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: white;
                border-radius: 3px;
                margin: 5px 0;
                height: 40px;
              }

              button {
                background-color: whitesmoke;
                border: 1px solid lightgray;
                width: 30px;
                height: 30px;
                text-align: center;
                vertical-align: middle;
                font-weight: bold;
                font-size: 20px;
                outline: none;
                &:hover {
                  background-color: lightgray;
                }
              }
            }

            .colorSelectBox,
            .sizeSelectBox {
              padding: 0 20px;

              select {
                outline: none;
                appearance: menulist-button;
                background-color: white;
                border: 1px solid lightgray;
                margin: 5px 0;
                border-radius: 3px;
                width: 100%;
                height: 40px;
              }
            }
          }

          .headTable,
          .footerTable {
            height: 50px;
            background-color: #eee;

            .radioContainer {
              display: flex;
              align-items: center;
              margin-left: 20px;
              height: 50px;
            }

            .header {
              font-size: 18px;
              font-weight: bold;
              background-color: #eee;
            }

            .optionItem,
            .optionValue {
              width: 20%;
            }
          }
        }
      }
    }
  }

  .applyBtn {
    margin: 15px 0;
    width: 150px;

    .v-btn {
      width: 100%;
    }
  }

  .secondOption {
    td {
      height: 50px;
    }
    .secondHeading {
      background-color: #eee;
      .pdOptionInfo,
      .normalStock {
        width: 45%;
      }
      .deleteSpace {
        width: 5%;
      }

      .color,
      .size {
        width: 25%;
      }
    }
  }
}
</style>
