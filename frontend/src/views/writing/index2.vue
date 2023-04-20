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
              <span style="height: 30px; line-height: 30px; font-size: 18px"
                >智能写作模板</span
              >
              <br />
              <span
                style="
                  height: 30px;
                  line-height: 30px;
                  font-size: 14px;
                  color: #b6b6b6;
                "
                >选择合适的创作类型</span
              >
            </div>
          </div>
        </el-col>
      </el-row>
      <div style="padding:24px">
        <div class="tip">
          模型选择
        </div>
        <el-select v-model="value" class="m-2" placeholder="Select" style="width:100%;margin-bottom:32px">
          <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
        </el-select>
        <div >
          <div class="tip">
          模型选择
        </div>
        <el-select v-model="value" class="m-2" placeholder="Select" style="width:100%;margin-bottom:32px">
          <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
        </el-select>
        <div class="tip">
          提示语句
        </div>
        <el-input v-model="textarea" type="textarea" :disabled="stage" :rows="11" placeholder="" clearable />
        </div>
        <div style="padding-top: 10px; padding-bottom: 10px">
        <el-button type="primary" @click="errorCorrect()" :loading="loading"
          >开始创作</el-button
        >
        <el-button
          type="basic"
          style="margin-left: 24px; margin-top: 16px"
          @click="handleDownload('text-demo')"
          >导出图片</el-button
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
export default {
  data() {
    return {
      activeMenu: "1",
      text: '',
      value: ref(1),
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
      openMDE() {
      this.mde = new SimpleMDE({
        element: this.$refs.textarea,
        spellChecker: false
      })},
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
</style>
