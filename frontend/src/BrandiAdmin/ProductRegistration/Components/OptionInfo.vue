<template>
  <div v-if="Object.keys(option).length">
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
                    <select
                      @change="selectColors"
                      v-for="list in colorSelectList"
                      :key="list"
                      class="colorSelect"
                    >
                      <option value="" selected
                        >색상 옵션을 선택해 주세요</option
                      >
                      <option
                        v-for="list in option.data.color"
                        :value="list.name"
                        :key="list.color_no"
                        >{{ list.name }}</option
                      >
                    </select>
                  </td>
                  <div class="colorButtonBox">
                    <td
                      v-for="list in colorSelectList"
                      :key="list"
                      :value="list"
                      class="colorAddDeleteBtn"
                    >
                      <button @click="colorSelectAdd">+</button>
                      <button
                        v-if="colorSelectList.length > 1"
                        :value="list"
                        @click="colorSelectDelete"
                      >
                        -
                      </button>
                    </td>
                  </div>
                </tr>
                <tr class="sizeOpt bodyTable">
                  <td class="optionCate">사이즈</td>
                  <td class="sizeSelectBOx">
                    <select
                      @change="selectSizes"
                      v-for="list in sizeSelectList"
                      :key="list"
                    >
                      <option value="">사이즈 옵션을 선택해 주세요</option>
                      <option
                        v-for="list in option.data.size"
                        :key="list.size_no"
                        :value="list.name"
                        >{{ list.name }}</option
                      >
                    </select>
                  </td>
                  <div class="sizeButtonBox">
                    <td
                      v-for="list in sizeSelectList"
                      :key="list"
                      :value="list"
                      class="sizeAddDeleteBtn"
                    >
                      <button @click="sizeSelectAdd">+</button>
                      <button
                        v-if="sizeSelectList.length > 1"
                        :value="list"
                        @click="sizeSelectDelete"
                      >
                        -
                      </button>
                    </td>
                  </div>
                </tr>
              </tbody>
              <tfoot>
                <tr class="footerTable">
                  <td class="optionCate">재고관리여부</td>
                  <td colspan="2">
                    <div class="radioContainer">
                      <v-radio-group v-model="stockQuantityDefaultValue" row>
                        <v-radio label="재고수량관리안함" :value="1"></v-radio>
                        <v-radio label="재고수량관리" :value="2"></v-radio>
                      </v-radio-group>
                    </div>
                  </td>
                </tr>
              </tfoot>
            </table>
            <div class="applyBtn">
              <v-btn @click="clickApply" color="primary" large>적용</v-btn>
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
              <tbody class="secondBody">
                <tr>
                  <td colspan="4">
                    옵션 정보를 입력 후 [적용] 버튼을 눌러주세요.
                  </td>
                </tr>
                <tr
                  v-if="applyOn"
                  v-for="(option, index) in applyOptionData"
                  :id="index"
                  :key="index"
                >
                  <td class="applySelectedColor">
                    <select name="" id="index"
                      ><option value="">{{ option.color }}</option></select
                    >
                  </td>
                  <td class="applySelectedSize">
                    <select name="" id=""
                      ><option value="">{{ option.size }}</option></select
                    >
                  </td>
                  <td>
                    <div class="radioContainer">
                      <v-radio-group v-model="defaultRadio" row>
                        <v-radio label="재고관리안함"></v-radio>
                        <v-radio value="1" label="재고관리"></v-radio>
                        <div class="stockInputContainer">
                          <input
                            @input="updateQuantity"
                            v-model="option.quantity"
                            class="stockQuantity"
                            type="text"
                          />
                          <span>개</span>
                        </div>
                      </v-radio-group>
                    </div>
                  </td>
                  <td>
                    <v-btn
                      @click="applyOption(index)"
                      class="mx-2"
                      fab
                      dark
                      small
                      color="error"
                    >
                      <v-icon dark>mdi-minus</v-icon>
                    </v-btn>
                  </td>
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
import { mapState, mapMutations } from "vuex";
import { ADMIN_API_URL } from "../../../../config";

