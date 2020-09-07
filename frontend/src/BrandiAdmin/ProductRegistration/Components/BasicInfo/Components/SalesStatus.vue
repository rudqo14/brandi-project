<template>
  <div>
    <div class="salesStatus">
      <div class="inputName">
        <div>판매여부</div>
      </div>
      <div class="inputPlace">
        <div class="radioContainer">
          <v-radio-group v-model="defaultValue" row>
            <v-radio label="판매" value="판매" @click="sellYesSelect"></v-radio>
            <v-radio
              label="미판매"
              value="미판매"
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
import { mapMutations, mapState } from "vuex";

const AdminStore = "adminStore";

export default {
  data() {
    return {
      defaultValue: "판매",
    };
  },

  computed: {
    // store 의 state 를 사용하는 코드, 단일 컴포넌트의 data 를 사용하는 것처럼 사용하면 된다.
    ...mapState(AdminStore, {
      sellYn: (state) => state.sellYn,
    }),
  },

  // store 의 mutations 를 사용하는 코드 , 사용할 때는 this.함수명()
  methods: {
    ...mapMutations(AdminStore, ["sellYesHandler", "sellNoHandler"]),

    // 판매여부를 "판매" 로 선택하는 메소드
    sellYesSelect() {
      this.sellYesHandler();
    },

    // 판매여부를 "미판매" 로 선택하는 메소드
    sellNoSelect() {
      this.sellNoHandler();
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
