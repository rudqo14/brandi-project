<template>
  <div class="imageRegistration">
    <div class="inputName">
      <div>이미지 등록</div>
      <div class="requiredMark">*</div>
    </div>
    <div class="inputPlace">
      <div class="imageContainer">
        <div class="imgWraaper">
          <div class="imgBox">
            <img src="/Images/no_image.png" alt="img" />
          </div>
          <v-btn normal>
            <span class="firstImgText">*대표 이미지</span>
            선택
          </v-btn>
        </div>
        <div class="imgWraaper">
          <div class="imgBox">
            <img src="/Images/no_image.png" alt="img" />
          </div>
          <v-btn normal>
            이미지
            <span>선택</span>
          </v-btn>
        </div>
        <div class="imgWraaper">
          <div class="imgBox">
            <img src="/Images/no_image.png" alt="img" />
          </div>
          <v-btn normal>
            이미지
            <span>선택</span>
          </v-btn>
        </div>
        <div class="imgWraaper">
          <div class="imgBox">
            <img src="/Images/no_image.png" alt="img" />
          </div>
          <v-btn normal>
            이미지
            <span>선택</span>
          </v-btn>
        </div>
        <div class="imgWraaper">
          <div class="imgBox">
            <img src="/Images/no_image.png" alt="img" />
          </div>
          <v-btn normal>
            이미지
            <span>선택</span>
          </v-btn>
        </div>
      </div>
      <div class="alertText">
        <i class="fas fa-exclamation-triangle"></i> 640 * 720 사이즈 이상 등록 가능하며 확장자는 jpg 만 등록 가능합니다.
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.imageRegistration {
  display: flex;
  height: 300px;
  border-bottom: 1px solid lightgray;

  .inputName {
    display: flex;
    align-items: center;
    width: 302px;
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
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 10px;

    .alertText {
      color: #1e90ff;
      margin: 2px 0;
      font-size: 14px;
      margin-top: 30px;
    }

    .imageContainer {
      display: flex;

      .imgWraaper {
        display: flex;
        flex-direction: column;
        margin-right: 15px;

        .v-btn__content {
          .firstImgText {
            font-size: 15px;
            font-weight: bold;
            color: #1e90ff;
          }
        }
        .imgBox {
          width: 180px;
          height: 180px;

          img {
            width: 100%;
          }
        }
      }
    }
  }
}
</style>
