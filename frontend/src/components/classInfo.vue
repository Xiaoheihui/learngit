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
          <el-menu-item index="8" @click="gotoCommunity">社区论坛</el-menu-item>
        </el-menu>
        <div class="select">
          <div>
            <el-radio-group v-model="gameLevel">
              <el-tag>竞赛级别</el-tag>
              <el-radio :label="0">全部</el-radio>
              <el-radio :label="1">A类</el-radio>
              <el-radio :label="2">B类</el-radio>
              <el-radio :label="3">C类</el-radio>
              <el-radio :label="4">D类</el-radio>
            </el-radio-group>
          </div>
          <div>
            <el-radio-group v-model="gameArea">
              <el-tag>比赛地区</el-tag>
              <el-radio :label="0">全部</el-radio>
              <el-radio :label="1">全国</el-radio>
              <el-radio :label="36">全球</el-radio>
              <el-radio :label="2">北京</el-radio>
              <el-radio :label="20">广东</el-radio>
              <el-radio :label="100">其他</el-radio>
            </el-radio-group>
          </div>
          <div class="selectSon">
            <el-tag>报名开始时间</el-tag>
            <el-date-picker type="date" placeholder="选择日期" v-model="selectStart"></el-date-picker>
            <el-tag>报名结束时间</el-tag>
            <el-date-picker type="date" placeholder="选择日期" v-model="selectEnd"></el-date-picker>
          </div>
          <el-button type="primary" @click="select">筛选</el-button>
        </div>
        <el-table
          :data="tables.slice((currentPage-1)*PageSize,currentPage*PageSize)"
          :default-sort = "{prop: 'startTime', order: 'descending'}"
          @row-click="openDetails"
          style="width:80%;margin-left:10%;"
          stripe>
          <el-table-column
            prop="clickCounts"
            width="120">
            <template slot="header" slot-scope="scope">
             <i class="el-icon-view"></i>
            </template>
          </el-table-column>
          <el-table-column
            prop="gameName"
            label="比赛名称"
            width="450">
            <template slot-scope="scope">
              {{scope.row.gameName['gameName']}}
            </template>
          </el-table-column>
          <el-table-column
            prop="startTime"
            sortable
            label="报名开始时间"
            width="160">
          </el-table-column>
          <el-table-column
            prop="deltaTime"
            sortable
            label="报名截止时间"
            width="160">
          </el-table-column>
          <el-table-column align="center">
            <template slot="header" slot-scope="scope">
              <el-input
                v-model="search"
                placeholder="输入关键字搜索"></el-input>
            </template>
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
      console.log(this.$route.params.classNum)
        if(this.$route.params.classNum)
          this.activeIndex = this.$route.params.classNum
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
            console.log(res.data)
            let infos = res.data.compInfo
            this.totalCount = infos.length
            for(let i=0;i<infos.length;++i){
              let gameName = infos[i]['IName']
              let gameId = infos[i]['Iid']
              let gameApplyEndTime = infos[i]['IApplyEndTime']
              let gameApplyStartTime = infos[i]['IApplyStartTime']
              let clickCounts = infos[i]['clickCounts']
              this.tableData.push({
                gameName:{
                  'gameName':gameName,
                  'gameId':gameId,
                },
                gameId:gameId,
                deltaTime:gameApplyEndTime,
                startTime:gameApplyStartTime,
                clickCounts:clickCounts
              })
            }
          }
          else{
            this.$message.error(res.data.message)
          }
        })
      },
      data(){
      return{
        userInfoVisible:false,
        activeIndex:"-1",
        username:null,
        nickName:'',
        userId:'',
        tableData:[],
        currentPage:1,
        totalCount:0,
        PageSize:8,
        pageSizes:[1,2,3,4],
        gameLevel:0,
        gameArea:0,
        selectStart:null,
        selectEnd:null,
        search:''
      }
      },
      computed: {
        tables () {
          const search = this.search
          if (search) {
            console.log('this.tableData', this.tableData)
            return this.tableData.filter(dataNews => {
              return Object.keys(dataNews).some(key => {
                return String(dataNews[key]).toLowerCase().indexOf(search) > -1
              })
            })
          }
          console.log('this.tableData', this.tableData)
          return this.tableData
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
        this.$router.push({path:'/classInfo/'+classNum})
        this.$router.go(0)
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
          this.$router.push({path:'/gameDetail/'+row.gameName['gameId']})
        },
        select(){
          console.log(this.selectEnd)
          if(this.selectStart!=null&&this.selectEnd!=null&&this.selectEnd<this.selectStart)
          {
            this.$message.error('请正确选择时间！')
            return
          }
          let start = this.selectStart
          let end = this.selectEnd
          if(start==null)
            start = ''
          if(end==null)
            end = ''
          this.$api.comp.getCompInfoBySelect({
            gameClass:this.activeIndex,
            gameLevel: this.gameLevel,
            gameArea:this.gameArea,
            selectStart:start,
            selectEnd: end
          }).then((res)=>{
            if(res.data.status==0){
              let infos = res.data.compInfo
              this.tableData = []
              this.totalCount = infos.length
              for(let i=0;i<infos.length;++i){
                let gameName = infos[i]['IName']
                let gameId = infos[i]['Iid']
                let gameApplyEndTime = infos[i]['IApplyEndTime']
                let gameApplyStartTime = infos[i]['IApplyStartTime']
                let clickCounts = infos[i]['clickCounts']
                this.tableData.push({
                  gameName:{
                    'gameName':gameName,
                    'gameId':gameId,
                  },
                  gameId:gameId,
                  deltaTime:gameApplyEndTime,
                  startTime:gameApplyStartTime,
                  clickCounts:clickCounts
                })
              }
              this.$message.success(res.data.message)
            }
            else{
              this.$message.error(res.data.message)
            }
          })
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
    .select{
      margin-top:180px;
      width:56%;
      margin-left:22%;
      .el-radio-group{
        display:flex;
        justify-content: space-between;
        align-items: center;
        flex-direction: row;
      }
      div{
        margin-bottom:14px;
      }
      .selectSon{
        margin-bottom:20px;
        display:flex;
        justify-content: space-between;
        align-items: center;
        flex-direction: row;
      }
      .el-button{
        width:60%;
        border-radius:50px;
      }
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
    .el-table{
      margin-top:20px;
      .el-input__inner{
        border-radius: 30px;
      }
    }
  }
</style>
