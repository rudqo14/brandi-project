<template>
  <div class="productOneLineDescription">
    <div class="inputName">
      <div>한줄 상품 설명</div>
    </div>
    <div class="inputPlace">
      <v-text-field label="한줄 상품 설명을 입력해주세요." solo dense></v-text-field>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.productOneLineDescription {
  display: flex;
  height: 61px;
  border-bottom: 1px solid lightgray;

  .inputName {
    display: flex;
    align-items: center;
    width: 299px;
    height: 100%;
    padding-left: 15px;
    border-right: 1px solid lightgray;
    font-size: 15px;
  }

  .inputPlace {
    display: flex;
    width: 100%;
    padding: 10px;
  }
}
</style>
