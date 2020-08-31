<template>
  <div class="productOneLineDescription">
    <div class="inputName">
      <div>한줄 상품 설명</div>
    </div>
    <div class="inputPlace">
      <input
        :value="simpleDescription"
        @input="inputSimpleDescription"
        label="한줄 상품 설명을 입력해주세요."
        solo
        dense
      ></input>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  computed: {
    ...mapState({
      simpleDescription: (state) => state.simpleDescription,
    }),
  },
  methods: {
    ...mapMutations(["updateSimpleDescription"]),
    inputSimpleDescription(e) {
      this.$store.commit("updateSimpleDescription", e.target.value);
    },
  },
};
</script>

<style lang="scss" scoped>
.productOneLineDescription {
  display: flex;
  height: 61px;
  border-bottom: 1px solid lightgray;

  .inputName {
    display: flex;
    align-items: center;
    width: 303px;
    height: 100%;
    padding-left: 15px;
    border-right: 1px solid lightgray;
    font-size: 15px;
  }

  .inputPlace {
    display: flex;
    width: 100%;
    padding: 10px;
    margin: 10px;
    background-color: #fff;
    box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2),
      0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12);

    input {
      outline: none;
      width: 100%;
      margin-left: 10px;
    }
  }
}
</style>
