<template>
  <div>
    <div class="sellerSelect">
      <div class="inputName">
        <div>셀러선택</div>
        <div class="requiredMark">*</div>
      </div>
      <div class="inputPlace">
        <div class="searchWrapper">
          <span>셀러검색을 해주세요</span>
        </div>
        <div class="sellerSelectBtn">
          <v-btn color="success" dark depressed normal>셀러검색</v-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.sellerSelect {
  display: flex;
  height: 55px;
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
    align-items: center;
    width: 100%;
    margin-left: 10px;

    .searchWrapper {
      display: flex;
      align-items: center;
      background-color: #f5f5f5;
      padding: 0 10px;
      margin-right: 15px;
      width: 313px;
      height: 36px;
      font-size: 15px;
      cursor: not-allowed;
    }
  }
}
</style>
