<template>
  <div>
    <div class="menu homeMenu">
      <div class="MC homeContainer">
        <div class="iconBox">
          <i class="fas fa-home"></i>
        </div>
        <span>홈</span>
      </div>
      <div class="menuToggle homeToggle">
        <i class="fas fa-angle-left"></i>
        <!-- <i class="fas fa-angle-down"></i> -->
      </div>
    </div>
    <div class="menu statisticsMenu">
      <div class="MC statiscticsContainer">
        <div class="iconBox">
          <i class="far fa-chart-bar"></i>
        </div>
        <span>통계</span>
      </div>
      <div class="menuToggle homeToggle">
        <i class="fas fa-angle-left"></i>
      </div>
    </div>
    <div class="menu orderMenu">
      <div class="MC orderContainer">
        <div class="iconBox">
          <i class="fas fa-shopping-cart"></i>
        </div>
        <span>주문 관리</span>
      </div>
      <div class="menuToggle homeToggle">
        <i class="fas fa-angle-left"></i>
      </div>
    </div>
    <div class="menu productMenu">
      <div class="MC productContainer">
        <div class="iconBox">
          <i class="fas fa-shopping-bag"></i>
        </div>
        <span>상품 관리</span>
      </div>
      <div class="menuToggle homeToggle">
        <i class="fas fa-angle-left"></i>
      </div>
    </div>
    <div class="menu userMenu">
      <div class="MC userContainer">
        <div class="iconBox">
          <i class="fas fa-user"></i>
        </div>
        <span>회원 관리</span>
      </div>
      <div class="menuToggle homeToggle">
        <i class="fas fa-angle-left"></i>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 40px;
  padding: 0 15px;
  border-bottom: 1px solid #414247;

  .MC {
    display: flex;
  }

  .iconBox {
    width: 20px;
    margin-right: 5px;
  }
}
</style>