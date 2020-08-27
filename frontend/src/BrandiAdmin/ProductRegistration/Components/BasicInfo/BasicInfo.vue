<template>
  <div>
    <article class="basicInfo">
      <div class="title">
        <i class="fas fa-pencil-alt"></i>
        <span class="menuName">기본 정보</span>
      </div>
      <SellerSelect />
      <SalesStatus />
      <DisplayStatus />
      <Category />
      <ProductName />
      <ProductOneLineDescription />
      <ImageRegistraion />
      <DetailProductDescription />
    </article>
  </div>
</template>

<script>
import SellerSelect from "./Components/SellerSelect";
import SalesStatus from "./Components/SalesStatus";
import DisplayStatus from "./Components/DisplayStatus";
import Category from "./Components/Category";
import ProductName from "./Components/ProductName";
import ProductOneLineDescription from "./Components/ProductOneLineDescription";
import ImageRegistraion from "./Components/ImageRegistraion";
import DetailProductDescription from "./Components/DetailProductDescription";
export default {
  components: {
    SellerSelect,
    SalesStatus,
    DisplayStatus,
    Category,
    ProductName,
    ProductOneLineDescription,
    ImageRegistraion,
    DetailProductDescription,
  },
};
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
    font-size: 18px;
    padding-left: 15px;

    .menuName {
      margin-left: 10px;
    }
  }
}
</style>