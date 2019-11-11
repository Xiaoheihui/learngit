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
              <img :src=imgurl class="headimg" alt="touxiang">
              <span>嘿嘿嘿灰灰 &nbsp;&nbsp;<el-tag effect="dark" type="primary" size="medium">楼主</el-tag></span>
            </div>
            <el-divider></el-divider>
            <div class="senderContent">
              <h1>这是测试的标题！</h1>
              <p>
                看到反光镜，面孔，新裤子痛仰这些老牌乐队这么卖力的在演唱，尤其是彭磊蹦起来的那一瞬间除了感动尊敬，更多的是心疼
                他们，因为20年前，他们的梦想肯定是都是变成摇滚巨星让全世界听到他们的歌那种梦想吧(像彭磊说的大家都还是很平凡直到
                现在)，都已经中年了，我确定他们离自己当初想要成就的梦想距离还是很远，所以好像特别珍惜这个舞台，现在的音乐环境没
                有给到属于他们的才华相匹配的舞台和荣耀，他们的才华应该是工人体育馆随随便便开，全国大型巡演分分钟票售罄，幸运的
                是这帮老炮儿还活跃在舞台上，中途已经不知道有多少优秀的音乐人离开了，真心希望每个拿起吉他的孩子都能让这个世界听
                得他的歌儿。
              </p>
            </div>
            <el-divider></el-divider>
            <div class="senderEnd">
              <span><i class="el-icon-time"></i> 2019.11.11 22.31</span>
            </div>
          </div>
          <div class="bbsReply">
            <div class="replyHead">
              <img :src=imgurl class="headimg" alt="touxiang">
              <span>嘿嘿嘿 &nbsp;&nbsp;<el-tag effect="dark" type="danger" size="medium">回复</el-tag></span>
            </div>
            <el-divider></el-divider>
            <div class="replyContent">
              <p>
                看到反光镜，面孔，新裤子痛仰这些老牌乐队这么卖力的在演唱，尤其是彭磊蹦起来的那一瞬间除了感动尊敬，更多的是心疼
                他们，因为20年前，他们的梦想肯定是都是变成摇滚巨星让全世界听到他们的歌那种梦想吧(像彭磊说的大家都还是很平凡直到
                现在)
              </p>
            </div>
            <el-divider></el-divider>
            <div class="replyEnd">
              <span><i class="el-icon-time"></i> 2019.11.11 22.31</span>
            </div>
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
        </div>
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
          activeIndex:'8',
          imgurl:"/static/img/timg.jpg",
          currentPage:1,
          totalCount:0,
          PageSize:8,
          pageSizes:[1,2,3,4],
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
      width:80%;
      margin-left:10%;
      background-color: aliceblue;
      .bbsSender{
        margin-left:80px;
        margin-right:80px;
        margin-bottom:10px;
        padding-top:30px;
       padding-bottom:30px;
        border-style: solid;
        border-width: 1px;
        border-color:black;
        border-radius:10px;
        .senderHead{
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
            font-size:18px;
          }
        }
        .senderContent{
          margin-left:10px;
          margin-right:10px;
          h1{
            text-align: left;
          }
          p{
            font-size:19px;
            text-align: left;
            line-height:1.8;
          }
        }
        .senderEnd{
          span{
            float:right;
          }
        }
      }
      .bbsReply{
        margin-left:80px;
        margin-right:80px;
        margin-bottom:10px;
        padding-top:30px;
        padding-bottom:30px;
        border-style: solid;
        border-width: 1px;
        border-color:black;
        border-radius:10px;
        .replyHead{
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
            font-size:18px;
          }
        }
        .replyContent{
          margin-left:10px;
          margin-right:10px;
          p{
            font-size:19px;
            text-align: left;
            line-height:1.8;
          }
        }
        .replyEnd{
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
