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
        <ckeditor
          :editor="editor"
          v-model="editorData"
          :config="editorConfig"
        ></ckeditor>
        <!-- <Editor height="500px" @input="inputEdiorText" />
        <Viewer /> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapMutations } from "vuex";
import "codemirror/lib/codemirror.css";
import "@toast-ui/editor/dist/toastui-editor.css";
import { Editor, Viewer } from "@toast-ui/vue-editor";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import CKEditor from "@ckeditor/ckeditor5-vue";

const AdminStore = "adminStore";

export default {
  components: {
    ckeditor: CKEditor.component,
    Editor,
    Viewer,
  },

  data() {
    return {
      defaultValue: "에디터사용",
      editor: ClassicEditor,
      editorData: "<p>Content of the editor.</p>",
      editorConfig: {
        // The configuration of the editor.
      },
    };
  },

  methods: {
    ...mapMutations(AdminStore, ["detailInformation"]),

    inputEdiorText(e) {
      this.detailInformation(e.target.value);
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
