<template>
    <div class="favorite">
      <el-table :data="tableData.slice((currentPage-1)*PageSize,currentPage*PageSize)">
        <el-table-column
          prop="gameId"
          width="80"
          label="#"></el-table-column>
        <el-table-column
          prop="gameName"
          label="比赛名称"></el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="100">
          <template slot-scope="scope">
            <el-button type="text" @click="gotoGameDetail(scope.row.gameId)">查看</el-button>
            <el-button type="text" @click="deleteFavorite(scope.row.gameId)">取消</el-button>
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
</template>

<script>
    export default {
      name: "favorite",
      props:{
        userId:{
          type:Number
        }
      },
      mounted(){
        this.$api.user.getFavorite({
          userId:this.userId
        }).then((res)=>{
          console.log(res.data)
          if(res.data.status==0){
            let info = res.data.markMessages
            this.totalCount = info.length
            for(let i=0;i<info.length;++i){
              this.tableData.push({
                gameId:info[i]['compInfoId'],
                gameName:info[i]['compTitle']
              })
            }
          }
        })
      },
      data(){
        return{
          tableData:[],
          currentPage:1,
          totalCount:0,
          PageSize:8,
          pageSizes:[1,2,3,4],
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
        deleteFavorite(compId){
          this.$api.user.deleteFavorite({
            compId:compId,
            userId:this.userId
          }).then((res)=>{
           if(res.data.status==0){
             for(let i=0;i<this.tableData.length;++i){
               if(this.tableData[i]['gameId']==compId){
                 this.tableData.splice(i, 1)
                 this.totalCount = this.totalCount - 1
                 break;
               }
             }
             this.$message.success(res.data.message)
           }
           else{
             this.$message.error(res.data.message)
           }
          })
        },
        gotoGameDetail(gameId){
          this.$router.push({path:'/gameDetail', query:{gameId:gameId}})
        }
      }
    }
</script>

<style scoped>

</style>
