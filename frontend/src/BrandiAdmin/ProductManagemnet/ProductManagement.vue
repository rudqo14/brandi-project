<template>
  <div class="productManagementContainer">
    <div class="productTitle">
      <h1>상품관리</h1>
    </div>
    <article class="filterArticle">
      <div class="filterContainer">
        <div class="filterDate">조회 기간</div>
        <a-date-picker
          v-model="startValue"
          :disabled-date="disabledStartDate"
          format="YYYY-MM-DD"
          placeholder="Start"
          @openChange="handleStartOpenChange"
        />
        <a-date-picker
          v-model="endValue"
          :disabled-date="disabledEndDate"
          format="YYYY-MM-DD"
          placeholder="End"
          :open="endOpen"
          @openChange="handleEndOpenChange"
        />
      </div>
      <div class="filterContainer">
        <div class="filterDate">판매여부 :</div>
        <v-btn
          v-on:click="sellHandler"
          class="btnAll"
          name="전체"
          v-bind:color="sellData === '전체' ? 'primary' : 'white'"
        >전체</v-btn>
        <v-btn
          v-on:click="sellHandler"
          class="btnV"
          name="판매"
          v-bind:color="sellData === '판매' ? 'primary' : 'white'"
        >판매</v-btn>
        <v-btn
          v-on:click="sellHandler"
          class="btnV"
          name="미판매"
          v-bind:color="sellData === '미판매' ? 'primary' : 'white'"
        >미판매</v-btn>
      </div>
      <div class="filterContainer">
        <div class="filterDate">할인여부 :</div>
        <v-btn
          v-on:click="saleHandler"
          class="btnAll"
          name="전체"
          v-bind:color="saleData === '전체' ? 'primary' : 'white'"
        >전체</v-btn>
        <v-btn
          v-on:click="saleHandler"
          class="btnV"
          name="할인"
          v-bind:color="saleData === '할인' ? 'primary' : 'white'"
        >할인</v-btn>
        <v-btn
          v-on:click="saleHandler"
          class="btnV"
          name="미할인"
          v-bind:color="saleData === '미할인' ? 'primary' : 'white'"
        >미할인</v-btn>
      </div>
      <div class="filterContainer">
        <div class="filterDate">진열여부 :</div>
        <v-btn
          v-on:click="displayHandler"
          class="btnAll"
          name="전체"
          v-bind:color="displayData === '전체' ? 'primary' : 'white'"
        >전체</v-btn>
        <v-btn
          v-on:click="displayHandler"
          class="btnV"
          name="진열"
          v-bind:color="displayData === '진열' ? 'primary' : 'white'"
        >진열</v-btn>
        <v-btn
          v-on:click="displayHandler"
          class="btnV"
          name="미진열"
          v-bind:color="displayData === '미진열' ? 'primary' : 'white'"
        >미진열</v-btn>
      </div>
      <div class="centerContainer">
        <v-btn tile @click="searchFilterHandler" class="btnSearch" color="primary">검색</v-btn>
        <v-btn tile v-on:click="filterResetHandler" class="searchReset" color="white">초기화</v-btn>
      </div>
    </article>
    <div class="subTitle">
      <p>상품 관리 / 상품 관리 > 상품관리 관리 > 리스트</p>
      <div class="toggleContainer">
        <div v-on:click="pageNumClick" class="defaultToggle">
          {{ toggleData }}
          <div class="imgContainer">
            <img src="/Images/arrow-down.png" />
          </div>
        </div>
        <div v-if="isTogglePageNum === true" class="toggleDataContainer">
          <div class="toggleList" v-on:click="toggleClick">10개씩보기</div>
          <div class="toggleList" v-on:click="toggleClick">20개씩보기</div>
          <div class="toggleList" v-on:click="toggleClick">50개씩보기</div>
        </div>
      </div>
    </div>
    <div class="excelContainer">
      <v-btn class="excelBtn" color="success" small>선택상품 엑셀다운로드</v-btn>
      <v-btn class="excelBtn" color="success" small>전체상품 엑셀다운로드</v-btn>
    </div>
    <article class="tableArticle">
      <div class="totalPageNumber">
        전체 조회건 수 :
        <strong>{{ totalNumData }} 건</strong>
      </div>
      <div class="scollcontainer">
        <table class="dataTable">
          <thead class="tableTitle">
            <tr>
              <th class="checkboxContainer">
                <input
                  @click="totalCheckedHandler"
                  class="checkbox"
                  :checked="totalChecked"
                  type="checkbox"
                />
              </th>
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
            <tr v-for="(item, i) in tableData" :key="i">
              <td class="checkboxContainer">
                <input
                  @click="checkedHandler"
                  class="checkbox"
                  :checked="isChecked"
                  type="checkbox"
                />
              </td>
              <td>{{ item.productRegistDate }}</td>
              <td class="imgTd">
                <div class="imgContainer">
                  <img :src="item.productSmallImageUrl" />
                </div>
              </td>
              <td>{{ item.productName }}</td>
              <td>{{ item.productCode }}</td>
              <td>{{ item.productNo }}</td>
              <td>{{Math.floor(item.sellPrice).toLocaleString(5) + "원"}}</td>
              <td>{{Math.floor(item.discountPrice).toLocaleString(5) + "원"}}</td>
              <td>{{ item.productSellYn }}</td>
              <td>{{ item.productExhibitYn }}</td>
              <td>{{item.discountYn}}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- 페이지네이션 UI라이브러리를 사용하지 않은 커스텀 페이지네이션 -->
      <!-- <div class="productPagination">
        <button class="prevBtn" name="minus">{{prev}}{{prev}}</button>
        <button class="prevBtn" name="minus">{{prev}}</button>
        <ul class="hotelPageList">
          <li>1</li>
        </ul>
        <button class="nextBtn" name="plus">{{next}}</button>
        <button class="nextBtn" name="plus">{{next}}{{next}}</button>
      </div>-->

      <!-- 페이지 네이션 커스텀화 작업 -->
      <template>
        <div class="text-center">
          <v-pagination v-model="page" :length="Math.ceil(totalNumData / limit)" />
        </div>
      </template>
    </article>
  </div>
