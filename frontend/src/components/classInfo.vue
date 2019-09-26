<template>
    <div class="classInfo">
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
          <el-menu-item index="8" @click="gotoClassInfo('8')">社区论坛</el-menu-item>
        </el-menu>
        <el-table
          :data="tableData.slice((currentPage-1)*PageSize,currentPage*PageSize)"
          :default-sort = "{prop: 'startTime', order: 'descending'}"
          @row-click="openDetails"
          style="width:80%;margin-left:10%;"
          stripe>
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
            sortable
            label="报名开始时间">
          </el-table-column>
          <el-table-column
            prop="deltaTime"
            sortable
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
  import siteHeader from './siteHeader'
    export default {
    components:{userInfo, siteHeader},
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
        activeIndex:"1",
        username:null,
        nickName:'',
        userId:'',
        tableData:[],
        currentPage:1,
        totalCount:0,
        PageSize:8,
        pageSizes:[1,2,3,4]
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
        openDetails(row){
          this.$router.push({path:'/gameDetail', query:{gameId:row.gameId}})
        }
      }
    }
</script>

<style lang="scss">
  .customWidth{
    width:40%!important;
  }

  .body{
    width:100%;
    margin:0;
    padding:0;
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
    .el-table{
      margin-top:180px;

    }
  }
</style>
