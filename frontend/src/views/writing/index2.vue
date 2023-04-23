<template>
  <div class="container">
    <el-col :span="6" class="el-col-left">
      <el-row>
        <el-col :span="24">
          <div style="
              display: flex;
              align-items: center;
              background-color: #f8fafc;
              margin-bottom: 12px;
              border-radius: 10px;
            ">

            <img src="@/assets/img/5.png" style="height: 96px; width: 96px" />
            <div>
              <span style="height: 30px; line-height: 30px; font-size: 16px">AI写作</span>
              <br />
              <span style="
                  height: 30px;
                  line-height: 30px;
                  font-size: 14px;
                  color: #b6b6b6;
                ">输入提示词生成AI文案</span>
            </div>

          </div>
        </el-col>
      </el-row>
      <div style="padding:24px">
        <div class="tip">
          创作模板选择
        </div>
        <el-select v-model="value" class="m-2" placeholder="Select" style="width:100%;margin-bottom:32px">
          <el-option v-for="item in options0" :key="item.value" :disabled="item.disabled" :label="item.label"
            :value="item.value" @click="handleOptionClick1(item.value)" />
        </el-select>
        <div>
          <div class="tip" v-if="value === 1">
            项目名称
          </div>
          <el-select v-model="value1" v-if="value === 1" class="m-2" placeholder="Select"
            style="width:100%;margin-bottom:32px">
            <el-option v-for="item in options1" :key="item.value1" :label="item.label" :value="item.value1"
              @click="handleOptionClick3(item.label)" />
          </el-select>
          <div class="tip" v-if="value === 2">
            团建主题
          </div>
          <el-input v-model="input" v-if="value === 2" type="input" :disabled="stage" :rows="11" placeholder=""
            style="width:100%;margin-bottom:32px" clearable />
          <div class="tip">
            {{ contenttip }}
          </div>
          <el-input v-model="textarea" type="textarea" :disabled="stage" :rows="11" placeholder="" clearable />
        </div>
        <div style="padding-top: 10px; padding-bottom: 10px;width:100%">
          <el-button type="basic" style="margin-top: 16px;width:36%" @click="handleback()">返回首页</el-button>
          <el-button type="primary" @click="errorCorrect()" :loading="loading" style="width: 60%;"><i class="el-icon-edit"
              style="margin-right:12px;"></i>开始创作</el-button>
        </div>
      </div>
    </el-col>
    <el-col :span="18" style="border-left: 1px solid #e6e6e6; background-color: #f8fafc; z-index: -1;"
      class="el-col-right">
      <div v-loading="loading" element-loading-background="#666" style="margin:24px;height:95%">
        <v-md-editor v-model="text" height="100%"></v-md-editor>
      </div>

    </el-col>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from "axios";
export default {
  computed: {
    contenttip() {
      // 根据value属性的值返回一个新的字符串
      switch (this.value) {
        case 1:
          this.input = "RPA自动化用工技术研究";
          return '工作概况';
        case 2:
          this.input = "";
          return '提示信息';
        case 3:
          this.input = "";
          return '调研方向';
        default:
          return '';
      }
    },

  },
  props: ['cardId'], // 接收 cardId 作为 props
  data() {
    return {
      vueValue: process.env.VUE_APP_VARIABLE,
      activeMenu: "1",
      textarea: "",
      text: "",
      loading: false,
      value: ref(1),
      value1: ref(1),
      input: "",
      result: "",
      stage: false,
      visible: false,
      result: "",
      options0: [
        {
          value: 1,
          label: 'PDCA研发版',
          contenttip: '工作概况'
        },
        {
          value: 2,
          label: '团建新闻稿',
          contenttip: '提示信息'
        },
        {
          value: 3,
          label: '竞品调研',
          contenttip: '调研方向'
        },
        {
          value: 4,
          label: 'AI算命',
          disabled: true
        },
        {
          value: 5,
          label: '产品介绍',
          disabled: true
        },
        {
          value: 6,
          label: '营销文案',
          disabled: true
        },
      ],
      options1: [
        {
          value1: 1,
          label: 'RPA自动化用工技术研究',
        },
        {
          value1: 2,
          label: '文件服务',
        },
      ],
    };
  },
  methods: {
    handleback() {
      this.$router.push({ name: 'Wt' });
    },
    handleOptionClick3(label) {
      // 在选项点击后将label的值赋给input
      this.input = label;
    },
    errorCorrect() {
      var that = this;
      that.loading = true;
      var textarea = that.textarea;
      var value = that.value;
      var input = that.input;
      console.log(textarea)
      console.log(value)
      console.log(input)
      if (textarea === "" || (value === 2 && input === "")) {
        this.$message({
          showClose: true,
          message: "输入内容不能为空",
          type: "warning",
        });
        that.result = "";
      } else {
        // 请求后端API服务，请求方法为post，请求体字段为json格式 text
        axios
          .post("http://127.0.0.1:8000/api/gpt/pdca", {
            value: that.value,
            input: that.input,
            textarea: that.textarea
          })
          .then((response) => {
            console.log(response);
            that.text = response.data.correctionResults;
            console.log(that.imageUrl);
            that.visible = true;
            that.loading = false;
            that.$message({
              showClose: true,
              message: "Success！",
              type: "success",
            });
          })
          .catch((error) => {
            console.log(error);
            that.result = "";
            that.visible = false;
            that.$message({
              showClose: true,
              message: "请求出现异常！",
              type: "error",
            });
          });
      }
    },
  },
};
</script>

<style>
.menu {
  height: 100%;
  border-right: none;
  border-radius: 10px;
  width: 90%;
}

.selected-menu {
  border-radius: 6px;
  font-size: 14px;
  height: 44px;
}

.menu-container {
  display: flex;
  justify-content: center;
}

.menu-text {
  display: flex;
  align-items: center;
  line-height: 44px;
}

.card {
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.card:hover {
  box-shadow: 0px 12px 30px rgba(88, 106, 148, 0.2);
  cursor: pointer;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
}

.container {
  height: 100vh;
  position: relative;
}

.container::before {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 1px;
  background-color: #e6e6e6;
  opacity: 0.5;
  z-index: -1;
}

.el-col-right {
  height: 100%;
  border-left: 1px solid #e6e6e6;
}

.el-col-right .card {
  margin-left: 24px;
}

.el-menu-item {
  color: #777f8f;
}

.el-menu-item.is-active {
  color: #6681fa;
  background-color: #eaeeff;
}

.tip {
  font-family: PingFang SC, Helvetica Neue, Arial, Helvetica, sans-serif;
  font-size: 14px;
  font-weight: normal;
  margin-bottom: 20px;
}

/* 设置渐变色背景 */
.el-button--primary {
  background: linear-gradient(to right, #00bfff, #1e90ff);
  border-color: #5aadff;
  /* 添加边框颜色以使其更加突出 */
}

/* 更改鼠标悬停颜色 */
.el-button--primary:hover {
  background: linear-gradient(to right, #00bfff, #1e90ff);
  border-color: #00bfff;
  filter: brightness(110%);
  /* 使颜色减淡 50% */
}
</style>