<template>
  <div>
    <header>
      <div class="adminPageLogo">
        <div class="logoWrapper">
          <img class="brandiLogoImg" src="/Images/admin-logo.png" alt="img" />
        </div>
        <div class="adminPageChange">⌄</div>
        <div class="adminVersion">staging(200806_authority_func)</div>
      </div>
      <div class="adminAccount">
        <div class="account">intern_master</div>
        <div class="accountToggle">⌄</div>
      </div>
    </header>
    <main class="adminMain">
      <aside :class="{sideMenuBar: !isSideBar, sideMenuBarReduction: isSideBar}">
        <!-- <aside class="sideMenuBar"> -->
        <div class="sideBarToggleContainer">
          <div
            @click="sideBarActive"
            :class="{sideBarToggleWrapper: !isSideBar, sideBarToggleWrapperOff: isSideBar}"
          >
            <i class="fas fa-angle-left"></i>
          </div>
        </div>
        <div class="menuContainer">
          <div :class="{toggleOnSideBar: !isSideBar, toggleOffSideBar: isSideBar}">
            <ReductionSideBar />
          </div>
          <div :class="{openSideBar: !isSideBar, closedSideBar: isSideBar}">
            <OpenSideBar />
          </div>
        </div>
      </aside>
      <section class="content">
        <ProductResistration />
      </section>
    </main>
  </div>
</template>

<script>
import ReductionSideBar from "./ReductionSideBar";
import OpenSideBar from "./OpenSideBar";
import ProductResistration from "../ProductRegistration/ProductResistration";
export default {
  components: {
    ReductionSideBar,
    OpenSideBar,
    ProductResistration,
  },
  data() {
    return {
      isSideBar: false,
    };
  },
  methods: {
    sideBarActive() {
      this.isSideBar = !this.isSideBar;
    },
  },
};
</script>

<style lang="scss" scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #873b53;
  height: 45px;
  padding: 0 20px;

  .adminPageLogo {
    display: flex;
    align-items: center;
    height: 22px;

    .logoWrapper {
      width: 100px;
      height: 22px;

      .brandiLogoImg {
        width: 100%;
        height: 100%;
      }
    }

    .adminPageChange {
      font-size: 15px;
      height: 24px;
      padding: 0 10px;
      color: #fff;
    }

    .adminVersion {
      color: #fff;
      height: 16px;
      font-size: 12px;
    }
  }

  .adminAccount {
    display: flex;
    justify-content: space-around;
    align-items: center;
    border-left: 1px solid #484a4f;
    height: 100%;

    .account {
      color: #cecfd3;
      font-size: 15px;
      margin-left: 10px;
    }

    .accountToggle {
      color: #cecfd3;
      font-size: 15px;
      height: 24px;
      padding: 0 10px;
    }
  }
}
.adminMain {
  display: flex;
  width: 100%;
  height: 100%;

  .sideMenuBarReduction {
    width: 45px;
  }

  .sideMenuBar {
    width: 215px;
  }

  .sideMenuBar,
  .sideMenuBarReduction {
    display: inline-block;
    background-color: #333;
    height: 100%;

    .sideBarToggleContainer {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      height: 100px;

      .sideBarToggleWrapper {
        background: white;
        cursor: pointer;
        border-top-left-radius: 5px;
        border-bottom-left-radius: 5px;
        padding: 10px 10px 10px 14px;
      }

      .sideBarToggleWrapperOff {
        background: white;
        cursor: pointer;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        padding: 10px 10px 10px 14px;
        transform: rotate(180deg);
      }
    }

    .menuContainer {
      width: 215px;
      color: lightgray;
      font-size: 14px;
      font-weight: lighter;

      .toggleOnSideBar {
        display: none;
      }

      .toggleOffSideBar {
        display: block;
      }

      .openSideBar {
        display: block;
      }

      .closedSideBar {
        display: none;
      }

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
    }
  }
}
</style>