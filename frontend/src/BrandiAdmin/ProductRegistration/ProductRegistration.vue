<template>
  <div>
    <header>
      <div class="pageTitle">
        <span class="mainName">상품 등록</span>
        <span class="subName">상품 정보 등록</span>
      </div>
      <div class="pageStateBar">
        <i class="fas fa-home"></i>
        <span>상품 관리</span>
        <i class="fas fa-angle-right"></i>
        <span>상품 관리</span>
        <i class="fas fa-angle-right"></i>
        <span>상품 등록</span>
      </div>
    </header>
    <section class="pageContents">
      <BasicInfo />
      <OptionInfo />
      <SellingInfo />
    </section>
  </div>
</template>

<script>
import BasicInfo from "./Components/BasicInfo/BasicInfo";
import OptionInfo from "./Components/OptionInfo";
import SellingInfo from "./Components/SellingInfo";
export default {
  components: {
    BasicInfo,
    OptionInfo,
    SellingInfo,
  },
};
</script>

<style lang="scss" scoped>
header {
  width: 100%;
  .pageTitle {
    margin: 25px;

    .mainName {
      font-size: 30px;
      color: #666;
    }

    .subName {
      font-size: 14px;
      color: #888;
    }
  }

  .pageStateBar {
    display: flex;
    align-items: center;
    width: 100%;
    height: 40px;
    padding-left: 25px;
    font-size: 15px;
    background-color: #eeeeee;

    .fas {
      color: gray;
      padding: 0 8px;
    }
  }
}

.pageContents {
  margin: 10px 5px;
  background-color: #fafafa;
}
</style>