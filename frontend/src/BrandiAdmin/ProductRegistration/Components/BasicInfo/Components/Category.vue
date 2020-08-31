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
              @change="getSubCategory($event)"
              v-model="key"
            >
              <option value="0">1차 카테고리를 선택해주세요</option>
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
              @change="selectSubCategory($event)"
              v-model="value"
            >
              <option value="0">2차 카테고리를 선택해주세요</option>
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
import { ADMIN_API_URL } from "../../../../../../config";

export default {
  created() {
    this.getMainCategoryData();
  },

  data() {
    return {
      mainCategory: [],
      subCategory: [],
      key: "",
      mainCategoryId: "",
      subCategoryId: "",
    };
  },

  methods: {
    getMainCategoryData() {
      axios.get(`${ADMIN_API_URL}/admin/product/category`).then((res) => {
        this.mainCategory = res.data.data;
      });
    },
    getSubCategory(event) {
      this.mainCategoryId = event.target.value;

      axios
        .get(`${ADMIN_API_URL}/admin/product/category/${this.mainCategoryId}`)
        .then((res) => {
          this.subCategory = res.data.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    selectSubCategory(event) {
      this.subCategoryId = event.target.value;
      console.log("subCategoryId: ", this.subCategoryId);
      console.log("mainCategoryId: ", this.mainCategoryId);
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
