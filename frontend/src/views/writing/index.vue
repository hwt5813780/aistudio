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
            <img src="@/assets/img/5.png" style="height: 96px; width: 96px" />
            <div>
              <span style="height: 30px; line-height: 30px; font-size: 16px"
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
            <span class="menu-text">全部模板</span>
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
          class="card2"
          v-for="card in filteredCards"
          :key="card.id"
          style="margin-top: 24px; margin-left: 24px; width: 256px"
          @click.native="goToCardDetail(card.id)"
          :body-style="{ padding: '0px' }"
        >
          <img
            :src="card.img"
            style="height: 156px; object-fit: cover; width: 100%"
          />
          <div
            style="
              padding-top: 12px;
              padding-left: 16px;
              padding-right: 16px;
              padding-bottom: 6px;
              font-size: 14px;
            "
          >
            <span style="color: #000; font-size: 14px">{{ card.title }}</span>
            <p style="color: #9999; font-size: 14px">{{ card.description }}</p>
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
      activeMenu: "0",
      cards: [
        {
          id: 1,
          title: "PDCA研发版",
          description: "提示工作内容自动生成PDCA",
          img: require("@/assets/img/pdca.png"),
        },
        {
          id: 2,
          icon: "el-icon-s-help",
          title: "团建新闻稿",
          description: "自动生成团建活动的新闻稿件",
          img: require("@/assets/img/actreport.png"),
        },
        {
          id: 3,
          icon: "el-icon-s-help",
          title: "健康报告",
          description: "通过数据指标生成健康报告",
          img: require("@/assets/img/invest.png"),
        },
        {
          id: 4,
          icon: "el-icon-s-help",
          title: "AI算命",
          description: "人工智能的科学算命方法",
          img: require("@/assets/img/fortune.jpg"),
        },
        {
          id: 5,
          icon: "el-icon-s-help",
          title: "产品介绍",
          description: "根据提示编写产品的介绍文案",
          img: require("@/assets/img/productintro.png"),
        },
        {
          id: 6,
          icon: "el-icon-s-help",
          title: "营销文案",
          description: "输入产品的提示智能生成营销文案",
          img: require("@/assets/img/marketing.jpg"),
        },
      ],
      selectedIds: [1, 2, 3, 4, 5, 6], // 选择的id数组，用来进行筛选
    };
  },
  methods: {
    goToCardDetail(cardId) {
      if (cardId === 1 || cardId === 2 || cardId === 3) {
        this.$router.push({ name: "CardDetail", params: { cardId: cardId } });
      } else {
        this.$message({
          message: "当前的模板暂未开放",
          type: "warning",
        });
      }
    },

    handleMenuSelect(index) {
      this.activeMenu = index;
      if (index === "0") {
        this.selectedIds = [1, 2, 3, 4, 5, 6];
      } else if (index === "1") {
        this.selectedIds = [1, 2];
      } else if (index === "2") {
        this.selectedIds = [4, 6];
      } else if (index === "3") {
        this.selectedIds = [];
      } else if (index === "4") {
        this.selectedIds = [6];
      } else if (index === "5") {
        this.selectedIds = [6];
      } else if (index === "6") {
        this.selectedIds = [6];
      } else if (index === "7") {
        this.selectedIds = [6];
      }
    },
  },
  computed: {
    filteredCards() {
      // 使用filter方法筛选cards数组
      return this.cards.filter((card) => this.selectedIds.includes(card.id));
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

.card2 {
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.card2:hover {
  box-shadow: 0px 12px 30px rgba(6, 15, 36, 0.2);
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
