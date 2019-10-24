<template>
    <div class="index">
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
        <div class="body-header">
          <el-carousel :interval="5000" height="400px">
            <el-carousel-item v-for="item in imageBox" :key="item.id">
              <img :src="item.idView" class="image">
            </el-carousel-item>
          </el-carousel>
          <div class="body-header-right">
            <el-tabs type="border-card">
              <el-tab-pane label="最新比赛">
                <el-table
                  style="margin-top:0px;"
                  :show-header="false"
                  :data="tableDataNew">
                  <el-table-column label="比赛名称" prop="gameName"></el-table-column>
                </el-table>
              </el-tab-pane>
              <el-tab-pane label="最热比赛">
                <el-table
                  style="margin-top:0px;"
                  :show-header="false"
                  :data="tableDataHot">
                  <el-table-column label="比赛名称" prop="gameName"></el-table-column>
                </el-table>
              </el-tab-pane>
            </el-tabs>
          </div>
        </div>

      </div>
    </div>
</template>

<script>
  import userInfo from './userInfo'
  import siteHeader from './siteHeader'
    export default {
        name: "index",
        components:{userInfo,siteHeader},
        mounted(){
          this.username = sessionStorage.getItem('username')
          this.userId = sessionStorage.getItem('userId')
          this.nickName = sessionStorage.getItem('nickName')
          if(!this.nickName)
            this.nickName = this.username
          this.email = sessionStorage.getItem('email')
          this.$api.comp.getNewestComp({}).then((res)=>{
            if(res.data.status==0){
              let info = res.data
              let compList = info['compList']
              for(let i=0;i<compList.length;++i){
                this.tableDataNew.push({
                  gameName:compList[i]['gameName']
                })
              }
            }
          })
          this.$api.comp.getHotestComp({}).then((res)=>{
            if(res.data.status==0){
              let info = res.data
              let compList = info['compList']
              for(let i=0;i<compList.length;++i){
                this.tableDataHot.push({
                  gameName:compList[i]['gameName']
                })
              }
            }
          })
        },
        data(){
            return{
              activeIndex:'0',
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
              userInfoVisible:false,
              tableDataNew:[],
              tableDataHot:[]
            }
        },
      methods:{
        handleSelect(key, keyPath) {
          console.log(key, keyPath);
        },
        gotoClassInfo(classNum){
          this.$router.push({path:'/classInfo/'+classNum})
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
  .customWidth{
    width:40%!important;
  }
  .el-button{
    border-radius:30px;
  }

  .body{
    width:100%;
    margin:0;
    padding:0;
    .body-header{
      margin-top:200px;
      z-index:-1;
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
      position:fixed;
      left:0;
      top:100px;
      width:100%;
      li{
        font-size:17px;
      }
    }
  }
</style>
