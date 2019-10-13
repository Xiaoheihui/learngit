<template>
    <div class="bbsDetail">
      <site-header></site-header>
      <div class="body">
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
          <el-menu-item index="0" @click="gotoIndex">平台首页</el-menu-item>
          <el-menu-item index="1" @click="gotoClassInfo('1')">科技创新</el-menu-item>
          <el-menu-item index="2" @click="gotoClassInfo('2')">创业商业</el-menu-item>
          <el-menu-item index="3" @click="gotoClassInfo('3')">艺术爱好</el-menu-item>
          <el-menu-item index="4" @click="gotoClassInfo('4')">游戏动漫</el-menu-item>
          <el-menu-item index="5" @click="gotoClassInfo('5')">广告公益</el-menu-item>
          <el-menu-item index="6" @click="gotoClassInfo('6')">学科竞赛</el-menu-item>
          <el-menu-item index="7" @click="gotoClassInfo('7')">体育竞赛</el-menu-item>
          <el-menu-item index="8" @click="gotoCommunity">社区论坛</el-menu-item>
        </el-menu>
      </div>
    </div>
</template>

<script>
  import siteHeader from './siteHeader'
    export default {
      name: "bbsDetail",
      components:{siteHeader},
      data(){
        return{
          activeIndex:'8'
        }
      },
      methods:{
        gotoClassInfo(classNum){
          // this.activeIndex = classNum
          this.$router.push({path:'/classInfo', query:{classNum:classNum}})
          // this.$router.go(0)
        },
        gotoIndex(){
          this.$router.push({name:'index'})
        },
        handleSelect(key, keyPath) {
          // console.log(key, keyPath);
        },
        gotoCommunity(){
          this.$router.push({name:'community'})
        },
      }
    }
</script>

<style lang="scss">
.bbsDetail{
  .body {
    width: 100%;
    margin: 0;
    padding: 0;

    .el-menu {
      position: fixed;
      left: 0;
      top: 100px;
      width: 100%;
      z-index: 10;

      li {
        font-size: 17px;
      }
    }
  }
}
</style>
