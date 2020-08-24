<template>
  <div id="app">
    <Header />
    <router-view></router-view>
  </div>
</template>

<script>
import Header from "../src/BrandiService/Components/Header";
import detail from "./BrandiService/Detail/Detail.vue";

export default {
  components: {
    Header,
  },
};
</script>

<style lang="scss">
@import "./Styles/reset.scss";
</style>
