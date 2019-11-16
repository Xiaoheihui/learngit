<template>
    <div class="gameDetail">
      <el-dialog title="用户信息"
                 :visible.sync="gameUserInfoVisible"
                 v-if="gameUserInfoVisible===true"
                 append-to-body
                 customClass="customWidth">
        <game-user-info :userId="this.promulgatorId"></game-user-info>
      </el-dialog>
      <site-header v-on:childsay="listenChild"></site-header>
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
        <div class="detail">
          <div class="detail-header">
            <h1>{{this.gameName}}</h1>
            <div class="recordinfo">
              <span><i class="el-icon-time"></i> {{time}}</span>
              <span @click="gameUserInfoVisible=true"><i class="el-icon-user"></i> {{promulgator}}</span>
              <span><i class="el-icon-view"></i> {{chickCount}}</span>
              <div>
                <el-button size="small" type="primary" icon="el-icon-star-on" @click="addFavorite" circle></el-button>
                <el-button size="small" type="danger" @click="deleteCompInfo" v-if="is_superuser" icon="el-icon-delete-solid" circle></el-button>
              </div>
            </div>
          </div>
          <el-table :data="tableData1"
                               border
                               style="width:80%;margin-left:10%;margin-top:40px;">
          <el-table-column
            prop="gameApplyStartTime"
            label="报名开始时间"
          ></el-table-column>
          <el-table-column
            prop="gameApplyEndTime"
            label="报名结束时间"
          ></el-table-column>
          <el-table-column
            prop="gameObject"
            label="参赛对象"
          ></el-table-column>
          <el-table-column
            prop="applyMethods"
            label="参赛方法"
          ></el-table-column>
        </el-table>
          <el-table :data="tableData2"
                    border
                    style="width:80%;margin-left:10%;margin-top:0;">
            <el-table-column
              prop="gameForm"
              label="参赛形式"
            ></el-table-column>
            <el-table-column
              prop="gameOrganizers"
              label="主办单位"
            ></el-table-column>
            <el-table-column
              prop="gameArea"
              label="参赛地区"
            ></el-table-column>
            <el-table-column
              prop="gameLevel"
              label="竞赛级别"
            ></el-table-column>
          </el-table>
          <el-table :data="tableData3"
                    border
                    style="width:80%;margin-left:10%;margin-top:0;">
            <el-table-column
              prop="gameTime"
              label="比赛时间"
            ></el-table-column>
            <el-table-column
              prop="gameClass"
              label="比赛类别"
            ></el-table-column>
            <el-table-column
              prop="gameUrl"
              label="官方网址"
            ></el-table-column>
            <el-table-column
              prop="gameId"
              label="比赛ID"
            ></el-table-column>
          </el-table>
          <div class="gameText">
            <p>{{this.gameStatement}}</p>
          </div>

        </div>

      </div>
    </div>
</template>

<script>
  import siteHeader from './siteHeader'
  import gameUserInfo from './gameUserInfo'
    export default {
      name: "gameDetail",
      components:{siteHeader, gameUserInfo},
      mounted(){
        this.gameId = this.$route.params.gameId
        this.userId = sessionStorage.getItem('userId')
        if(sessionStorage.getItem('is_superuser')==='false'||sessionStorage.getItem('is_superuser')==null)
          this.is_superuser = false
        else
          this.is_superuser = true
        this.$api.comp.getCompInfoByCompId({
          compId:this.gameId
        }).then((res)=>{
          console.log(res)
          if(res.data.status==0){
            let info = res.data
            this.gameName = info['IName']
            this.gameObject = info['IObject']
            this.gameApplyStartTime = info['IApplyStartTime']
            this.gameApplyEndTime = info['IApplyEndTime']
            this.gameOrganizers = info['IOrganizers']
            this.gameForm = info['IForm']
            this.applyMethods = info['IMethods']
            this.gameUrl = info['Iurls']
            this.gameLevel = info['compLevel']
            this.gameClass = info['compClass']
            this.gameArea = info['compArea']
            this.gameStatement = info['IStatement']
            this.gameTime = info['ISchedule']
            this.activeIndex = String(info['IClass'])
            this.recordId = info['Rid']
            this.promulgator = info['unickname']
            this.promulgatorId = info['promulgator']
            this.time = info['time']
            this.chickCount = info['chickCount']
            this.favor = info['markCount']
            this.tableData1.push({
              gameApplyEndTime:this.gameApplyEndTime,
              gameApplyStartTime:this.gameApplyStartTime,
              gameObject:this.gameObject,
              applyMethods:this.applyMethods
            })
            this.tableData2.push({
              gameForm:this.gameForm,
              gameOrganizers:this.gameOrganizers,
              gameArea:this.gameArea,
              gameLevel:this.gameLevel
            })
            this.tableData3.push({
              gameClass:this.gameClass,
              gameTime:this.gameTime,
              gameUrl:this.gameUrl,
              gameId:this.gameId
            })

          }
          else{
            this.$message.error(res.data.message)
          }
        })
      },
      data(){
        return{
          activeIndex:'',
          userId:null,
          promulgatorId:null,
          gameName:'',
          gameId:0,
          gameApplyEndTime:'',
          gameApplyStartTime:'',
          gameOrganizers:'',
          gameObject:'',
          applyMethods:'',
          gameForm:'',
          gameUrl:'',
          gameClass:'',
          gameLevel:'',
          gameArea:'',
          gameStatement:'',
          gameTime:'',
          recordId:'',
          promulgator:'',
          time:'',
          favor:0,
          chickCount:0,
          tableData1:[],
          tableData2:[],
          tableData3:[],
          gameUserInfoVisible:false,
          is_superuser:false,
        }
      },
      methods:{
        listenChild:function(data){
          this.favor -= 1
        },
        gotoClassInfo(classNum){
          this.$router.push({path:'/classInfo/'+classNum})
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
        addFavorite(){
          if(!this.userId){
            this.$message.warning('登录后才可以收藏哦！')
            return
          }
          this.$api.user.addFavorite({
            compId:this.recordId,
            userId:this.userId
          }).then((res)=>{
            console.log(res)
            if(res.data.status==0){
              this.favor+=1
              this.$message.success('收藏成功！')
            }
            else if(res.data.status==2){
              this.$message.warning(res.data.message)
            }
            else{
              this.$message.error('收藏失败，请重试！')
            }
          })
        },
        deleteCompInfo(){
          this.$api.comp.deleteCompInfo({
            userId:this.userId,
            compId:this.gameId
          }).then((res)=>{
            if(res.data.status===0){
              this.$message.success(res.data.message)
              this.$router.push({path:'/classInfo/1'})
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
    .detail{
      margin-top:200px;
      .detail-header{
        .el-button{
          border-radius:30px;
        }
        h1{
          font-size:30px;
          color:#36648B
        }
        .recordinfo{
          width:44%;
          margin-left:28%;
          display:flex;
          justify-content: space-around;
          align-items: center;
          flex-direction: row;
        }
      }
      .gameText{
        margin-top:20px;
        width:80%;
        margin-left:10%;
        background-color: #f7f7f7;
        p{
          white-space: pre-wrap;
          padding-top:40px;
          width:70%;
          margin-left:15%;
          line-height:2;
          text-align: left;
        }
      }

    }
  }
</style>
