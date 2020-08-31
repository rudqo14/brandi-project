<template>
  <div>
    <div class="salesStatus">
      <div class="inputName">
        <div>판매여부</div>
      </div>
      <div class="inputPlace">
        <div class="radioContainer">
          <v-radio-group v-model="row" row>
            <v-radio
              label="판매"
              value="radio-1"
              @click="sellYesHandler"
            ></v-radio>
            <v-radio
              label="미판매"
              value="radio-2"
              @click="sellNoHandler"
            ></v-radio>
          </v-radio-group>
        </div>
        <div class="alertText">
          <i class="fas fa-exclamation-triangle"></i> 미판매 선택시 앱에서 Sold
          Out으로 표시 됩니다.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from "vuex";

const AdminStore = "adminStore";

export default {
  data() {
    return {};
  },
  computed: {},
  methods: {
    ...mapMutations(AdminStore, ["sellYesHandler, sellNoHandler"]),
    sellYesHandler() {
      this.sellYesHandler;
    },
    sellNoHandler() {
      this.sellNoHandler;
    },
  },
};
</script>

<style lang="scss" scoped>
.salesStatus {
  display: flex;
  height: 70px;
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
      font-size: 16px;

      .v-input {
        font-size: 10px;
        margin: 0;
        height: 30px;
      }
    }

    .alertText {
      color: #1e90ff;
      font-size: 14px;
      margin-left: 4px;
    }
  }
}
</style>
