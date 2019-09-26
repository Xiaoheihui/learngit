<template>
    <div class="classInfo">
      <el-dialog title="用户信息"
                 :visible.sync="userInfoVisible"
                 v-if="userInfoVisible==true"
                 customClass="customWidth">
        <userInfo></userInfo>
      </el-dialog>
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
                <span>您好,{{nickName}}</span>
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
          <el-menu-item index="0" @click="gotoIndex">平台首页</el-menu-item>
          <el-menu-item index="1" @click="gotoClassInfo('1')">科技创新</el-menu-item>
          <el-menu-item index="2" @click="gotoClassInfo('2')">创业商业</el-menu-item>
          <el-menu-item index="3" @click="gotoClassInfo('3')">艺术爱好</el-menu-item>
          <el-menu-item index="4" @click="gotoClassInfo('4')">游戏动漫</el-menu-item>
          <el-menu-item index="5" @click="gotoClassInfo('5')">广告公益</el-menu-item>
          <el-menu-item index="6" @click="gotoClassInfo('6')">学科竞赛</el-menu-item>
          <el-menu-item index="7" @click="gotoClassInfo('7')">体育竞赛</el-menu-item>
          <el-menu-item index="8" @click="gotoClassInfo('8')">社区论坛</el-menu-item>
        </el-menu>
        <el-table
          :data="tableData.slice((currentPage-1)*PageSize,currentPage*PageSize)"
          style="width:80%;margin-left:10%;"
          max-height="1000">
          <el-table-column
            prop="gameId"
            label="比赛ID"
            width="250">
          </el-table-column>
          <el-table-column
            prop="gameName"
            label="比赛名称"
            width="450">
          </el-table-column>
          <el-table-column
            prop="startTime"
            label="报名开始时间">
          </el-table-column>
          <el-table-column
            prop="deltaTime"
            label="报名截止时间">
          </el-table-column>
        </el-table>
        <div class="tabListPage">
          <el-pagination @size-change="handleSizeChange"
                         @current-change="handlesCurrentChange"
                         :current-page="currentPage"
                         :page-sizes="pageSizes"
                         :page-size="PageSize" layout="total, prev, pager, next, jumper"
                         :total="totalCount">
          </el-pagination>
        </div>
      </div>
    </div>
</template>

<script>
  import userInfo from './userInfo'
    export default {
    components:{userInfo},
        name: "classInfo",
      mounted(){
      console.log(this.$route.query.classNum)
        if(this.$route.query.classNum)
          this.activeIndex = this.$route.query.classNum
        this.username = sessionStorage.getItem('username')
        this.userId = sessionStorage.getItem('userId')
        this.nickName = sessionStorage.getItem('nickName')
        if(!this.nickName)
          this.nickName = this.username
        this.email = sessionStorage.getItem('email')
        this.$api.comp.getCompInfoByClassId({
          classId:parseInt(this.activeIndex)
        }).then((res)=>{
          if(res.data.status==0){
            let infos = res.data.compInfo
            console.log(infos[0])
            this.totalCount = infos.length
            for(let i=0;i<infos.length;++i){
              let gameName = infos[i]['IName']
              let gameId = infos[i]['Iid']
              let gameApplyEndTime = infos[i]['IApplyEndTime']
              let gameApplyStartTime = infos[i]['IApplyStartTime']
              this.tableData.push({
                gameName:gameName,
                gameId:gameId,
                deltaTime:gameApplyEndTime,
                startTime:gameApplyStartTime
              })
            }
          }
        })
      },
      data(){
      return{
        userInfoVisible:false,
        activeIndex:"2",
        username:null,
        nickName:'',
        userId:'',
        tableData:[],
        currentPage:1,
        totalCount:0,
        PageSize:8,
      }
      },
      methods:{
        // 每页显示的条数
        handleSizeChange(val) {
          // 改变每页显示的条数
          this.PageSize=val
          // 注意：在改变每页显示的条数时，要将页码显示到第一页
          this.currentPage=1
        },
        // 显示第几页
        handlesCurrentChange(val) {
          // 改变默认的页数
          this.currentPage=val
        },
      gotoClassInfo(classNum){
        // this.activeIndex = classNum
        this.$router.push({path:'/classInfo', query:{classNum:classNum}})
        this.$router.go(0)
      },
        gotoIndex(){
        this.$router.push({name:'index'})
        },
        handleSelect(key, keyPath) {
          // console.log(key, keyPath);
        },
        logout(){
          sessionStorage.clear();
          this.$store.dispatch('UserLogout')
          if(! this.$store.state.token){

            this.$router.go(0)
          }else{
            this.$message.error('退出失败');
          }
        },
      }
    }
</script>

<style lang="scss">
  .customWidth{
    width:45%!important;
  }

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
  .body{
    width:100%;
    margin:0;
    padding:0;
    position:fixed;
    left:0;
    top:100px;
    .el-menu{
      li{
        font-size:17px;
      }
    }
  }
</style>
