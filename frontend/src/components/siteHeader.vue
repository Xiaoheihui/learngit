<template>
    <div class="header">
      <el-dialog title="用户信息"
                 :visible.sync="userInfoVisible"
                 v-if="userInfoVisible===true"
                 append-to-body
                 customClass="customWidth">
        <userInfo v-on:childsay="listenChild"></userInfo>
      </el-dialog>
      <el-dialog title="我的论坛"
                 :visible.sync="myBBSVisible"
                 v-if="myBBSVisible===true"
                 append-to-body
                 customClass="customWidth">
        <myBBS :userId=userId></myBBS>
      </el-dialog>
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
              <span>您好,{{nickName}}</span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item @click.native="userInfoVisible=true">用户信息</el-dropdown-item>
                <el-dropdown-item @click.native="myBBSVisible=true">我的论坛</el-dropdown-item>
                <el-dropdown-item @click.native = "logout">登出</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  import userInfo from './userInfo'
  import myBBS from './myBBS'
    export default {
      name: "siteHeader",
      components:{userInfo, myBBS},
      mounted(){
        this.username = sessionStorage.getItem('username')
        this.userId = parseInt(sessionStorage.getItem('userId'))
        this.nickName = sessionStorage.getItem('nickName')
        if(!this.nickName)
          this.nickName = this.username
        this.email = sessionStorage.getItem('email')
      },
      data(){
        return{
          userInfoVisible:false,
          myBBSVisible:false,
          username:null,
          nickName:'',
          userId:null,
          email:''
        }
      },
      methods:{
        logout(){
          sessionStorage.clear();
          this.$store.dispatch('UserLogout')
          if(! this.$store.state.token){

            this.$router.go(0)
          }else{
            this.$message.error('退出失败');
          }
        },
        listenChild:function(data){
          console.log('change')
          this.nickName = data
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
    z-index:10;
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
      .user{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        span{
          font-size:17px;
        }
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
</style>
