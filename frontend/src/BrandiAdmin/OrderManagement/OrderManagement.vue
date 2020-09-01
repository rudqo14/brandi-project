<template>
  <div class="orderManagementContainer">
    <div class="orderTitle">
      <h1>주문 관리</h1>
      <h2>결제완료 관리</h2>
    </div>
    <article class="filterArticle">
      <div class="filterContainer">
        <div class="filterDate">
          <v-select
            class="select"
            :items="items"
            label="Select.."
            dense
          ></v-select>
          <input class="search" placeholder="검색어를 입력하세요." />
        </div>
      </div>
      <div class="filterContainer">
        <div class="filterDate">주문완료일:</div>
        <div class="btnContainer">
          <v-btn
            v-on:click="sellHandler"
            class="btnAll"
            name="전체"
            v-bind:color="sellData === '전체' ? 'primary' : 'white'"
            >전체</v-btn
          >
          <v-btn
            v-on:click="sellHandler"
            class="btnV"
            name="오늘"
            v-bind:color="sellData === '오늘' ? 'primary' : 'white'"
            >오늘</v-btn
          >
          <v-btn
            v-on:click="sellHandler"
            class="btnV"
            name="3일"
            v-bind:color="sellData === '3일' ? 'primary' : 'white'"
            >3일</v-btn
          >
          <v-btn
            v-on:click="sellHandler"
            class="btnV"
            name="1주일"
            v-bind:color="sellData === '1주일' ? 'primary' : 'white'"
            >1주일</v-btn
          >
          <v-btn
            v-on:click="sellHandler"
            class="btnV"
            name="1개월"
            v-bind:color="sellData === '1개월' ? 'primary' : 'white'"
            >1개월</v-btn
          >
          <v-btn
            v-on:click="sellHandler"
            class="btnV"
            name="3개월"
            v-bind:color="sellData === '3개월' ? 'primary' : 'white'"
            >3개월</v-btn
          >
        </div>
        <a-range-picker :format="dateFormat" @change="onChange" />
      </div>
      <div class="centerContainer">
        <v-btn tile class="btnSearch" color="primary">검색</v-btn>
        <v-btn
          tile
          v-on:click="filterResetHandler"
          class="searchReset"
          color="white"
          >초기화</v-btn
        >
      </div>
    </article>
    <div class="subTitle">
      <p>주문관리 > 결제완료 관리 > 결제완료 리스트</p>
      <div class="rowContainer">
        <div class="toggleContainer">
          <div v-on:click="orderToggleHandler" class="defaultToggle">
            {{ orderToggle }}
            <div class="imgContainer">
              <img src="/Images/arrow-down.png" />
            </div>
          </div>
          <div v-if="isToggleOrder === true" class="toggleDataContainer">
            <div class="toggleList" v-on:click="orderToggleClick">
              최신주문일순
            </div>
            <div class="toggleList" v-on:click="orderToggleClick">
              주문일의 역순
            </div>
          </div>
        </div>
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
            <div class="toggleList" v-on:click="toggleClick">100개씩보기</div>
            <div class="toggleList" v-on:click="toggleClick">150개씩보기</div>
          </div>
        </div>
      </div>
    </div>
    <div class="excelAndCancelContainer">
      <div class="cancelContainer">
        <div class="cancelTitle">전체 조회건 수: {{ totalNumData }}건</div>
        <v-btn color="primary" small>주문취소처리</v-btn>
      </div>
      <div class="excelContainer">
        <v-btn class="excelBtn" color="success" small
          >선택상품 엑셀다운로드</v-btn
        >
        <v-btn class="excelBtn" color="success" small
          >전체상품 엑셀다운로드</v-btn
        >
      </div>
    </div>
    <article class="tableArticle">
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
            <th>결제일자</th>
            <th>주문번호</th>
            <th>주문상세번호</th>
            <th>상품명</th>
            <th>옵션정보</th>
            <th>수량</th>
            <th>주문자명</th>
            <th>핸드폰번호</th>
            <th>결제금액</th>
            <th>주문상태</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in orderData.data" :key="i">
            <td class="checkboxContainer">
              <input
                @click="checkedHandler"
                class="checkbox"
                v-bind:checked="isChecked"
                type="checkbox"
              />
            </td>
            <td>{{ item.order_time }}</td>
            <td>{{ item.order_no }}</td>
            <td>{{ item.order_detail_no }}</td>
            <td class="productName">{{ item.product_name }}</td>
            <td>{{ item.color }} / {{ item.size }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.user_name }}</td>
            <td>{{ item.phone_number }}</td>
            <td>{{ Math.floor(item.price).toLocaleString(5) + "원" }}</td>
            <td>{{ item.order_status }}</td>
          </tr>
        </tbody>
      </table>
      <div class="excelAndCancelContainer">
        <div class="cancelContainer">
          <v-btn color="primary" small>주문취소처리</v-btn>
        </div>
        <div class="excelContainer">
          <v-btn class="excelBtn" color="success" small
            >선택상품 엑셀다운로드</v-btn
          >
          <v-btn class="excelBtn" color="success" small
            >전체상품 엑셀다운로드</v-btn
          >
        </div>
      </div>
      <template>
        <div class="text-center">
          <v-pagination
            v-model="page"
            :length="Math.ceil(totalNumData / toggleNumber)"
          />
        </div>
      </template>
    </article>
  </div>
