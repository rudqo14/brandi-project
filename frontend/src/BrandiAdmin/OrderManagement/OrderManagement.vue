<template>
  <div class="orderManagementContainer">
    <div class="orderTitle">
      <h1>주문 관리</h1>
      <h2>결제완료 관리</h2>
    </div>
    <article class="filterArticle">
      <div class="filterContainer">
        <div class="filterDate">
          <v-select v-model="selectSearch" class="select" :items="items" label="Select.." dense />
          <input
            @keyup.enter="searchFilterHandler"
            v-model="searchInputContents"
            class="search"
            placeholder="검색어를 입력하세요."
          />
        </div>
      </div>
      <div class="filterContainer">
        <div class="filterDate">주문완료일:</div>
        <div class="btnContainer">
          <v-btn
            v-for="(item, i) in dateData"
            :key="i"
            v-on:click="sellHandler(item)"
            class="btnV"
            name="전체"
            v-bind:color="sellData === item ? 'primary' : 'white'"
          >{{item}}</v-btn>
        </div>
        <div>
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
      </div>
      <div class="centerContainer">
        <v-btn tile @click="searchFilterHandler" class="btnSearch" color="primary">검색</v-btn>
        <v-btn tile v-on:click="filterResetHandler" class="searchReset" color="white">초기화</v-btn>
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
            <div class="toggleList" v-on:click="orderToggleClick">최신주문일순</div>
            <div class="toggleList" v-on:click="orderToggleClick">주문일의 역순</div>
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
        <v-btn class="excelBtn" color="success" small>선택상품 엑셀다운로드</v-btn>
        <v-btn class="excelBtn" color="success" small>전체상품 엑셀다운로드</v-btn>
      </div>
    </div>
    <article class="tableArticle">
      <div class="scrollcontainer">
        <table class="dataTable">
          <thead class="tableTitle">
            <tr>
              <th class="checkboxContainer">
                <input v-model="selectAll" class="checkbox" type="checkbox" />
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
            <tr v-for="(item, i) in orderData" :key="i">
              <td class="checkboxContainer">
                <input v-model="selected" :value="i" class="checkbox" type="checkbox" />
              </td>
              <td>{{ item.order_time }}</td>
              <td>{{ item.order_no }}</td>
              <td class="linkDetail">
                <router-link
                  :to="`/admin/productDetail/${item.order_detail_no}`"
                >{{ item.order_detail_no }}</router-link>
              </td>
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
      </div>
      <div class="excelAndCancelContainer">
        <div class="cancelContainer">
          <v-btn color="primary" small>주문취소처리</v-btn>
        </div>
        <div class="excelContainer">
          <v-btn class="excelBtn" color="success" small>선택상품 엑셀다운로드</v-btn>
          <v-btn class="excelBtn" color="success" small>전체상품 엑셀다운로드</v-btn>
        </div>
      </div>
      <template>
        <div class="text-center">
          <v-pagination v-model="page" :length="Math.ceil(totalNumData / toggleNumber)" />
        </div>
      </template>
    </article>
  </div>
</template>

<script>
import moment from "moment";
import axios from "axios";
import { gonhoIp } from "../../../config";
import dateData from "../../../Data/orderDateBtn.json";

