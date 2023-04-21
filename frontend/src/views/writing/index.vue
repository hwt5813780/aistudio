<template>
  <div class="container">
    <el-col :span="5">
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
      <div class="menu-container">
        <el-menu
          class="menu"
          :default-active="activeMenu"
          @select="handleMenuSelect"
          text-color="#B2B2B2"
          active-text-color="#131344"
        >
          <el-menu-item
            index="0"
            class="selected-menu"
            style="margin-bottom: 6px"
          >
            <span class="menu-text">最近常用</span>
          </el-menu-item>
          <el-menu-item
            index="1"
            class="selected-menu"
            style="margin-bottom: 6px"
          >
            <span class="menu-text"
              ><i class="el-icon-s-order"></i>报告写作</span
            >
          </el-menu-item>
          <el-menu-item
            index="2"
            class="selected-menu"
            style="margin-bottom: 6px"
          >
            <span class="menu-text"
              ><i class="el-icon-platform-eleme"></i>社媒写作</span
            >
          </el-menu-item>
          <el-menu-item
            index="3"
            class="selected-menu"
            style="margin-bottom: 6px"
          >
            <span class="menu-text"
              ><i class="el-icon-s-custom"></i>教育（论文）</span
            >
          </el-menu-item>
          <el-menu-item
            index="4"
            class="selected-menu"
            style="margin-bottom: 6px"
          >
            <span class="menu-text"><i class="el-icon-s-comment"></i>电商</span>
          </el-menu-item>
          <el-menu-item
            index="5"
            class="selected-menu"
            style="margin-bottom: 6px"
          >
            <span class="menu-text"
              ><i class="el-icon-s-marketing"></i>营销广告</span
            >
          </el-menu-item>
          <el-menu-item
            index="6"
            class="selected-menu"
            style="margin-bottom: 6px"
          >
            <span class="menu-text"
              ><i class="el-icon-s-management"></i>文学</span
            >
          </el-menu-item>
          <el-menu-item
            index="7"
            class="selected-menu"
            style="margin-bottom: 6px"
          >
            <span class="menu-text"
              ><i class="el-icon-camera-solid"></i>短视频文案</span
            >
          </el-menu-item>
        </el-menu>
      </div>
    </el-col>
    <el-col
      :span="19"
      style="border-left: 1px solid #e6e6e6; background-color: #f8fafc"
      class="el-col-right"
    >
      <div class="card-container">
        <el-card
          class="card"
          v-for="card in cards"
          :key="card.id"
          style="margin-top: 24px; margin-left: 24px; width: 302px"
          @click.native="$router.push({ name: 'CardDetail' })"
          :body-style="{ padding: '0px' }"
        >
          <img :src="require(card.img)" style="height: 202px" />
          <div
            style="
              padding-top: 24px;
              padding-left: 24px;
              padding-right: 24px;
              padding-bottom: 16px;
            "
          >
            <span>{{ card.title }}</span>
            <p style="color: #999; font-size: 14px">{{ card.description }}</p>
          </div>
        </el-card>
      </div>
    </el-col>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeMenu: "1",
      cards: [
        {
          id: 1,
          title: "PDCA研发版",
          description: "提示工作内容自动生成PDCA",
          img: "../../../src/assets/img/pdca.png",
        },
        {
          id: 2,
          icon: "el-icon-s-help",
          title: "卡片二",
          description: "这是第二个卡片的说明文字。",
          img: "../../../src/assets/img/pdca.png",
        },
        {
          id: 3,
          icon: "el-icon-s-help",
          title: "卡片二",
          description: "这是第二个卡片的说明文字。",
          img: "../../../src/assets/img/pdca.png",
        },
        {
          id: 4,
          icon: "el-icon-s-help",
          title: "卡片二",
          description: "这是第二个卡片的说明文字。",
          img: "../../../src/assets/img/pdca.png",
        },
        {
          id: 5,
          icon: "el-icon-s-help",
          title: "卡片二",
          description: "这是第二个卡片的说明文字。",
          img: "../../../src/assets/img/pdca.png",
        },
        {
          id: 6,
          icon: "el-icon-s-help",
          title: "卡片二",
          description: "这是第二个卡片的说明文字。",
          img: "../../../src/assets/img/pdca.png",
        },
      ],
    };
  },
  methods: {
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
  box-shadow: 0px 12px 30px rgba(19, 31, 61, 0.2);
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
</style>
