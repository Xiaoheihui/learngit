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
        <div class="bbsContent">
          <div class="bbsSender">
            <div class="senderHead">
              <h1>{{bbsinfo.bbstopic}}</h1>
              <div class="bbsInfo">
                <div class="senderName">
                  <img :src=imgurl class="headimg" alt="touxiang">
                  <span>{{bbsinfo.bbsSender}} &nbsp;&nbsp;<el-tag effect="dark" type="primary" size="medium">楼主</el-tag></span>
                </div>
                <span><i class="el-icon-chat-dot-square"></i> {{bbsinfo.bbsComments}}</span>
                <span><i class="el-icon-time"></i> {{bbsinfo.bbsTime}}</span>
              </div>
            </div>
            <el-divider></el-divider>
            <div class="senderContent">
              <p>
                {{bbsinfo.bbsContent}}
              </p>
            </div>

            <!--<div class="senderEnd">-->
              <!--<span><i class="el-icon-time"></i> 2019.11.11 22.31</span>-->
            <!--</div>-->
          </div>
          <el-divider></el-divider>
          <div class="bbsReply" v-for="(item,index) in replyList">
            <div class="replyHead">
              <div class="replyName">
                <img :src="item['img']"  class="headimg" alt="touxiang">
                <span>{{item['name']}} &nbsp;&nbsp;<el-tag effect="dark" type="danger" size="small">回复</el-tag></span>
              </div>
              <span># {{item['level']}}</span>
            </div>
            <div class="replyContent">
              <p>
                {{item['content']}}
              </p>
            </div>
            <div class="replyEnd">
              <span><i class="el-icon-time"></i> {{item['time']}}</span>
            </div>
            <el-divider></el-divider>
          </div>
          <div class="tabListPage">
            <el-pagination @size-change="handleSizeChange"
                           @current-change="handlesCurrentChange"
                           :current-page="currentPage"
                           :page-sizes="pageSizes"
                           :page-size="PageSize" layout="total, prev, pager, next, jumper"
                           :total="totalCount">
            </el-pagination>
          </div>
          <send-reply :userId=userId :bbsId=bbsId></send-reply>
        </div>
      </div>
    </div>
</template>

<script>
  import siteHeader from './siteHeader'
  import sendReply from './sendReply'
    export default {
      name: "bbsDetail",
      components:{siteHeader, sendReply},
      mounted(){
        this.userId = parseInt(sessionStorage.getItem('userId'))
        this.bbsId = parseInt(this.$route.params.bbsId)
        this.totalCount = this.replyList.length
        this.$api.bbs.getReplyByBBSId({
          bbsId:this.bbsId
        }).then((res)=>{
          if(res.data.status===0){
            let replyList = res.data.replyinfos
            for(let i=0;i<replyList.length;++i){
              this.replyList.push({
                name:replyList[i]['Unickname'],
                level:replyList[i]['RLevelNum'],
                content:replyList[i]['RContent'],
                time:replyList[i]['time'],
                img:replyList[i]['img']
              })
            }
          }
        })
        this.$api.bbs.getBBSByBBSId({
          bbsId:this.bbsId
        }).then((res)=>{
          if(res.data.status===0){
            let bbsinfo = res.data.bbsinfo
            this.bbsinfo.bbsSender = bbsinfo['senderName']
            this.bbsinfo.bbstopic = bbsinfo['TTopic']
            this.bbsinfo.bbsComments = bbsinfo['TReplyCount']
            this.bbsinfo.bbsTime = bbsinfo['time']
            this.bbsinfo.bbsContent = bbsinfo['TContents']
          }
          else{
            console.log(res.data.message)
          }
        })
      },
      data(){
        return{
          activeIndex:'8',
          imgurl:"/static/img/timg.jpg",
          currentPage:1,
          totalCount:0,
          PageSize:8,
          pageSizes:[1,2,3,4],
          userId:null,
          bbsId:null,
          replyList:[],
          bbsinfo:{
            bbstopic:'',
            bbsSender:'',
            bbsComments:0,
            bbsTime:'',
            bbsContent:''
          }
        }
      },
      methods:{
        gotoClassInfo(classNum){
          // this.activeIndex = classNum
          this.$router.push({path:'/classInfo/'+classNum})
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
      }
    }
</script>

<style lang="scss">
.bbsDetail{
  .body {
    width: 100%;
    margin: 0;
    padding: 0;
    .bbsContent{
      margin-top:180px;
      padding-bottom:50px;
      width:80%;
      margin-left:10%;
      /*background-color: aliceblue;*/
      .bbsSender{
        margin-left:100px;
        margin-right:100px;
        margin-bottom:10px;
        padding-top:30px;
       padding-bottom:10px;
        /*border-style: solid;*/
        /*border-width: 1px;*/
        /*border-color:black;*/
        /*border-radius:10px;*/
        .senderHead{
          .bbsInfo{
            display: flex;
            flex-direction: row;
            align-items:center;
            justify-content: space-around;
            width:60%;
            margin-left:20%;
            .senderName{
              display: flex;
              flex-direction: row;
              align-items:center;
              justify-content: start;
              .el-tag{
                font-size:13px;
              }
            }
          }
          .headimg{
            width:50px;
            height:50px;
            border-radius: 50%;
            margin-right:20px;
          }
          span{
            text-align: left;
            font-size:16px;
          }
        }
        .senderContent{
          margin-left:10px;
          margin-right:10px;
          h1{
            text-align: left;
          }
          p{
            font-size:17px;
            text-align: left;
            line-height:1.8;
          }
        }
        /*.senderEnd{*/
          /*span{*/
            /*float:right;*/
          /*}*/
        /*}*/
      }
      .bbsReply{
        margin-left:100px;
        margin-right:100px;
        margin-bottom:10px;
        padding-top:10px;
        padding-bottom:30px;
        /*border-style: solid;*/
        /*border-width: 1px;*/
        /*border-color:black;*/
        /*border-radius:10px;*/
        .replyHead{
          display: flex;
          flex-direction: row;
          align-items:center;
          justify-content: space-between;
          /*padding-right:40px;*/
          .replyName{
            display: flex;
            flex-direction: row;
            align-items:center;
            justify-content: start;
            .headimg{
              width:50px;
              height:50px;
              border-radius: 50%;
              margin-right:20px;
            }
            span{
              text-align: left;
              font-size:15px;
            }
            .el-tag{
              font-size:12px;
            }
          }

        }
        .replyContent{
          margin-left:10px;
          margin-right:10px;
          p{
            font-size:16px;
            text-align: left;
            line-height:1.6;
          }
        }
        .replyEnd{
          padding-bottom:20px;
          span{
            float:right;
          }
        }
      }
    }
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