export default {
  created() {
    this.resetOrderDate();

    this.axiosConnect();
  },

  computed: {
    selectAll: {
      //체크박스 전체선택/해제
      //체크박스가 선택되어있는지 확인 후 전체선택되어 있으면,
      //전체해제
      //getter를 통해 종속성을 추적
      get() {
        if (!this.orderData.length) {
          return false;
        }
        return this.orderData
          ? this.selected.length == this.orderData.length
          : false;
      },

      //setter를 통해 변경을 알림
      //select한 체크박스값을 배열안에 넣어 적용
      set(value) {
        const selected = [];

        if (value) {
          this.orderData.forEach(function (item, i) {
            selected.push(i);
          });
        }
        this.selected = selected;
      },
    },
  },

  data() {
    return {
      dateData: dateData.data,
      dateFormat: "YYYY/MM/DD",
      items: [
        "Select..",
        "주문번호",
        "주문상세번호",
        "주문자명",
        "핸드폰번호",
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
      sellData: "3일",
      disabledDates: {},
      totalChecked: false,
      isChecked: false,
      totalPageNum: 0,
      page: 1,
      checked: [],
      startValue: null,
      endValue: null,
      endOpen: false,
      searchInputContents: "",
      selectSearch: "",
      searchFilter: "",
      startDate: "",
      endDate: "",
      checked: [],
      selected: [],
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
          "&fromDate=" + startDateYear + startDateMonth + startDateDay;
      } else {
        this.startDate = "";
      }
    },

    endValue(val) {
      if (val !== null) {
        const endDateYear = val._d.getFullYear();
        const endDateMonth = ("0" + (val._d.getMonth() + 1)).slice(-2);
        const endDateDay = ("0" + val._d.getDate()).slice(-2);

        this.endDate = "&toDate=" + endDateYear + endDateMonth + endDateDay;
      } else {
        this.endDate = "";
      }
    },

    selectSearch(e) {
      this.selectSearch = e;
    },
  },

  methods: {
    moment,

    //created 될때 3일에 해당하는 date값을 통해 리스트영역 백엔드와 통신
    //날짜를 보내줄때는 20200904와 같은 형식으로 보내야함
    resetOrderDate() {
      const nowYear = new Date().getFullYear();
      const nowMonth = ("0" + (new Date().getMonth() + 1)).slice(-2);
      const nowDay = ("0" + new Date().getDate()).slice(-2);
      const days = 1000 * 60 * 60 * 24;
      const beforeYear = new Date(new Date() - 3 * days).getFullYear();
      const beforeMonth = (
        "0" +
        (new Date(new Date() - 3 * days).getMonth() + 1)
      ).slice(-2);
      const beforeDays = (
        "0" + new Date(new Date() - 3 * days).getDate()
      ).slice(-2);

      this.startValue = moment(
        `${beforeYear}/${beforeMonth}/${beforeDays}`,
        this.dateFormat
      );
      this.endValue = moment(
        `${nowYear}/${nowMonth}/${nowDay}`,
        this.dateFormat
      );

      this.startDate = `&fromDate=${beforeYear}${beforeMonth}${beforeDays}`;
      this.endDate = `&toDate=${nowYear}${nowMonth}${nowDay}`;
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

    axiosConnect() {
      axios
        .get(
          `${gonhoIp}/admin/order/orderCompletedList?limit=${this.toggleNumber}&sort=${this.isOrderFilter}&page=${this.page}${this.startDate}${this.endDate}${this.searchFilter}`
        )
        .then((res) => {
          this.orderData = res.data.data;
          this.totalNumData = res.data.total_number;
        });
    },

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

      this.axiosConnect();
    },

    //토글 아이템 클릭시 10개인지 20개인지 필터링하여
    //백엔드와 통신한 데이터를 통해 리스트를 보여준다.
    toggleClick(e) {
      this.toggleData = e.target.innerHTML;
      this.isTogglePageNum = false;

      if (e.target.innerHTML === "10개씩보기") {
        this.toggleNumber = 10;
        this.page = 1;
      } else if (e.target.innerHTML === "20개씩보기") {
        this.toggleNumber = 20;
        this.page = 1;
      } else if (e.target.innerHTML === "50개씩보기") {
        this.toggleNumber = 50;
        this.page = 1;
      } else if (e.target.innerHTML === "100개씩보기") {
        this.toggleNumber = 100;
        this.page = 1;
      } else if (e.target.innerHTML === "150개씩보기") {
        this.toggleNumber = 150;
        this.page = 1;
      }

      this.axiosConnect();
    },

    //판매여부 클릭 이벤트
    //v-btn 클릭시 여백부분 클릭할때와 글씨부분 클릭할때가 다르다.
    sellHandler(item) {
      this.sellData = item;
      //현재에 해당하는 날짜 계산하여 년,월,일 추출
      const nowYear = new Date().getFullYear();
      const nowMonth = new Date().getMonth() + 1;
      const nowDay = new Date().getDate();

      const days = 1000 * 60 * 60 * 24;

      if (this.sellData === "전체") {
        this.startValue = null;
        this.endValue = null;
      } else if (this.sellData === "오늘") {
        this.startValue = moment(
          `${nowYear}/${nowMonth}/${nowDay}`,
          this.dateFormat
        );
        this.endValue = moment(
          `${nowYear}/${nowMonth}/${nowDay}`,
          this.dateFormat
        );
      } else if (this.sellData === "3일") {
        const beforeYear = new Date(new Date() - 3 * days).getFullYear();
        const beforeMonth = new Date(new Date() - 3 * days).getMonth() + 1;
        const beforeDays = new Date(new Date() - 3 * days).getDate();

        this.startValue = moment(
          `${beforeYear}/${beforeMonth}/${beforeDays}`,
          this.dateFormat
        );
        this.endValue = moment(
          `${nowYear}/${nowMonth}/${nowDay}`,
          this.dateFormat
        );
      } else if (this.sellData === "1주일") {
        const beforeYear = new Date(new Date() - 7 * days).getFullYear();
        const beforeMonth = new Date(new Date() - 7 * days).getMonth() + 1;
        const beforeDays = new Date(new Date() - 7 * days).getDate();

        this.startValue = moment(
          `${beforeYear}/${beforeMonth}/${beforeDays}`,
          this.dateFormat
        );
        this.endValue = moment(
          `${nowYear}/${nowMonth}/${nowDay}`,
          this.dateFormat
        );
      } else if (this.sellData === "1개월") {
        const prevDate = new Date(
          new Date().setMonth(new Date().getMonth() - 1)
        );

        const beforeYear = prevDate.getFullYear();
        const beforeMonth = prevDate.getMonth() + 1;
        const beforeDays = prevDate.getDate();

        this.startValue = moment(
          `${beforeYear}/${beforeMonth}/${beforeDays}`,
          this.dateFormat
        );
        this.endValue = moment(
          `${nowYear}/${nowMonth}/${nowDay}`,
          this.dateFormat
        );
      } else if (this.sellData === "3개월") {
        const prevDate = new Date(
          new Date().setMonth(new Date().getMonth() - 3)
        );

        const beforeYear = prevDate.getFullYear();
        const beforeMonth = prevDate.getMonth() + 1;
        const beforeDays = prevDate.getDate();

        this.startValue = moment(
          `${beforeYear}/${beforeMonth}/${beforeDays}`,
          this.dateFormat
        );
        this.endValue = moment(
          `${nowYear}/${nowMonth}/${nowDay}`,
          this.dateFormat
        );
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
      this.selectSearch = "";
      this.sellData = "3일";
      this.saleData = "전체";
      this.displayData = "전체";
      this.searchInputContents = "";
      this.resetOrderDate();
    },

    searchFilterHandler() {
      if (this.selectSearch === "주문번호" && this.searchInputContents) {
        this.searchFilter = `&orderId=${this.searchInputContents}`;
      } else if (
        this.selectSearch === "주문상세번호" &&
        this.searchInputContents
      ) {
        this.searchFilter = `&orderDetailId=${this.searchInputContents}`;
      } else if (this.selectSearch === "주문자명" && this.searchInputContents) {
        this.searchFilter = `&orderer=${this.searchInputContents}`;
      } else if (
        this.selectSearch === "핸드폰번호" &&
        this.searchInputContents
      ) {
        this.searchFilter = `&phoneNumber=${this.searchInputContents}`;
      } else if (this.selectSearch === "상품명" && this.searchInputContents) {
        this.searchFilter = `&productName=${this.searchInputContents}`;
      } else {
        this.searchFilter = "";
      }

      if (!this.searchFilter && !this.startDate && !this.endDate) {
        return alert(
          "날짜 조건이 없을 경우에는 필수 필터 조건 검색이 존재합니다.\n(주문번호 or 주문상세번호 or 주문자명 or 핸드폰번호"
        );
      }

      if (this.searchFilter && !this.searchInputContents) {
        return alert("검색어를 입력해주세요.");
      }

      this.axiosConnect();

      this.searchFilter = "";
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
      margin-bottom: 30px;

      .btnContainer {
        margin-right: 40px;

        .btnV {
          margin-right: 4px;
        }
      }

      .filterDate {
        display: flex;
        /* margin-bottom: 30px; */

        .select {
          width: 200px;
          margin-right: 20px;
        }

        .search {
          width: 400px;
          height: 40px;
          background: white;
          border: 1px solid #e5e5e5;
          border-radius: 5px;
          padding: 0 10px;

          &:focus {
            border: 1px solid #dbdbdb;
            outline: none;
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
  .scrollcontainer {
    overflow-x: scroll;

    .dataTable {
      display: table;
      border: 1px solid black;
      min-width: 1600px;
      height: 40px;
      font-size: 14px;
      text-align: center;
      border-collapse: collapse;
      white-space: nowrap;

      .linkDetail {
        text-decoration: underline;
      }

      th,
      td {
        min-width: 100px;
        padding: 8px 4px;
        vertical-align: top;
        border: 0.5px solid rgb(221, 221, 211);
      }

      .productName {
        /* width: 400px; */
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
