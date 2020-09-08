<template>
  <v-app id="app">
    <Header v-if="$route.path.indexOf('admin') == -1" />
    <router-view :key="$route.fullPath"></router-view>
    <Footer v-if="$route.path.indexOf('admin') == -1" />
  </v-app>
</template>

<script>
import Header from "./BrandiService/Components/Header";
import Footer from "./BrandiService/Components/Footer";

export default {
  components: {
    Header,
    Footer,
  },
};
</script>

<style lang="scss">
@import "./Styles/reset.scss";
</style>
