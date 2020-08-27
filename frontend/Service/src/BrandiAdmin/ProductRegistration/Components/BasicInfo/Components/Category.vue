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
            <v-select :items="items" label="1차 카테고리를 선택해주세요" solo></v-select>
          </div>
          <div class="secondaryCategory">
            <v-select :items="items" label="1차 카테고리를 먼저 선택해주세요" solo></v-select>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: ["Foo", "Bar", "Fizz", "Buzz"],
    };
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

        .primaryCategory {
          width: 50%;
        }

        .secondaryCategory {
          width: 50%;
        }
      }
    }
  }
}
</style>
