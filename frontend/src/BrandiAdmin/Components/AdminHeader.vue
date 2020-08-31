<template>
  <div class="AdminHeader">
    <header>
      <div class="adminPageLogo">
        <div class="logoWrapper">
          <img class="brandiLogoImg" src="/Images/admin-logo.png" alt="img" />
        </div>
      </div>
      <div class="adminAccount">
        <div class="account">intern_master</div>
        <div class="accountToggle">⌄</div>
      </div>
    </header>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.AdminHeader {
  height: 45px;

  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    background: #873b53;
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
}
</style>
