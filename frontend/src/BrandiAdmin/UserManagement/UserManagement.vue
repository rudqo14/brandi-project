<template>
  <div>
    <header>
      <div class="pageTitle">
        <span class="mainName">회원 관리_커뮤니티</span>
        <span class="subName">회원 목록</span>
      </div>
      <div class="pageStateBar">
        <i class="fas fa-home"></i>
        <span>회원 관리</span>
        <i class="fas fa-angle-right"></i>
        <span>회원 관리_커뮤니티</span>
        <i class="fas fa-angle-right"></i>
        <span>회원 리스트</span>
      </div>
    </header>
    <section class="pageContents">
      <div class="userTableContainer">
        <div class="containerTitle">
          <i class="fas fa-users"></i>
          <span>회원 리스트</span>
        </div>
        <div class="filterContainer" v-if="this.users.data.length">
          <div class="pageInfo">
            <span>Page</span>
            <button @click="movePage('minus')" :class="[ this.page === 1 ? 'prevent' : '']"><</button>
            <input v-model="page" />
            <button
              @click="movePage('plus')"
              :class="[ this.page === getTotalPage ? 'prevent' : '']"
            >></button>
            <span>of {{ getTotalPage }} | View</span>
            <select v-model="selectedLimit">
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="10">10</option>
              <option value="20">20</option>
              <option value="50">50</option>
              <option value="100">100</option>
              <option value="150">150</option>
            </select>
            <span>records | Found total {{ userTotal }} records</span>
          </div>
        </div>
        <div class="filterContainer" v-else>No records found to show</div>
        <table>
          <thead>
            <tr class="headTop">
              <td class="check">
                <input type="checkbox" />
              </td>
              <td class="userNo">회원 번호</td>
              <td class="userName">회원명</td>
              <td class="socialNetwork">가입계정</td>
              <td class="phoneNumber">휴대폰</td>
              <td class="email">이메일</td>
              <td class="event">이벤트/마케팅 알림</td>
              <td class="accessOS">접속 OS</td>
              <td class="lastAccess">최종접속일</td>
              <td class="createdAt">등록일</td>
              <td class="actions">Actions</td>
            </tr>
            <tr class="headSearch">
              <td class="check"></td>
              <td class="userNo">
                <input v-model="filters.userNo" />
              </td>
              <td class="userName">
                <input v-model="filters.userName" />
              </td>
              <td class="socialNetwork">
                <select v-model="filters.socialNetwork">
                  <option value=" " selected>Select...</option>
                  <option value="브랜디">브랜디</option>
                  <option value="구글">구글</option>
                </select>
              </td>
              <td class="phoneNumber">
                <input v-model="filters.phoneNumber" />
              </td>
              <td class="email">
                <input v-model="filters.email" />
              </td>
              <td class="event"></td>
              <td class="accessOS"></td>
              <td class="lastAccess">
                <div>
                  <a-date-picker v-model="lastAccessFrom" :format="dateFormat" placeholder="From" />
                </div>
                <div>
                  <a-date-picker v-model="lastAccessTo" :format="dateFormat" placeholder="To" />
                </div>
              </td>
              <td class="createdAt">
                <div>
                  <a-date-picker v-model="createdAtFrom" placeholder="From" :format="dateFormat" />
                </div>
                <div>
                  <a-date-picker v-model="createdAtTo" placeholder="To" :format="dateFormat" />
                </div>
              </td>
              <td class="actions">
                <button class="search" @click="searchData">
                  <i class="fas fa-search"></i>Search
                </button>
                <button class="reset" @click="resetFilter">
                  <i class="fas fa-times"></i>Reset
                </button>
              </td>
            </tr>
          </thead>
          <tbody v-if="this.users.data.length">
            <tr v-for="user in users.data">
              <td class="check">
                <input type="checkbox" />
              </td>
              <td class="userNo">{{ user.user_no }}</td>
              <td class="userName">{{ user.name }}</td>
              <td class="socialNetwork">{{ user.social_name ? user.social_name : "브랜디" }}</td>
              <td class="phoneNumber">{{ user.phone_number }}</td>
              <td class="email">{{ user.email }}</td>
              <td class="event">동의</td>
              <td class="accessOS">확인불가</td>
              <td class="lastAccess">{{ user.last_access }}</td>
              <td class="createdAt">{{ user.created_at }}</td>
              <td class="actions">
                <button class="detail">
                  <i class="fas fa-search"></i>Detail
                </button>
                <button class="changePW" v-if="user.social_name === null">비번변경</button>
                <button class="toBrandi" v-else>브랜디 계정으로 전환</button>
              </td>
            </tr>
          </tbody>
          <tbody v-else>
            <tr>
              <td>No data available in table</td>
            </tr>
          </tbody>
        </table>
        <div class="filterContainer">
          <div class="pageInfo">
            <span>Page</span>
            <button @click="movePage('minus')" :class="[ this.page === 1 ? 'prevent' : '']"><</button>
            <input v-model="page" />
            <button
              @click="movePage('plus')"
              :class="[ this.page === getTotalPage ? 'prevent' : '']"
            >></button>
            <span>of {{ getTotalPage }} | View</span>
            <select name="page" v-model="selectedLimit">
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="10">10</option>
              <option value="20">20</option>
              <option value="50">50</option>
              <option value="100">100</option>
              <option value="150">150</option>
            </select>
            <span>records | Found total {{ userTotal }} records</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
