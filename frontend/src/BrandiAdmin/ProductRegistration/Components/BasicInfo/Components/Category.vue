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
            <select class="mainCategoryBox">
              <option value="0">1차 카테고리를 선택해주세요</option>
              <option
                @click="selectMainCategory($event, list.main_category_no)"
                v-for="list in mainCategory"
                :key="list.main_category_no"
                :value="list.main_category_no"
              >{{list.name}}</option>
            </select>
          </div>
          <div class="secondaryCategory">
            <select class="subCategoryBox">
              <option value="0">2차 카테고리를 선택해주세요</option>
              <option value="1">2차 카테고리를 선택해주세요</option>
            </select>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  created() {
    this.getMainCategoryData();
  },

  data() {
    return {
      mainCategory: [],
    };
  },

  methods: {
    getMainCategoryData() {
      axios.get("http://localhost:8080/Data/MainCategory.json").then((res) => {
        this.mainCategory = res.data.data;
      });
    },
    selectMainCategory(event, id) {
      console.log("asdfasdf");
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