</template>

<script>
import { gonhoIp } from "../../../config";
import axios from "axios";

export default {
  created() {
    this.axiosConnect();
  },

  data() {
    return {
      isTogglePageNum: false,
      toggleData: "10개씩보기",
      sellData: "전체",
      saleData: "전체",
      displayData: "전체",
      disabledDates: {},
      totalChecked: false,
      isChecked: false,
      tableData: [],
      totalPageNum: 0,
      limit: 10,
      totalNumData: 0,
      page: 1,
      startValue: null,
      endValue: null,
      endOpen: false,
      startDate: "",
      endDate: "",
      sellDataUrl: "전체",
      saleDataUrl: "전체",
      displayDataUrl: "전체",
    };
  },

  watch: {
    page: function () {
      this.axiosConnect();
    },

    startValue(val) {
      if (val !== null) {
        const startDateYear = val._d.getFullYear();
        const startDateMonth = ("0" + (val._d.getMonth() + 1)).slice(-2);
        const startDateDay = ("0" + val._d.getDate()).slice(-2);

        this.startDate =
          "&startDate=" + startDateYear + startDateMonth + startDateDay;
      }
    },
    endValue(val) {
      if (val !== null) {
        const endDateYear = val._d.getFullYear();
        const endDateMonth = ("0" + (val._d.getMonth() + 1)).slice(-2);
        const endDateDay = ("0" + val._d.getDate()).slice(-2);

        this.endDate = "&endDate=" + endDateYear + endDateMonth + endDateDay;
      }
    },
  },

  methods: {
    axiosConnect() {
      axios
        .get(
          `${gonhoIp}/admin/product?${this.sellDataUrl}${this.saleDataUrl}${this.displayDataUrl}${this.startDate}${this.endDate}&page=${this.page}&limit=${this.limit}`
        )
        .then((res) => {
          console.log(res.data);
          this.tableData = res.data.data[0];
          this.totalNumData = res.data.data[1].total;
        });

      console.log(
        `${gonhoIp}/admin/product?${this.sellDataUrl}${this.saleDataUrl}${this.displayDataUrl}${this.startDate}${this.endDate}&page=${this.page}&limit=${this.limit}`
      );
    },

    searchFilterHandler() {
      if (this.sellData === "판매") {
        this.sellDataUrl = "&sellYn=1";
      } else if (this.sellData === "미판매") {
        this.sellDataUrl = "&sellYn=0";
      } else {
        this.sellDataUrl = "";
      }

      if (this.saleData === "할인") {
        this.saleDataUrl = "&discountYn=1";
      } else if (this.saleData === "미할인") {
        this.saleDataUrl = "&discountYn=0";
      } else {
        this.saleDataUrl = "";
      }

      if (this.displayData === "진열") {
        this.displayDataUrl = "&exhibitionYn=1";
      } else if (this.displayData === "미진열") {
        this.displayDataUrl = "&exhibitionYn=0";
      } else {
        this.displayDataUrl = "";
      }

      this.axiosConnect();
    },

    //DatePicker 적용
    //startDate와 endDate 클릭할때 disabled 적용하여 클릭하지 못하게끔 함
    disabledStartDate(startValue) {
      const endValue = this.endValue;
      if (!startValue || !endValue) {
        return false;
      }
      return startValue.valueOf() > endValue.valueOf();
    },
    disabledEndDate(endValue) {
      const startValue = this.startValue;
      if (!endValue || !startValue) {
        return false;
      }
      return startValue.valueOf() >= endValue.valueOf();
    },
    //start 토글이 종료되면 endDate토글이 열리게 적용
    handleStartOpenChange(open) {
      if (!open) {
        this.endOpen = true;
      }
    },
    handleEndOpenChange(open) {
      this.endOpen = open;
    },

    //페이지의 아이템을 몇개씩 보여줄껀지에 대한 토글 기능
    pageNumClick() {
      this.isTogglePageNum = !this.isTogglePageNum;
    },

    //토글 아이템 클릭시 10개인지 20개인지 필터링하여
    //백엔드와 통신한 데이터를 통해 리스트를 보여준다.
    toggleClick(e) {
      this.toggleData = e.target.innerHTML;
      this.isTogglePageNum = false;

      if (this.toggleData === "10개씩보기") {
        this.limit = 10;
        this.page = 1;
      } else if (this.toggleData === "20개씩보기") {
        this.limit = 20;
        this.page = 1;
      } else if (this.toggleData === "50개씩보기") {
        this.limit = 50;
        this.page = 1;
      }

      this.axiosConnect();
    },

    //판매여부 클릭 이벤트
    //v-btn 클릭시 여백부분 클릭할때와 글씨부분 클릭할때가 다르다.
    sellHandler(e) {
      if (e.target.name) {
        this.sellData = e.target.name;
      } else {
        this.sellData = e.target.innerText;
      }
    },
    saleHandler(e) {
      if (e.target.name) {
        this.saleData = e.target.name;
      } else {
        this.saleData = e.target.innerText;
      }
    },

    displayHandler(e) {
      if (e.target.name) {
        this.displayData = e.target.name;
      } else {
        this.displayData = e.target.innerText;
      }
    },

    //초기화 버튼 클릭시에 필터링에 해당하는 데이터들 모두 초기화시킨다.
    filterResetHandler() {
      this.sellData = "전체";
      this.saleData = "전체";
      this.displayData = "전체";
      this.startValue = null;
      this.endValue = null;
      this.startDate = null;
      this.endDate = null;
    },

    //테이블에 있는 체크버튼중 최상단 체크박스 클릭시
    //모든 체크버튼 ON/OFF 시킴
    totalCheckedHandler() {
      this.totalChecked = !this.totalChecked;

      if (this.totalChecked) {
        this.isChecked = true;
      } else {
        this.isChecked = false;
      }
    },

    checkedHandler() {
      this.totalChecked = false;
    },

    onChange(date, dateString) {
      console.log(date, dateString);
    },
  },

  components: {},
};
</script>

