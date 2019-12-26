<template>
    <div class="myBBS">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="我的发帖" name="first">
          <el-table :data="tableData1.slice((currentPage1-1)*PageSize1,currentPage1*PageSize1)" border>
            <el-table-column prop="bbsClass"
                             label="板块"
                             width="120"></el-table-column>
            <el-table-column prop="bbsName"
                             label="帖子标题"></el-table-column>
            <el-table-column prop="sendTime"
                             label="发帖时间"></el-table-column>
            <el-table-column
              fixed="right"
              label="操作"
              prop="bbsId"
              width="100">
              <template slot-scope="scope">
                <el-button type="text" @click="checkBBS(scope.row.bbsId)">查看</el-button>
                <el-button type="text" @click="deleteBBS(scope.row.bbsId)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="tabListPage">
            <el-pagination @current-change="handlesCurrentChange1"
                           :current-page="currentPage1"
                           :page-size="PageSize1" layout="total, prev, pager, next, jumper"
                           :total="totalCount1">
            </el-pagination>
          </div>
        </el-tab-pane>
        <el-tab-pane label="我的回帖" name="second">
          <el-table :data="tableData2.slice((currentPage2-1)*PageSize2,currentPage2*PageSize2)" border>
            <el-table-column prop="bbsName"
                             label="帖子标题"></el-table-column>
            <el-table-column prop="replyContent"
                             label="回复内容"></el-table-column>
            <el-table-column prop="replyTime"
                             label="回复时间"></el-table-column>
            <el-table-column
              fixed="right"
              prop="id"
              label="操作"
              width="100">
              <template slot-scope="scope">
                <el-button type="text" @click="checkBBS(scope.row.id.bbsId)">查看</el-button>
                <el-button type="text" @click="deleteReply(scope.row.id.replyId)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="tabListPage">
            <el-pagination @current-change="handlesCurrentChange2"
                           :current-page="currentPage2"
                           :page-size="PageSize2" layout="total, prev, pager, next, jumper"
                           :total="totalCount2">
            </el-pagination>
          </div>
        </el-tab-pane>
      </el-tabs>

    </div>
</template>

<script>
    export default {
      name: "myBBS",
      props:{
        userId:{
          type:Number
        }
      },
      mounted(){
        this.$api.bbs.getBBSByUserId({
          userId:this.userId
        }).then((res)=>{
          if(res.data.status==0){
            let info = res.data.bbsinfo
            this.totalCount1 = info.length
            for(let i=0;i<info.length;++i){
              this.tableData1.push({
                bbsName:info[i]['TTopic'],
                bbsId:info[i]['Tid'],
                bbsClass:info[i]['bbsClass'],
                sendTime:info[i]['sendTime']
              })
            }
          }
          else{
            this.$message.error(res.data.message)
          }
        })

        this.$api.bbs.getReplyByUserId({
          userId:this.userId
        }).then((res)=>{
          if(res.data.status==0){
            let replyList = res.data.bbsinfo
            this.totalCount2 = replyList.length
            for(let i=0;i<replyList.length;++i){
              this.tableData2.push({
                id:{
                  bbsId:replyList[i]['RTid'],
                  replyId:replyList[i]['Rid'],
                },
                bbsName:replyList[i]['bbsName'],
                replyContent:replyList[i]['RContent'],
                replyTime:replyList[i]['replyTime']
              })
            }

          }
        })
      },
      data(){
          return{
            activeName:'first',
            tableData1:[],
            tableData2:[],
            currentPage1:1,
            totalCount1:0,
            PageSize1:5,
            currentPage2:1,
            totalCount2:0,
            PageSize2:5,
          }
      },
      methods:{
        // 显示第几页
        handlesCurrentChange1(val) {
          // 改变默认的页数
          this.currentPage1=val
        },
        // 显示第几页
        handlesCurrentChange2(val) {
          // 改变默认的页数
          this.currentPage2=val
        },
        handleClick(tab, event) {
          console.log(tab, event);
        },
        checkBBS(bbsId){
          this.$router.push({path:'/bbsDetail/'+bbsId})
        },
        deleteBBS(bbsId){
          this.$confirm('确定永久删除这条帖子吗？', '提示', {
            confirmButtonText:'确定',
            cancelButtonText:'取消',
            type:'warning'
          }).then(()=>{
            this.$api.bbs.deleteBBS({
              bbsId:bbsId
            }).then((res)=>{
              if(res.data.status==0){
                for(let i=0;i<this.tableData1.length;++i){
                  if(this.tableData1[i]['bbsId']==bbsId){
                    this.tableData1.splice(i, 1)
                    this.totalCount1 = this.totalCount1 - 1
                    break;
                  }
                }
                this.$message.success(res.data.message)
              }
              else{
                this.$message.error(res.data.message)
              }
            })
          }).catch(()=>{

          })

        },
        deleteReply(replyId){
          this.$confirm('确定永久删除这条回复吗？', '提示', {
            confirmButtonText:'确定',
            cancelButtonText:'取消',
            type:'warning'
          }).then(()=>{
            this.$api.bbs.deleteReply({
              replyId:replyId
            }).then((res)=>{
              if(res.data.status==0){
                for(let i=0;i<this.tableData2.length;++i){
                  if(this.tableData2[i].id.replyId==replyId){
                    this.tableData2.splice(i, 1)
                    this.totalCount2 = this.totalCount2 - 1
                    break;
                  }
                }
                this.$message.success(res.data.message)
              }
              else{
                this.$message.error(res.data.message)
              }
            })
          }).catch(()=>{

          })

        }
      }
    }
</script>

<style lang="scss">
.myBBS{
  .tabListPage{
    margin-top:10px;
    width:50%;
    margin-left:25%;
  }
}
</style>
