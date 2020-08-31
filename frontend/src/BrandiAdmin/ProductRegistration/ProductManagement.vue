<template>
  <div class="productManagementContainer">
    <div class="productTitle">
      <h1>상품관리</h1>
    </div>
    <article class="filterArticle">
      <div class="filterContainer">
        <div class="filterDate">조회 기간</div>
        <input class="startDate" placeholder="클릭해주세요." />
        <div class="middleDate">~</div>
        <input class="endDate" placeholder="클릭해주세요." />
      </div>
      <div class="filterContainer">
        <div class="filterDate">판매여부 :</div>
        <v-btn class="btnAll" color="primary">전체</v-btn>
        <v-btn class="btnV" color="white">판매</v-btn>
        <v-btn class="btnV" color="white">미판매</v-btn>
      </div>
      <div class="filterContainer">
        <div class="filterDate">할인여부 :</div>
        <v-btn class="btnAll" color="primary">전체</v-btn>
        <v-btn class="btnV" color="white">할인</v-btn>
        <v-btn class="btnV" color="white">미할인</v-btn>
      </div>
      <div class="filterContainer">
        <div class="filterDate">진열여부 :</div>
        <v-btn class="btnAll" color="primary">전체</v-btn>
        <v-btn class="btnV" color="white">진열</v-btn>
        <v-btn class="btnV" color="white">미진열</v-btn>
      </div>
      <div class="centerContainer">
        <v-btn tile class="btnSearch" color="primary">검색</v-btn>
        <v-btn tile color="white">초기화</v-btn>
      </div>
    </article>
    <div class="subTitle">
      <p>상품 관리 / 상품 관리 > 상품관리 관리 > 리스트</p>
      <!-- <div v-on:click="onColorClick" class="option"> -->
      <!-- <div>{{ colorToggleData }}</div>
          <div class="imgContainer">
            <img
              src="https://www.brandi.co.kr/static/3.49.1/images/ic-arrow-bl-down@3x.png"
            />
      </div>-->
      <!-- <div
          v-bind:class="{
              toggleOn: isColorToggle,
              toggleOff: !isColorToggle,
            }"
      >-->
      <div :click="pageNumClick" class="defaultToggle">
        {{toggleData}}
        <div class="imgContainer">
          <img src="/Images/arrow-down.png" />
        </div>
      </div>
      <!-- <div
          v-for="(item, index) in detailData.option_colors"
          class="colorToggle"
          v-bind:key="index"
          @click="colorToggleData = detailData.option_colors[index]"
      >{{ item }}</div>-->
      <!-- </div> -->
      <!-- </div> -->
    </div>
    <div>
      <v-btn small>선택상품 엑셀다운로드</v-btn>
      <v-btn small>전체상품 엑셀다운로드</v-btn>
    </div>
    <article class="tableArticle">
      <div class="totalPageNumber">
        전체 조회건 수 :
        <strong>1,964,433 건</strong>
      </div>
      <table class="dataTable">
        <thead class="tableTitle">
          <tr>
            <th class="checkbox">체크</th>
            <th>등록일</th>
            <th class="imgBox">대표이미지</th>
            <th>상품명</th>
            <th>상품코드</th>
            <th>상품번호</th>
            <th>판매가</th>
            <th>할인가</th>
            <th>판매여부</th>
            <th>진열여부</th>
            <th>할인여부</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="checkbox">체크</td>
            <td>2020-08-18 13:13:11</td>
            <td class="imgTd">
              <div class="imgContainer">
                <img src="/Images/17866000_1598706486_image1_S.jpg" />
              </div>
            </td>
            <td>[옴니어스]API S</td>
            <td>SN0000000018312</td>
            <td>17865665</td>
            <td>1,500,000</td>
            <td>1,500,000</td>
            <td>미판매</td>
            <td>미진열</td>
            <td>미할인</td>
          </tr>
        </tbody>
      </table>
    </article>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isToggle: false,
      toggleData: "10개씩 보기",
    };
  },
  methods: {
    pageNumClick() {
      this.isToggle = !this.isToggle;
    },
  },
};
</script>

<style lang="scss" scoped>
.text-start {
  padding: 10px 16px;
}
.productManagementContainer {
  background-color: #fafafa;

  .productTitle {
    margin: 10px 20px;
    font-weight: 200;

    h1 {
      font-size: 26px;
    }
  }

  .filterArticle {
    border: 3px solid #dbdbdb;
    margin: 10px;
    padding: 15px 20px;
    margin-bottom: 20px;

    .filterContainer {
      display: flex;
      align-items: center;
      margin-bottom: 10px;

      .btnAll {
        margin-right: 10px;
      }

      .btnV {
        margin-right: 5px;
      }

      .filterDate {
        width: 130px;
      }

      .startDate,
      .endDate {
        border: 1px solid #dbdbdb;
      }

      .middleDate {
        width: 30px;
        text-align: center;
        background-color: #dbdbdb;
        border: 1px solid #dbdbdb;
      }
    }

    .centerContainer {
      margin: 10px;
      display: flex;
      justify-content: center;

      .btnSearch {
        margin-right: 5px;
      }
    }
  }
}

.subTitle {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #eee;
  margin-bottom: 16px;
  font-size: 14px;
  padding: 8px 16px;

  p {
    margin: 0;
  }

  .defaultToggle {
    background-color: white;
    padding: 4px 20px;
    border: 1px solid #e5e5e5;
    border-radius: 5px;
    display: flex;
    align-items: center;
    cursor: pointer;

    .imgContainer {
      width: 14px;
      height: 8px;
      margin-left: 8px;

      img {
        width: 100%;
        height: 100%;
      }
    }
  }
}

.tableArticle {
  margin: 10px;

  .totalPageNumber {
    font-size: 13px;

    strong {
      font-weight: bold;
    }
  }

  .dataTable {
    display: table;
    border: 1px solid black;
    width: 100%;
    height: 40px;
    font-size: 14px;
    text-align: center;
    border-collapse: collapse;

    th,
    td {
      padding: 8px 0;
      vertical-align: top;
      border: 0.5px solid rgb(221, 221, 211);
    }

    .checkbox {
      width: 50px;
      height: 30px;
    }

    .imgBox {
      width: 87px;
    }

    .imgTd {
      width: 87px;
      height: 87px;

      .imgContainer {
        width: 70px;
        height: 70px;
        margin: 0 8px;

        img {
          width: 100%;
          height: 100%;
        }
      }
    }
  }
}
</style>
