<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import detail from "./BrandiService/Detail/Detail.vue";

export default {
  components: {
    detail,
  },
};
</script>

<style lang="scss">
@import "./Styles/reset.scss";
</style>