</template>

<script>
// import HotelDatePicker from "vue-hotel-datepicker";
// import Datepicker from "vuejs-datepicker";
import moment from "moment";
import axios from "axios";
import { sujungIp } from "../../../config";

export default {
  created() {
    axios
      .get(
        `${sujungIp}/admin/order/orderCompletedList?limit=10&page=1&fromDate=20200420`
      )
      .then((res) => {
        this.orderData = res.data;
        this.totalNumData = res.data.total_number;
      });
  },

  data() {
    return {
      dateFormat: "YYYY/MM/DD",
      items: [
        "Select..",
        "주문번호",
        "주문상세번호",
        "주문자명",
        "핸드폰번호",
        "셀러명",
        "상품명",
      ],
      isOrderFilter: false,
      totalNumData: 0,
      orderData: [],
      isToggleOrder: false,
      orderToggle: "최신주문일순",
      isTogglePageNum: false,
      toggleData: "10개씩보기",
      toggleNumber: 10,
      sellData: "전체",
      saleData: "전체",
      displayData: "전체",
      disabledDates: {},
      startDate: "",
      endDate: "",
      totalChecked: false,
      isChecked: false,
      tableData: [],
      totalPageNum: 0,
      page: 1,
    };
  },
  watch: {
    page: function() {
      axios
        .get(
          `${sujungIp}/admin/order/orderCompletedList?limit=${this.toggleNumber}&sort=${this.isOrderFilter}&page=${this.page}&fromDate=20200420`
        )
        .then((res) => {
          this.orderData = res.data;
          this.totalNumData = res.data.total_number;
        });
    },
  },

  methods: {
    moment,
    //페이지의 아이템을 몇개씩 보여줄껀지에 대한 토글 기능
    pageNumClick() {
      this.isTogglePageNum = !this.isTogglePageNum;
    },

    orderToggleHandler() {
      this.isToggleOrder = !this.isToggleOrder;
    },

    orderToggleClick(e) {
      this.orderToggle = e.target.innerHTML;
      this.isToggleOrder = false;

      this.orderToggle === "최신주문일순"
        ? (this.isOrderFilter = false)
        : (this.isOrderFilter = true);

      axios
        .get(
          `${sujungIp}/admin/order/orderCompletedList?limit=${this.toggleNumber}&sort=${this.isOrderFilter}&page=1&fromDate=20200420`
        )
        .then((res) => {
          this.orderData = res.data;
          this.totalNumData = res.data.total_number;
        });
    },

    //토글 아이템 클릭시 10개인지 20개인지 필터링하여
    //백엔드와 통신한 데이터를 통해 리스트를 보여준다.
    toggleClick(e) {
      this.toggleData = e.target.innerHTML;
      this.isTogglePageNum = false;

      if (e.target.innerHTML === "10개씩보기") {
        this.toggleNumber = 10;
      } else if (e.target.innerHTML === "20개씩보기") {
        this.toggleNumber = 20;
      } else if (e.target.innerHTML === "50개씩보기") {
        this.toggleNumber = 50;
      } else if (e.target.innerHTML === "100개씩보기") {
        this.toggleNumber = 100;
      } else if (e.target.innerHTML === "150개씩보기") {
        this.toggleNumber = 150;
      }

      axios
        .get(
          `${sujungIp}/admin/order/orderCompletedList?limit=${this.toggleNumber}&sort=${this.isOrderFilter}&page=1&fromDate=20200420`
        )
        .then((res) => {
          this.orderData = res.data;
          this.totalNumData = res.data.total_number;
        });
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

  components: {
    // HotelDatePicker,
    // Datepicker,
  },
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

.orderManagementContainer {
  background-color: #fafafa;

  .orderTitle {
    margin: 10px 20px;
    font-weight: 200;
    display: flex;
    align-items: center;

    h1 {
      font-size: 26px;
    }

    h2 {
      font-size: 16px;
      color: #888888;
    }
  }

  .filterArticle {
    border: 3px solid #dbdbdb;
    margin: 10px;
    padding: 15px 20px;
    margin-bottom: 20px;

    .filterContainer {
      width: 1000px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;

      .filterDate {
        display: flex;
        margin-bottom: 30px;

        .select {
          width: 200px;
          margin-right: 50px;
        }

        .search {
          width: 400px;
          background: white;
          border: 1px solid #e5e5e5;
          border-radius: 5px;
          padding: 2px 10px;

          &:focus {
            border: 1px solid black;
            border-radius: 5px;
          }
        }
      }
    }

    .centerContainer {
      margin: 50px 0 20px;
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

  .rowContainer {
    display: flex;

    .toggleContainer {
      position: relative;

      .toggleDataContainer {
        position: absolute;
        top: 30px;
        left: 0;
        background-color: white;
        border: 1px solid #e5e5e5;
        width: 134px;
        z-index: 999;
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
}

.excelAndCancelContainer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px;

  .cancelContainer {
    display: flex;

    .cancelTitle {
      margin-right: 10px;
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

    .productName {
      width: 400px;
      padding: 5px 20px;
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
