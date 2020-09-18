<template>
  <div>
    <div class="detailContainer">
      <div class="detailitle">주문상세조회</div>
      <div class="orderInformationContainer">
        <div class="orderInformation">주문 정보</div>
        <div class="informationContainer">
          <div class="orderNo">
            <div>주문번호</div>
            <div>{{ data.order_detail_no }}</div>
          </div>
          <div class="orderDate">
            <div>주문일자</div>
            <div>{{ data.order_date }}</div>
          </div>
          <div class="orderer">
            <div>주문자</div>
            <div>{{ data.orderer }}</div>
          </div>
          <div class="totalPrice">
            <div>결제금액</div>
            <div>{{ getTotalPrice() }}</div>
          </div>
        </div>
        <div class="orderProductContainer">
          <div class="orderTitle">주문상품</div>
          <div class="productContainer">
            <div class="cellerInfo">판매자 배송 상품</div>
            <div class="containerTop">
              <div class="cellerName">브랜디</div>
              <div class="orderPrice">주문금액</div>
              <div class="orderStatus">진행상황</div>
            </div>
            <div class="containerBottom">
              <div class="imgContainer">
                <img :src="data.image_small" alt="small_image" />
              </div>
              <div class="productInformation">
                <div class="productName">{{ data.product_name }}</div>
                <div class="productOption">{{ data.color }}/{{ productSize }}</div>
                <div class="orderQuantity">{{ data.quantity }}</div>
              </div>
              <div class="orderPrice">{{ getTotalPrice() }} 원</div>
              <div class="orderStatus">{{ data.order_status }}</div>
            </div>
          </div>
        </div>
      </div>
      <div class="paymentContainer">
        <div class="containerTop">결제정보</div>
        <div class="paymentInformation">
          <div class="payment">
            <div class="informationTitle">결제수단</div>
            <div class="information">신용카드</div>
          </div>
          <div class="totlaPrice">
            <div class="inforamtionTitle">총 상품금액</div>
            <div class="information">{{ getTotalPrice() }}</div>
          </div>
          <div class="couponPrice">
            <div class="informationTitle">쿠폰 할인 금액</div>
            <div class="information">0 원</div>
          </div>
          <div class="pointPrice">
            <div class="informationTitle">총 사용 포인트</div>
            <div class="information">0 원</div>
          </div>
          <div class="shippingPrice">
            <div class="informationTitle">배송비</div>
            <div class="information">0 원</div>
          </div>
          <div :class="['TotalPrice', 'shippingPrice']">
            <div class="informationTitle">총 주문금액</div>
            <div class="information">{{ getTotalPrice() }}</div>
          </div>
        </div>
      </div>
      <div class="shippingContainer">
        <div class="containerTop">배송지 정보</div>
        <div class="shippingInformation">
          <div class="receiver">
            <div class="informationTitle">수령인</div>
            <div class="informtaion">{{ data.receiver }}</div>
          </div>
          <div class="phoneNumber">
            <div class="informationTitle">휴대폰</div>
            <div class="information">{{ data.phone_number }}</div>
          </div>
          <div class="zipCode">
            <div class="informationTitle">우편번호</div>
            <div class="information">{{ data.zip_code }}</div>
          </div>
          <div class="address">
            <div class="informationTitle">주소</div>
            <div class="information">{{ data.address }}</div>
          </div>
          <div class="additionalAddress">
            <div class="informationTitle">나머지주소</div>
            <div class="information">{{ data.additional_address }}</div>
          </div>
          <div class="deliveryRequest">
            <div class="informationTitle">배송메모</div>
            <div class="information">{{ data.delivery_request }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { sip } from "../../../config"

export default {
    created() {
        getData()
    },
    data() {
        return {
            data: []
        }
    },
    methods: {
        getData(){
            axios.get(`${sip}/user/mypage/orderdetail/${}`, {headers: {Authorization: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX25vIjp7InVzZXJfbm8iOjF9fQ.uAYYPkfZVs1cyXezJ_MVCp4fzgYPjQGhRLn83bIxrH8"}}).then(res => {this.data = res.data;})
        }
    }
};
</script>

<style>
</style>