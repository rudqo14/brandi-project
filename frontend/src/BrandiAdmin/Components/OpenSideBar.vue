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
    <div class="menu statisticsMenu" @click="statisticsToggleHandler">
      <div class="MC statiscticsContainer">
        <div class="iconBox">
          <i class="far fa-chart-bar"></i>
        </div>
        <span>통계</span>
      </div>
      <div
        :class="{statiscticsToggle: !statisticsToggle, statiscticsToggleChage: statisticsToggle}"
      >
        <i class="fas fa-angle-left"></i>
      </div>
    </div>
    <ul
      :class="{statiscticsMenuList: statisticsToggle, statiscticsMenuListOpen: !statisticsToggle}"
    >
      <li>시간단위분석</li>
    </ul>

    <div class="menu orderMenu" @click="orderToggleHandler">
      <div class="MC orderContainer">
        <div class="iconBox">
          <i class="fas fa-shopping-cart"></i>
        </div>
        <span>주문 관리</span>
      </div>
      <div :class="{orderToggle: !orderToggle, orderToggleChage: orderToggle}">
        <i class="fas fa-angle-left"></i>
      </div>
    </div>
    <ul :class="{orderMenuList: orderToggle, orderMenuListOpen: !orderToggle}">
      <li>결제완료관리</li>
    </ul>
    <div class="menu productMenu" @click="productToggleHandler">
      <div class="MC productContainer">
        <div class="iconBox">
          <i class="fas fa-shopping-bag"></i>
        </div>
        <span>상품 관리</span>
      </div>
      <div :class="{productToggle: !productToggle, productToggleChange: productToggle}">
        <i class="fas fa-angle-left"></i>
      </div>
    </div>
    <ul :class="{productrMenuList: productToggle, productrMenuListOpen: !productToggle}">
      <li>상품 관리</li>
      <li>상품 등록</li>
    </ul>
    <div class="menu userMenu" @click="userToggleHandler">
      <div class="MC userContainer">
        <div class="iconBox">
          <i class="fas fa-user"></i>
        </div>
        <span>회원 관리</span>
      </div>
      <div :class="{userToggle: !userToggle, userToggleChange: userToggle}">
        <i class="fas fa-angle-left"></i>
      </div>
    </div>
    <ul :class="{userMenuList: userToggle, userMenuListOpen: !userToggle}">
      <li>회원 관리_커뮤니티</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      statisticsToggle: false,
      orderToggle: false,
      productToggle: false,
      userToggle: false,
    };
  },

  methods: {
    statisticsToggleHandler() {
      this.statisticsToggle = !this.statisticsToggle;
    },
    orderToggleHandler() {
      this.orderToggle = !this.orderToggle;
    },
    productToggleHandler() {
      this.productToggle = !this.productToggle;
    },
    userToggleHandler() {
      this.userToggle = !this.userToggle;
    },
  },
};
</script>

<style lang="scss" scoped>
.menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  height: 40px;
  padding: 0 15px;
  border-bottom: 1px solid #414247;
  &:hover {
    background-color: #2b2b30;
  }

  .MC {
    display: flex;
  }

  .iconBox {
    width: 20px;
    margin-right: 5px;
  }

  .statiscticsToggleChage,
  .orderToggleChage,
  .productToggleChange,
  .userToggleChange {
    transform: rotate(-90deg);
  }
}

.statiscticsMenuList,
.orderMenuList,
.productrMenuList,
.userMenuList {
  margin: 8px 0;
  /* transition: transform 0.3s ease-out;
  transform: scaleY(1);
  transform-origin: top;
  transform:scaleY(0) */
  // 어드민 사이드바 토글 애니메이션
  animation: 0.4s menuOpen ease-out forwards;
  @keyframes menuOpen {
    0% {
      transform: translatey(-10%);
    }
    100% {
      transform: translatey(0);
    }
  }

  li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #414247;
    cursor: pointer;
    height: 40px;
    padding: 0 18px;
    &:hover {
      background: #414247 !important;
    }

    // 어드민 사이드바 토글 애니메이션
    /* animation: 200ms 1ms menuOpen linear forwards;
    transform: translateY(-100%);
    @keyframes menuOpen {
      0% {
        transform: translatey(-50%);
      }
      100% {
        transform: translatey(0);
      }
    } */
  }
}

.statiscticsMenuListOpen,
.orderMenuListOpen,
.productrMenuListOpen,
.userMenuListOpen {
  display: none;
}
</style>