<template>
  <div class="productName">
    <div class="inputName">
      <div>상품명</div>
      <div class="requiredMark">*</div>
    </div>
    <div class="inputPlace">
      <div class="inputBox">
        <input type="text" @input="inputProductName" />
      </div>
      <div class="alertText">
        <i class="fas fa-exclamation-triangle"></i> 상품명에는 쌍따옴표(") 또는
        홑따옴표(')를 포함할 수 없습니다.
      </div>
      <div class="alertText">
        <i class="fas fa-exclamation-triangle"></i> 상품명에는 4byte 이모지를
        포함할 수 없습니다.
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapState } from "vuex";

const AdminStore = "adminStore";

export default {
  data() {
    return {};
  },

  // 상품명 입력 값으로 상품명 state 를 변경해주는 메소드
  methods: {
    ...mapMutations(AdminStore, ["updateProductName"]),
    inputProductName(e) {
      this.updateProductName(e.target.value);
    },
  },
};
</script>

<style lang="scss" scoped>
.productName {
  display: flex;
  height: 100px;
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

    .inputBox {
      display: flex;
      align-items: center;
      background-color: #fff;
      box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2),
        0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12);
      margin-bottom: 10px;

      input {
        outline: none;
        width: 100%;
        margin-left: 10px;
      }
    }

    .alertText {
      color: #1e90ff;
      margin: 2px 0;
      font-size: 14px;
    }
  }
}
</style>
