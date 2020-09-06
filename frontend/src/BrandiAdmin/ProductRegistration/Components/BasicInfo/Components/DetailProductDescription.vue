<template>
  <div class="detailProductDescription">
    <div class="inputName">
      <div>상세 상품 정보</div>
      <div class="requiredMark">*</div>
    </div>
    <div class="inputPlace">
      <div class="radioContainer">
        <v-radio-group v-model="defaultValue" row>
          <v-radio label="간편 업로드" value="radio-1"></v-radio>
          <v-radio label="에디터 사용 (html 가능)" value="에디터사용"></v-radio>
        </v-radio-group>
        <div>
          ( 에디터에 따라 상세 내용 화면에 다소 차이가 있을 수 있습니다.)
        </div>
      </div>
      <div class="alertText">
        <i class="fas fa-exclamation-triangle"></i> 미판매 선택시 앱에서 Sold
        Out으로 표시 됩니다.
      </div>
      <div class="imageInputBtn">
        <v-btn normal>
          <i class="far fa-image"></i>
          <span>사진 삽입</span>
        </v-btn>
        <span class="inputImageCheckMessage"
          >이미지 확장자는 JPG, PNG만 등록 가능합니다.</span
        >
      </div>
      <div class="editorContainer">
        <ckeditor @input="upDateDetailInformation" :config="editorConfig"
          ><text-area></text-area
        ></ckeditor>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapMutations, mapState } from "vuex";
import "codemirror/lib/codemirror.css";
import CKEditor from "ckeditor4-vue";
import { ADMIN_API_URL } from "../../../../../../config";

const AdminStore = "adminStore";

export default {
  components: {
    ckeditor: CKEditor.component,
  },

  data() {
    return {
      defaultValue: "에디터사용",
      editorData: "<p>Content of the editor.</p>",
      editorConfig: {
        height: 430,
        toolbarGroups: [
          { name: "styles" },
          { name: "colors" },
          { name: "basicstyles" },
          { name: "insert" },
          { name: "tools" },
          { name: "align" },
        ],
        colorButton: "colors",

        extraPlugins: "font,colorbutton,justify",
        filebrowserImageUploadUrl: `${ADMIN_API_URL}/admin/product/detail-image`,

        // filebrowserBrowseUrl: "/apps/ckfinder/3.4.5/ckfinder.html",
        //filebrowserImageBrowseUrl:
        //  "https://brandi-project.s3.ap-northeast-2.amazonaws.com/detail_2020_9_4_1599205694",

        //  filebrowserUploadUrl : String
        //  파일 업로드를 처리하는 스크립트의 위치 설정하면 업로드 탭이 링크 , 이미지 및 플래시 대화 상자 창에 나타남
        //filebrowserUploadUrl:
        //  "https://brandi-project.s3.ap-northeast-2.amazonaws.com/detail_2020_9_4_1599205694",
        // uploadUrl:
        //   "/apps/ckfinder/3.4.5/core/connector/php/connector.php?command=QuickUpload&type=Files&responseType=json",
      },
    };
  },
  methods: {
    ...mapMutations(AdminStore, ["upDateDetailInformation"]),

    inputEdiorText(e) {
      this.upDateDetailInformation(e.target.value);
    },
  },
};
</script>

<style lang="scss" scoped>
.detailProductDescription {
  display: flex;
  height: 700px;
  border-bottom: 1px solid lightgray;

  .inputName {
    display: flex;
    align-items: center;
    width: 306px;
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
    margin: 0 20px;

    .radioContainer {
      display: flex;
      align-items: center;
    }

    .alertText {
      padding-bottom: 20px;
      border-bottom: 1px solid lightgray;
      color: #1e90ff;
      font-size: 14px;
    }

    .imageInputBtn {
      margin-top: 20px;

      .v-btn {
        margin-right: 10px;
        font-size: 15px;

        .far {
          font-size: 20px;
        }

        span {
          font-size: 16px;
        }
      }

      .inputImageCheckMessage {
        color: red;
        font-weight: bold;
        font-size: 14px;
      }
    }

    .editorContainer {
      margin-top: 20px;
    }
  }
}
</style>
