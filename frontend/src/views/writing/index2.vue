<template>
  <div class="container">
    <el-col :span="6"
      class="el-col-left">
      <el-row>
        <el-col :span="24">
          <div
            style="
              display: flex;
              align-items: center;
              background-color: #f8fafc;
              margin-bottom: 12px;
              border-radius: 10px;
            "
          >
            <img
              src="../../../src/assets/img/5.png"
              style="height: 96px; width: 96px"
            />
            <div>
              <span style="height: 30px; line-height: 30px; font-size: 16px"
                >AI写作</span
              >
              <br />
              <span
                style="
                  height: 30px;
                  line-height: 30px;
                  font-size: 14px;
                  color: #b6b6b6;
                "
                >输入提示词生成AI文案</span
              >
            </div>
          </div>
        </el-col>
      </el-row>
      <div style="padding:24px">
        <div class="tip">
          创作模板选择
        </div>
        <el-select v-model="value" class="m-2" placeholder="Select" style="width:100%;margin-bottom:32px">
          <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
        </el-select>
        <div >
          <div class="tip">
          项目名称
        </div>
        <el-select v-model="value" class="m-2" placeholder="Select" style="width:100%;margin-bottom:32px">
          <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
        </el-select>
        <div class="tip">
          提示语句
        </div>
        <el-input v-model="textarea" type="textarea" :disabled="stage" :rows="11" placeholder="" clearable />
        </div>
        <div style="padding-top: 10px; padding-bottom: 10px;width:100%">
        <el-button
          type="basic"
          style="margin-top: 16px;width:36%"
          @click="handleDownload('text-demo')"
          >返回首页</el-button
        >
        <el-button type="primary" @click="errorCorrect()" :loading="loading" style="width: 60%;"
          ><i class="el-icon-edit" style="margin-right:12px;"></i>开始创作</el-button
        >
      </div>
      </div>
    </el-col>
    <el-col
      :span="18"
      style="border-left: 1px solid #e6e6e6; background-color: #f8fafc; z-index: -1;"
      class="el-col-right"
    >
    <div style="margin:24px;height:90%">
       <v-md-editor v-model="text" height="100%" ></v-md-editor>
    </div>
    
    </el-col>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from "axios";
export default {
  props: ['cardId'], // 接收 cardId 作为 props
  data() {
    return {
      activeMenu: "1",
      textarea: "",
      text: "",
      loading:false,
      value: ref(1),
      input: "",
      result: "",
      stage: false,
      visible: false,
      result: "",
      options: [
        {
          value: 1,
          label: '日报/周报/月报',
        },
        {
          value: 2,
          label: '调研报告',
        }
      ],
      cards: [
        {
          id: 1,
          title: "日报/周报/月报",
          description: "根据工作内容生成日报/周报/月报",
        },
        {
          id: 2,
          icon: "el-icon-s-help",
          title: "卡片二",
          description: "这是第二个卡片的说明文字。",
        },
        {
          id: 3,
          icon: "el-icon-s-help",
          title: "卡片二",
          description: "这是第二个卡片的说明文字。",
        },
        {
          id: 4,
          icon: "el-icon-s-help",
          title: "卡片二",
          description: "这是第二个卡片的说明文字。",
        },
        {
          id: 5,
          icon: "el-icon-s-help",
          title: "卡片二",
          description: "这是第二个卡片的说明文字。",
        },
        {
          id: 6,
          icon: "el-icon-s-help",
          title: "卡片二",
          description: "这是第二个卡片的说明文字。",
        },
      ],
    };
  },
  methods: {
    errorCorrect() {
      var that = this;
      that.loading = true;
      var key = that.textarea;
      console.log(key)
      if (key === "") {
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
            text: that.textarea, 
            key: that.textarea

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

  
    handleMenuSelect(index) {
      this.activeMenu = index;
      if (index === "1") {
        this.cards = [
          {
            id: 1,
            title: "日报/周报/月报",
            description: "根据工作内容生成日报/周报/月报",
          },
        ];
      } else if (index === "2") {
        this.cards = [
          {
            id: 2,
            icon: "el-icon-s-help",
            title: "卡片二",
            description: "这是第二个卡片的说明文字。",
          },
        ];
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
  border-color: #1e90ff; /* 添加边框颜色以使其更加突出 */
}

/* 更改鼠标悬停颜色 */
.el-button--primary:hover {
  background: linear-gradient(to right, #00bfff, #1e90ff);
  border-color: #00bfff;
  filter: brightness(110%); /* 使颜色减淡 50% */
}

</style>