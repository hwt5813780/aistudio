<template>
  <div class="home">
    <div class="header" style="position: relative">
      <video
        class="module-other-meet-banner-video-loop muted"
        style="height: 428px"
        playsinline=""
        autoplay=""
        loop=""
        muted=""
        src="@/assets/video/dashboard.mp4"
      ></video>
      <h1
        class="title"
        style="
          position: absolute;
          top: 28%;
          left: 32.8%;
          transform: translate(-50%, -50%);
          font-size: 36px;
        "
      >
        美络 AI-Studio
      </h1>
      <p
        class="description"
        style="
          position: absolute;
          top: 44%;
          left: 36.7%;
          transform: translate(-50%, -50%);
          font-size: 18px;
          color: #666;
        "
      >
        轻量人工智能工具包 集成OpenAI的API的选择器项
      </p>
      <el-button
        type="primary"
        class="bannerbutton"
        @click.native="goToOtherPage"
        :loading="loading"
        style="
          position: absolute;
          top: 64%;
          left: 30.4%;
          transform: translate(-50%, -50%);
          font-size: 14px;
          color: white;
        "
        ><i class="el-icon-edit" style="margin-right: 12px"></i
        >开始创作</el-button
      >
    </div>

    <div class="content">
      <el-card class="card" @click="goToPage1">
        <div class="card-image">
          <img src="@/assets/img/4.png" alt="Image 1" />
        </div>
        <div class="card-body" style="text-align: center">
          <div style="margin-bottom: 24px; font-weight: bold">图片信息提取</div>
          <el-button text style="width: 100%" class="button" @click="goToPage2"
            >开始使用</el-button
          >
        </div>
      </el-card>
      <el-card class="card" @click="goToPage2">
        <div class="card-image">
          <img src="@/assets/img/2.png" alt="Image 2" />
        </div>
        <div class="card-body" style="text-align: center">
          <div style="margin-bottom: 24px; font-weight: bold">文本信息提取</div>
          <el-button text style="width: 100%" class="button" @click="goToPage1"
            >开始使用</el-button
          >
        </div>
      </el-card>
      <el-card class="card" @click="goToPage3">
        <div class="card-image">
          <img src="@/assets/img/3.png" alt="Image 2" />
        </div>
        <div class="card-body" style="text-align: center">
          <div style="margin-bottom: 24px; font-weight: bold">文档信息提取</div>
          <el-button text style="width: 100%" class="button" @click="goToPage1"
            >开始使用</el-button
          >
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToPage1() {
      this.$router.push({ name: "Onlinecsc" });
    },
    goToPage2() {
      this.$router.push({ name: "Imagecsc" });
    },
    goToPage3() {
      this.$router.push({ name: "Documentcsc" });
    },
    goToOtherPage() {
      this.$router.push({ name: "AIwt" });
    },
  },
};
</script>

<style>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0;
}

.header {
  text-align: center;
  margin-bottom: 30px;
}

.title {
  font-size: 24px;
  font-weight: normal;
}

.description {
  font-size: 14px;
}

.content {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.card {
  width: 300px;
  margin: 20px;
}

.card-image {
  height: 200px;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-body {
  padding: 20px;
}

.card-body p {
  font-size: 14px;
}
/* 设置渐变色背景 */
.bannerbutton {
  background: linear-gradient(to right, #00bfff, #1e90ff);
  border-color: #5daeff; /* 添加边框颜色以使其更加突出 */
}

/* 更改鼠标悬停颜色 */
.bannerbutton:hover {
  background: linear-gradient(to right, #00bfff, #1e90ff);
  border-color: #00bfff;
  filter: brightness(110%); /* 使颜色减淡 10% */
}
</style>
