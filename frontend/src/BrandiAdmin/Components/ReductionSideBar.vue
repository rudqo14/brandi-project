<template>
  <div class="ReductionSideMenu">
    <div class="menu homeMenu">
      <i class="fas fa-home"></i>
    </div>
    <div class="menu statisticsMenu">
      <i class="far fa-chart-bar"></i>
    </div>
    <div class="menu orderMenu">
      <i class="fas fa-shopping-cart"></i>
    </div>
    <div class="menu productMenu">
      <i class="fas fa-shopping-bag"></i>
    </div>
    <div class="menu userMenu">
      <i class="fas fa-user"></i>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.ReductionSideMenu {
  .menu {
    display: flex;
    align-items: center;
    cursor: pointer;
    width: 45px;
    height: 40px;
    padding: 0 15px;
    border-bottom: 1px solid #414247;
    &:hover {
      background-color: #2b2b30;
    }
  }
}
</style>