<style lang="scss">
.text-start {
  padding: 10px 16px;
}
.ant-calendar-prev-year-btn,
.ant-calendar-prev-month-btn,
.ant-calendar-next-month-btn,
.ant-calendar-next-year-btn {
  margin-top: 20px;
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
        font-size: 14px;
        padding: 1.5px 15px;
        position: relative;
        cursor: pointer;
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
        cursor: pointer;
      }

      .searchReset {
        cursor: pointer;
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

  .toggleContainer {
    position: relative;

    .toggleDataContainer {
      position: absolute;
      top: 30px;
      left: 0;
      background-color: white;
      border: 1px solid #e5e5e5;
      width: 134px;
      cursor: pointer;

      .toggleList {
        padding: 6px 0 6px 20px;

        &:hover {
          background-color: #3071a9;
          color: white;
        }
      }
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
}

.excelContainer {
  display: flex;
  justify-content: center;

  .excelBtn {
    margin-right: 8px;
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

  .scollcontainer {
    overflow-x: scroll;

    .dataTable {
      display: table;
      border: 1px solid black;
      min-width: 1600px;
      height: 40px;
      font-size: 14px;
      text-align: center;
      border-collapse: collapse;

      th,
      td {
        min-width: 30px;
        padding: 8px 0;
        vertical-align: top;
        border: 0.5px solid rgb(221, 221, 211);
      }

      .checkboxContainer {
        width: 50px;
        height: 30px;

        .checkbox {
          width: 18px;
          height: 18px;
          cursor: pointer;
        }
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

  .productPagination {
    display: flex;
    justify-content: center;
    background-color: white;
    padding: 10px 0;

    ul {
      padding: 0;

      li {
        width: 30px;
        height: 30px;
        border: 1px solid #e5e5e5;
        color: black;
        background-color: #dbdbdb;
        text-align: center;
      }
    }

    .prevBtn,
    .nextBtn {
      width: 30px;
      height: 30px;
      border: 1px solid #e5e5e5;
      color: #428bca;
    }
  }
}
</style>
