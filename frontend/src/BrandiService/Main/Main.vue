<template>
  <div>
    <Header />
    <!-- <Banner /> -->
    <main>
      <div class="mainProducts">
        <section class="productContainer">
          <div class="productTitle">
            <h1>
              <span class="mainTitle">브랜디는 하루배송</span>
              <span class="subTitle">오늘 사고 내일 바로 입자!</span>
            </h1>
          </div>
          <article class="productList">
            <div class="product" v-for="product in product.data" v-bind:key="product.product_id">
              <div class="productImage" @click="linkToDetail">
                <img :src="product.thumbnail_image" alt="jpg" />
              </div>
              <div class="productName">{{ product.product_name }}</div>
              <div class="productPrice">
                <span class="discountRate">{{ product.discount_rate }}%</span>
                <span class="price">
                  {{
                  numberWithCommas(Math.floor(product.price))
                  }}
                </span>
                <span class="discountPrice">
                  {{
                  numberWithCommas(
                  parseInt(product.price) *
                  ((100 - product.discount_rate) / 100)
                  )
                  }}
                </span>
              </div>
            </div>
          </article>
        </section>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import Header from "../Components/Header";
import Banner from "../Components/Banner";
import Footer from "../Components/Footer";

export default {
  components: {
    Header,
    Banner,
  },
  created() {
    this.getProductData();
  },
  data() {
    return {
      product: [],
    };
  },
  methods: {
    getProductData() {
      axios.get("http://10.58.3.90:5000/product").then((res) => {
        this.product = res.data;
      });
    },
    numberWithCommas(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    linkToDetail() {
      this.$router.push("/detail");
    },
  },
};
</script>

<style lang="scss" scoped>
main {
  display: flex;
  justify-content: center;

  .mainProducts {
    max-width: 1275px;

    .productContainer {
      display: flex;
      flex-direction: column;

      .productTitle {
        margin-top: 100px;
        margin-bottom: 15px;

        .mainTitle {
          font-size: 26px;
          font-weight: bold;
        }

        .subTitle {
          font-size: 20px;
          margin-left: 5px;
          color: #4a4a4a;
        }
      }

      .productList {
        .product {
          display: inline-block;
          width: 255px;
          padding: 0 0.5% 30px 0.5%;

          .productImage {
            height: 254px;
            cursor: pointer;

            img {
              width: 100%;
              height: 100%;
            }
          }

          .productName {
            margin-top: 15px;
            font-size: 16px;
            font-weight: 500;
            text-overflow: ellipsis;
            overflow: hidden;
            white-space: nowrap;
          }

          .productPrice {
            margin-top: 5px;

            .discountRate {
              font-size: 20px;
              font-weight: 600;
              padding-right: 6px;
              color: #ff204b;
            }

            .price {
              font-size: 20px;
              font-weight: 600;
              padding-right: 6px;
            }

            .discountPrice {
              font-size: 15px;
              color: #757575;
              text-decoration: line-through;
            }
          }
        }
      }
    }
  }
}
</style>
