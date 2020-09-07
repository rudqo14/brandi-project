<template>
  <div class="category">
    <div class="inputName">
      <div>카테고리</div>
      <div class="requiredMark">*</div>
    </div>
    <div class="inputPlace">
      <div class="inputPlaceWrapper">
        <div class="cateSort">
          <div class="primarySortText">1차 카테고리</div>
          <div class="secondarySortText">2차 카테고리</div>
        </div>
        <div class="cateSelect">
          <div class="primaryCategory">
            <select
              class="mainCategoryBox"
              @change="getSubCategory"
              v-model="mainCategoryId"
            >
              <option value selected>1차 카테고리를 선택해주세요</option>
              <option
                v-for="list in mainCategory"
                :key="list.main_category_no"
                :value="list.main_category_no"
                >{{ list.name }}</option
              >
            </select>
          </div>
          <div class="secondaryCategory">
            <select
              class="subCategoryBox"
              @change="selectSubCategory"
              v-model="subCategoryId"
            >
              <option value v-if="!mainCategoryId"
                >1차 카테고리를 먼저 선택해주세요</option
              >
              <option value selected v-if="mainCategoryId"
                >2차 카테고리를 선택해주세요</option
              >
              <option
                v-for="list in subCategory"
                :key="list.sub_category_no"
                :value="list.sub_category_no"
                >{{ list.name }}</option
              >
            </select>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapMutations } from "vuex";
import { SERVER_IP } from "../../../../../../config";

const AdminStore = "adminStore";

export default {
  created() {
    this.getMainCategoryData();
  },

  data() {
    return {
      mainCategory: [],
      subCategory: [],
      key: "",
    };
  },

  methods: {
    ...mapMutations(AdminStore, ["getMainCategoryId", "getSubCategoryId"]),

    // 1차 카테고리를 가져오는 메소드 (첫 렌더링 때 사용)
    getMainCategoryData() {
      axios.get(`${SERVER_IP}/admin/product/category`).then((res) => {
        this.mainCategory = res.data.data;
      });
    },

    // 1차 카테고리 ID 를 state 로 전달하고,
    // 2차 카테고리 데이터를 가져오는 메소드 (1차 카테고리가 바뀔 때 마다 2차 카테고리 변경)
    getSubCategory(event) {
      this.getMainCategoryId(event.target.value);

      axios
        .get(`${SERVER_IP}/admin/product/category/${this.mainCategoryId}`)
        .then((res) => {
          this.subCategory = res.data.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    // 2차 카테고리 ID 를 state 로 전달해주는 메소드
    selectSubCategory(event) {
      this.getSubCategoryId(event.target.value);
    },
  },
};
</script>

<style lang="scss" scoped>
.category {
  display: flex;
  height: 150px;
  border-bottom: 1px solid lightgray;

  .inputName {
    display: flex;
    align-items: center;
    width: 298px;
    height: 100%;
    padding-left: 15px;
    border-right: 1px solid lightgray;
    font-size: 15px;

    .requiredMark {
      margin-left: 4px;
      color: red;
    }
  }

  .inputPlace {
    width: 100%;

    .inputPlaceWrapper {
      margin: 10px;
      border: 1px solid lightgray;
      .cateSort {
        display: flex;
        height: 45%;

        .primarySortText {
          display: flex;
          align-items: center;
          border-right: 1px solid lightgray;
          width: 50%;
          padding-left: 10px;
        }

        .secondarySortText {
          display: flex;
          align-items: center;
          padding-left: 10px;
        }
      }

      .cateSelect {
        display: flex;
        height: 40%;

        .primaryCategory,
        .secondaryCategory {
          width: 50%;

          select {
            appearance: menulist-button;
            background-color: white;
            border: 1px solid lightgray;
            padding-left: 3px;
            border-radius: 3px;
            width: 100%;
            height: 34px;
          }
        }
      }
    }
  }
}
</style>