const AdminStore = "adminStore";

export default {
  created() {
    this.getOptionData();
  },

  data() {
    return {
      optionDefaultValue: "기본옵션",
      stockQuantityDefaultValue: 1,
      defaultRadio: "1",
      stockManageRadio: "0",
      stockQuantity: "",
      colorListSize: 1,
      sizeListSize: 1,
      option: {},
      optionData: [{ color: [], size: [], quantity: [] }],
      updateOptionData: [{ color: [], size: [], quantity: [] }],
      applyOptionData: [],
      colorSelectList: [1],
      sizeSelectList: [1],
      applyOn: false,
    };
  },

  methods: {
    ...mapMutations(AdminStore, ["upDateAllOptions"]),
    getOptionData() {
      axios.get(`${ADMIN_API_URL}/admin/product/option`).then((res) => {
        this.option = res.data;
      });
    },

    colorSelectAdd() {
      this.colorListSize++;
      this.colorSelectList.push(this.colorListSize);
    },

    colorSelectDelete(e) {
      let colorSelectId = parseInt(e.target.value);
      const idx = this.colorSelectList.indexOf(colorSelectId);
      this.colorSelectList.splice(idx, 1);
    },

    sizeSelectAdd() {
      this.sizeListSize++;
      this.sizeSelectList.push(this.sizeListSize);
    },

    sizeSelectDelete(e) {
      let sizeSelectId = parseInt(e.target.value);
      const idx = this.sizeSelectList.indexOf(sizeSelectId);
      this.sizeSelectList.splice(idx, 1);
    },

    selectColors(e) {
      let colorName = e.target.value;
      this.optionData[0].color.splice(0, 1);
      this.optionData[0].color.push(colorName);
      this.updateOptionData[0].color.push(colorName);
    },

    selectSizes(e) {
      let sizeName = e.target.value;
      this.optionData[0].size.splice(0, 1);
      this.optionData[0].size.push(sizeName);
      this.updateOptionData[0].size.push(sizeName);
    },

    clickApply() {
      this.applyOptions();
      this.applyOn = true;
    },

    applyOptions() {
      for (let i = 0; i <= this.updateOptionData[0].color.length - 1; i++) {
        for (let j = 0; j <= this.updateOptionData[0].size.length - 1; j++) {
          this.applyOptionData.push({
            color: this.updateOptionData[0].color[i],
            size: this.updateOptionData[0].size[j],
            quantity: 0,
          });
        }
      }
    },

    applyOption(index) {
      this.applyOptionData.splice(index, 1);
    },

    updateQuantity() {
      this.upDateAllOptions(this.applyOptionData);
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
      height: inherit;
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
    border-bottom: 1px solid lightgray;

    .inputName {
      display: flex;
      align-items: center;
      width: 305px;
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

            .colorButtonBox,
            .sizeButtonBox {
              display: flex;
              flex-direction: column;
              justify-content: center;
              padding: 0 20px;

              .colorAddDeleteBtn,
              .sizeAddDeleteBtn {
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: white;
                border-radius: 3px;
                margin: 5px 0;
                height: 40px;
              }

              button {
                background-color: #eeeeee;
                border: 1px solid lightgray;
                border-radius: 3px;
                width: 30px;
                height: 30px;
                margin: 0 5px;
                text-align: center;
                vertical-align: middle;
                font-weight: bold;
                font-size: 20px;
                outline: none;
                color: black;
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

    .secondBody {
      .applySelectedColor,
      .applySelectedSize {
        padding: 0 15px;

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

      .radioContainer {
        margin-left: 20px;

        .stockQuantity:disabled {
          cursor: not-allowed;
          background-color: lightgray;
        }

        .stockInputContainer {
          margin-left: -10px;

          .stockQuantity {
            color: #333333;
            border: 1px solid #e5e5e5;
            font-size: 14px;
            padding: 5px;
            border-radius: 5px;
            margin-right: 10px;
            width: 100px;

            &:focus {
              border-color: #999;
            }
          }
        }
      }
    }
  }
}
</style>
