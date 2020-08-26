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
    <section>
      <BasicInfo />
      <OptionInfo />
      <SellingInfo />
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style>
header {
  width: 100%;
  height: 100px;

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
    width: 100%;
    background-color: lightgray;
    margin-left: 25px;
  }
}
</style>