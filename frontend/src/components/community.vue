<template>
    <div class="community">
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
        <div class="information">
          <el-tabs :tab-position="tabPosition" v-model="tableActive" type="border-card">
            <el-tab-pane label="科技创新" :key="1" :name="'1'">
              <bbs-info :bbsClass="1" :bbsClassName="'科技创新'"></bbs-info>
            </el-tab-pane>
            <el-tab-pane label="创业商业" :key="2" :name="'2'">
              <bbs-info :bbsClass="2" :bbsClassName="'创业商业'"></bbs-info>
            </el-tab-pane>
            <el-tab-pane label="艺术爱好" :key="3" :name="'3'">
              <bbs-info :bbsClass="3" :bbsClassName="'艺术爱好'"></bbs-info>
            </el-tab-pane>
            <el-tab-pane label="游戏动漫" :key="4" :name="'4'">
              <bbs-info :bbsClass="4" :bbsClassName="'游戏动漫'"></bbs-info>
            </el-tab-pane>
            <el-tab-pane label="广告公益" :key="5" :name="'5'">
              <bbs-info :bbsClass="5" :bbsClassName="'广告公益'"></bbs-info>
            </el-tab-pane>
            <el-tab-pane label="学科竞赛" :key="6" :name="'6'">
              <bbs-info :bbsClass="6" :bbsClassName="'学科竞赛'"></bbs-info>
            </el-tab-pane>
            <el-tab-pane label="体育竞赛" :key="7" :name="'7'">
              <bbs-info :bbsClass="7" :bbsClassName="'体育竞赛'"></bbs-info>
            </el-tab-pane>
          </el-tabs>
        </div>
      </div>
    </div>
</template>

<script>
  import siteHeader from './siteHeader'
  import bbsInfo from './bbsInfo'
    export default {
      name: "community",
      components:{siteHeader, bbsInfo},
      data(){
        return {
          activeIndex:"8",
          tabPosition:'left',
          tableActive:'1',
        }
      },
      methods:{
        handleSelect(key, keyPath) {
          console.log(key, keyPath);
        },
        gotoClassInfo(classNum){
          this.$router.push({path:'/classInfo', query:{classNum:classNum}})
        },
        gotoIndex(){
          this.$router.push({name:'index'})
        },
        gotoCommunity(){
          this.$router.push({name:'community'})
        }
      }
    }
</script>

<style lang="scss">
  .body{
    width:100%;
    margin:0;
    padding:0;
    .information{
      margin-top:180px;
    }
    .el-tabs__item{
      font-size:16px;
    }
    .el-menu{
      position:fixed;
      left:0;
      top:100px;
      width:100%;
      z-index:10;
      li{
        font-size:17px;
      }
    }
  }
</style>
