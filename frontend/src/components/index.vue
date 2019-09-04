<template>
    <div class="index">
      <div class="header">
        <div class="header-left">
          <img src="../static/img/timg.jpg">
          <span>大学生赛事平台</span>
        </div>
        <div class="header-right">
          <div class="user">
            <i class="el-icon-user"></i>
            <router-link :to="{ path: '/login'}" replace v-if="username==null"><span>登录</span></router-link>
            <el-divider direction="vertical" v-if="username==null"></el-divider>
            <router-link :to="{ path: '/register'}" replace v-if="username==null"><span>注册</span></router-link>
            <div v-else>
              <el-dropdown>
                <span >您好,{{username}}</span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item @click.native="userInfoVisible=true">用户信息</el-dropdown-item>
                  <el-dropdown-item @click.native = "logout">登出</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </div>
          </div>
        </div>
      </div>
      <div class="body">
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
          <el-menu-item index="1">平台首页</el-menu-item>
          <el-menu-item index="2">创业商业</el-menu-item>
          <el-menu-item index="3">体育竞技</el-menu-item>
          <el-menu-item index="4">学科竞赛</el-menu-item>
          <el-menu-item index="5">游戏动漫</el-menu-item>
          <el-menu-item index="6">广告公益</el-menu-item>
          <el-menu-item index="7">科技创新</el-menu-item>
          <el-menu-item index="8">社区论坛</el-menu-item>
        </el-menu>
        <div class="body-header">
          <el-carousel :interval="5000" height="400px">
            <el-carousel-item v-for="item in imageBox" :key="item.id">
              <img :src="item.idView" class="image">
            </el-carousel-item>
          </el-carousel>
          <div class="body-header-right">
            <el-tabs type="border-card">
              <el-tab-pane label="最新比赛">最新比赛</el-tab-pane>
              <el-tab-pane label="最热比赛">最热比赛</el-tab-pane>
              <el-tab-pane label="评论最多">评论最多</el-tab-pane>
            </el-tabs>
          </div>
        </div>

      </div>
    </div>
</template>

<script>
    export default {
        name: "index",
        data(){
            return{
              activeIndex:'1',
              imageBox:[
                {id:0,idView:require("../static/img/game1.jpg")},
                {id:1,idView:require("../static/img/game2.jpg")},
                {id:2,idView:require("../static/img/game3.jpg")},
                {id:3,idView:require("../static/img/game4.jpg")},
                {id:4,idView:require("../static/img/game5.jpg")},
              ],
              username:null,
              nickName:'',
              userId:'',

            }
        },
      methods:{
        handleSelect(key, keyPath) {
          console.log(key, keyPath);
        }
      }
    }
</script>

<style lang="scss">
    .header{
      position: fixed;
      left:0px;
      top:0px;
      background-color: #f7f7f7;
      width:100%;
      height:100px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      .header-right{
        height:100%;
        width:20%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        a {
          text-decoration: none;
        }
        span{
          color:#2C537A
        }
      }
      .header-left{
        height:100%;
        width:30%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-around;
        img{
          width:110px;
          height:94%;
          margin-top:3%;
          margin-bottom:3%;
        }
        span{
          font-size:32px;
        }
      }
    }
  .body{
    width:100%;
    margin:0;
    padding:0;
    position:fixed;
    left:0;
    top:100px;
    .body-header{
      margin-top:40px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-around;
      img{
        width:100%;
        height:100%;
      }
      .el-carousel{
        width:45%;
      }
      .body-header-right{
        height:400px;
        width:45%;
        background-color: aliceblue;
        .el-tabs{
          height:395px;
        }
      }
    }
    .el-menu{
      li{
        font-size:17px;
      }
    }
  }
</style>
