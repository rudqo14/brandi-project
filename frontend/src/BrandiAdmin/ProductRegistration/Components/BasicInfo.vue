<template>
  <div>
    <article class="basicInfo">
      <div class="title">
        <i class="fas fa-pencil-alt"></i>
        <span class="menuName">기본 정보</span>
      </div>
      <div class="row sellerSelect">
        <div class="inputName">
          <span>셀러선택</span>
          <span>*</span>
        </div>
        <div></div>
      </div>
      <div class="row salesStatus">
        <div class="inputName">
          <span>판매여부</span>
          <span>*</span>
        </div>
        <div></div>
      </div>
      <div class="row displayStatus">
        <div class="inputName">
          <span>진열여부</span>
          <span>*</span>
        </div>
        <div></div>
      </div>
      <div class="row category">
        <div class="inputName">
          <span>카테고리</span>
          <span>*</span>
        </div>
        <div></div>
      </div>
      <div class="row productName">
        <div class="inputName">
          <span>상품명</span>
          <span>*</span>
        </div>
        <div></div>
      </div>
      <div class="row productOneLineDescription">
        <div class="inputName">
          <span>한줄 상품 설명</span>
          <span>*</span>
        </div>
        <div></div>
      </div>
      <div class="row imageRegistration">
        <div class="inputName">
          <span>이미지 등록</span>
          <span>*</span>
        </div>
        <div></div>
      </div>
      <div class="row DetailProductDescription">
        <div class="inputName">
          <span>상세 상품 정보</span>
          <span>*</span>
        </div>
        <div></div>
      </div>
    </article>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.basicInfo {
  border: 1px solid lightgray;
  border-radius: 5px;

  .title {
    display: flex;
    align-items: center;
    background-color: lightgray;
    height: 38px;
    font-size: 16px;
    padding-left: 20px;

    .menuName {
      margin-left: 10px;
    }
  }

  .row {
    height: 55px;

    .inputName {
      width: 163px;
    }
  }
}
</style>