​
<script>
import axios from "axios";
import { sip } from "../../../config.js";

export default {
  created() {
    this.getUserData();
  },
  data() {
    return {
      dateFormat: "YYYY/MM/DD",
      users: [],
      userTotal: 0,
      query: "",
      filters: {
        lastAccessFrom: null,
        lastAccessTo: null,
        createdAtFrom: null,
        createdAtTo: null,
        userNo: null,
        userName: null,
        socialNetwork: null,
        phoneNumber: null,
        email: null
      },
      page: 1,
      selectedLimit: 1,
      offset: 1,
      lastAccessFrom: null,
      lastAccessTo: null,
      createdAtFrom: null,
      createdAtTo: null
    };
  },
  methods: {
    getUserData() {
      axios
        .get(
          `${sip}/admin/user/userlist?page=${this.page}&limit=${this.selectedLimit}${this.query}`
        )
        .then(res => {
          this.users = res.data;
          this.userTotal = res.data.total_user_number;
          this.offset = this.getOffset();
        })
        .catch(error => {
          console.log(error);
        });
    },

    movePage(value) {
      if (value === "plus") {
        if (this.page === this.getTotalPage) {
          event.prevent;
        } else {
          this.page++;
        }
      } else {
        if (this.page === 1) {
          event.prevent;
        } else {
          this.page--;
        }
      }
    },
    getOffset() {
      return (this.page - 1) * this.selectedLimit + 1;
    },
    getDateformat(val) {
      const newDate = new Date(val);
      let month = newDate.getMonth() + 1;
      let date = newDate.getDate();
      if (month < 10) {
        month = `0${month}`;
      }
      if (date < 10) {
        date = `0${date}`;
      }
      return `${newDate.getFullYear()}${month}${date}`;
    },
    resetFilter() {
      this.query = "";
      this.filters.lastAccessFrom = null;
      this.filters.lastAccessTo = null;
      this.filters.createdAtFrom = null;
      this.filters.createdAtTo = null;
      this.filters.userNo = null;
      this.filters.userName = null;
      this.filters.socialNetwork = null;
      this.filters.phoneNumber = null;
      this.filters.email = null;
      if (this.lastAccessFrom) {
        this.lastAccessFrom = null;
      }
      if (this.lastAccessTo) {
        this.lastAccessTo = null;
      }
      if (this.createdAtFrom) {
        this.createdAtFrom = null;
      }
      if (this.createdAtTo) {
        this.createdAtTo = null;
      }
    },
    searchData() {
      for (const key in this.filters) {
        if (this.filters[key]) {
          this.query += `&${key}=${this.filters[key]}`;
        }
      }
      this.page = 1;
      this.selectedLimit = 1;
      this.getUserData();
    }
  },
  computed: {
    getTotalPage() {
      if (Math.ceil(this.userTotal / this.selectedLimit) === 0) {
        return 1;
      }
      return Math.ceil(this.userTotal / this.selectedLimit);
    }
  },
  watch: {
    selectedLimit: {
      handler: function(val, oldvalue) {
        this.page = Math.ceil(this.offset / this.selectedLimit);
        this.getUserData();
      },
      deep: true
    },
    page: {
      handler: function(val, oldvalue) {
        this.getUserData();
      },
      deep: true
    },
    lastAccessFrom(val) {
      if (val) {
        if (this.lastAccessTo) {
          if (this.lastAccessTo < val._d) {
            alert("날짜를 확인해주세요");
            this.lastAccessFrom = null;
          } else {
            this.filters.lastAccessFrom = this.getDateformat(val._d);
          }
        } else {
          this.filters.lastAccessFrom = this.getDateformat(val._d);
        }
      } else {
        this.filters.lastAccessFrom = null;
      }
    },
    lastAccessTo(val) {
      if (val) {
        if (this.lastAccessFrom) {
          if (this.lastAccessFrom > val._d) {
            alert("날짜를 확인해주세요");
            this.lastAccessTo = null;
          } else {
            this.filters.lastAccessTo = this.getDateformat(val._d);
          }
        } else {
          this.filters.lastAccessTo = this.getDateformat(val._d);
        }
      } else {
        this.filters.lastAccessTo = null;
      }
    },
    createdAtFrom(val) {
      if (val) {
        if (this.createdAtTo) {
          if (this.createdAtTo < val._d) {
            alert("날짜를 확인해주세요");
            this.createdAtFrom = null;
          } else {
            this.filters.createdAtFrom = this.getDateformat(val._d);
          }
        } else {
          this.filters.createdAtFrom = this.getDateformat(val._d);
        }
      } else {
        this.filters.createdAtFrom = null;
      }
    },
    createdAtTo(val) {
      console.log(val);
      if (val) {
        if (this.createdAtFrom) {
          if (this.createdAtFrom > val._d) {
            alert("날짜를 확인해주세요");
            this.createdAtTo = null;
          } else {
            this.filters.createdAtTo = this.getDateformat(val._d);
          }
        } else {
          this.filters.createdAtTo = this.getDateformat(val._d);
        }
      } else {
        this.filters.createdAtTo = null;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
header {
  .pageTitle {
    padding: 20px 20px 10px 20px;
    .mainName {
      font-size: 25px;
      font-weight: 300;
      color: rgb(104, 104, 104);
    }
    .subName {
      font-weight: 300;
      color: rgb(116, 116, 116);
      font-size: 14px;
    }
  }
  .pageStateBar {
    font-size: 12.5px;
    padding: 8px 15px;
    background-color: rgb(237, 237, 237);
    ​ i {
      color: rgb(155, 153, 153);
      margin: 0 5px;
    }
  }
}
.pageContents {
  padding: 20px;
  overflow: scroll;

  .userTableContainer {
    min-width: 1780px;
    border: 1px solid lightgray;
    border-radius: 5px;

    .containerTitle {
      border-radius: 5px 0 0 0;
      background-color: rgb(235, 234, 234);
      i {
        color: gray;
        padding: 10px 5px 10px 10px;
      }
    }
    .filterContainer {
      padding: 10px 10px;
      .pageInfo {
        font-size: 13px;

        .prevent {
          color: gray;
        }

        button {
          border: 1px solid lightgray;
          width: 25px;
          height: 30px;
          border-radius: 3px;
        }
        input {
          width: 50px;
          height: 30px;
          border: 1px solid lightgray;
          border-radius: 3px;
          text-align: center;
        }
        select {
          appearance: menulist-button;
          width: 70px;
          height: 30px;
          border: 1px solid lightgray;
          border-radius: 3px;
          padding-left: 10px;
          cursor: pointer;
        }
      }
    }

    table,
    tr,
    td {
      color: black;
      border: 1px solid lightgray;
    }
    table {
      margin-left: 10px;
      border-collapse: collapse;
      text-align: left;
      .headTop {
        background-color: rgb(235, 234, 234);
        font-weight: bold;
        font-size: 14px;
      }
      tbody {
        font-size: 13px;
      }
      .check {
        padding: 13px;
      }
      .userNo {
        padding: 0 10px;
        input {
          height: 30px;
          border: 1px solid lightgray;
          border-radius: 5px;
          width: 60px;
        }
      }
      .userName {
        padding: 0 10px;
        input {
          height: 30px;
          border: 1px solid lightgray;
          border-radius: 5px;
          width: 100px;
        }
      }
      .socialNetwork {
        padding: 0 10px;
        select {
          appearance: menulist-button;
          width: 100px;
          height: 30px;
          border: 1px solid lightgray;
          border-radius: 5px;
          font-size: 13px;
          padding-left: 5px;
          cursor: pointer;
        }
      }
      .phoneNumber {
        padding: 0 10px;
        input {
          border: 1px solid lightgray;
          border-radius: 5px;
          width: 80px;
          height: 30px;
        }
      }
      .email {
        padding: 0 10px;
        input {
          border: 1px solid lightgray;
          border-radius: 5px;
          width: 150px;
          height: 30px;
        }
      }
      .lastAccess,
      .createdAt {
        width: 180;
        padding: 0 10px;
        div {
          margin-bottom: 7px;
          input {
            border-radius: 5px;
            height: 30px;
            border: 1px solid lightgray;
            width: 150px;
          }
        }
      }
      .actions {
        padding: 0 5px;
        button {
          margin: 5px;
          border-radius: 3px;
          padding: 7px;
        }
        .search {
          font-weight: bold;
          display: block;
          color: white;
          font-size: 13px;
          background-color: rgb(248, 174, 35);
          i {
            margin: 2px;
          }
        }
        .reset {
          font-weight: bold;
          display: block;
          color: white;
          font-size: 13px;
          background-color: rgb(242, 60, 57);
          i {
            margin: 2px;
          }
        }
        .detail {
          margin-right: 0;
          padding: 3px;
          font-size: 12px;
          border: 1px solid lightgray;
          height: 25px;
          i {
            margin: 2px;
          }
        }
        .changePW {
          margin-left: 0;
          height: 24px;
          padding: 3px;
          font-weight: bold;
          font-size: 12px;
          color: white;
          background-color: rgb(242, 60, 57);
        }
        .toBrandi {
          background-color: rgb(90, 192, 233);
          color: white;
          font-size: 12px;
          font-weight: bold;
          height: 24px;
          padding: 3px;
          margin-left: 0;
        }
      }
      .event,
      .night {
        width: 150;
        padding: 0 10px;
      }
      .accessOS {
        width: 80;
        padding: 0 10px;
      }
    }
  }
}
</style>