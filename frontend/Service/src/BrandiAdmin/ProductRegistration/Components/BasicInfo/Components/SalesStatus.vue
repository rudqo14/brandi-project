<template>
  <div>
    <div class="salesStatus">
      <div class="inputName">
        <div>판매여부</div>
      </div>
      <div class="inputPlace">
        <div class="radioContainer">
          <div class="onSale">
            <input type="radio" />
            <span>판매</span>
          </div>
          <div class="offSale">
            <input type="radio" />
            <span>미판매</span>
          </div>
        </div>
        <div class="alertText">
          <i class="fas fa-exclamation-triangle"></i> 미판매 선택시 앱에서 Sold Out으로 표시 됩니다.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.salesStatus {
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
  }

  .inputPlace {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    margin-left: 10px;

    .radioContainer {
      display: flex;
      margin-bottom: 7px;
      font-size: 16px;

      .onSale {
        margin-right: 40px;
      }
    }

    .alertText {
      color: #1e90ff;
      font-size: 14px;
    }
  }
}
</style>