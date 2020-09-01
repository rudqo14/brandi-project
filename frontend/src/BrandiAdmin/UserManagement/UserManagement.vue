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
        <div class="filterContainer">
          <div class="pageInfo">
            <span>Page</span>
            <button><</button>
            <input :value="page" />
            <button @click="movePage">></button>
            <span>of {{ page }} | View</span>
            <select name="selectedLimit">
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
                <input />
              </td>
              <td class="userName">
                <input />
              </td>
              <td class="socialNetwork">
                <select>
                  <option>Select...</option>
                  <option value="브랜디">브랜디</option>
                  <option value="구글">구글</option>
                </select>
              </td>
              <td class="phoneNumber">
                <input />
              </td>
              <td class="email">
                <input />
              </td>
              <td class="event"></td>
              <td class="accessOS"></td>
              <td class="lastAccess">
                <div>
                  <input type="date" value />
                </div>
                <div>
                  <input type="date" value />
                </div>
              </td>
              <td class="createdAt">
                <div>
                  <input type="date" placeholder="From" />
                </div>
                <div>
                  <input type="date" placeholder="To" />
                </div>
              </td>
              <td class="actions">
                <button class="search">
                  <i class="fas fa-search"></i>Search
                </button>
                <button class="reset">
                  <i class="fas fa-times"></i>Reset
                </button>
              </td>
            </tr>
          </thead>
          <tbody>
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
        </table>
        <div class="filterContainer">
          <div class="pageInfo">
            <span>Page</span>
            <button><</button>
            <input :value="page" />
            <button>></button>
            <span>of {{ page }} | View</span>
            <select name="page">
              <option value="1">1</option>
              <option value="2">2</option>
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
      users: [],
      page: 1,
      userTotal: 0,
      filters: ""
    };
  },
  methods: {
    getUserData() {
      axios
        .get(`${sip}/admin/user/userlist?page=1&limit=10`)
        .then(res => {
          this.users = res.data;
          this.userTotal = res.data.total_user_number;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getTotalPage() {
      return;
    },
    movePage() {
      console.log(selectedLimit);
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
  .userTableContainer {
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