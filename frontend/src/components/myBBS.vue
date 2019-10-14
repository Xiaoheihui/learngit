<template>
    <div class="myBBS">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="我的发帖" name="first">
          <el-table :data="tableData1.slice((currentPage1-1)*PageSize1,currentPage1*PageSize1)">
            <el-table-column prop="bbsId"
                             label="#"
                              width="80"></el-table-column>
            <el-table-column prop="bbsClass"
                             label="板块"
                             width="120"></el-table-column>
            <el-table-column prop="bbsName"
                             label="帖子标题"></el-table-column>
            <el-table-column
              fixed="right"
              label="操作"
              width="100">
              <template slot-scope="scope">
                <el-button type="text">查看</el-button>
                <el-button type="text" @click="deleteBBS(scope.row.bbsId)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="tabListPage">
            <el-pagination @size-change="handleSizeChange1"
                           @current-change="handlesCurrentChange1"
                           :current-page="currentPage1"
                           :page-sizes="pageSizes1"
                           :page-size="PageSize1" layout="total, prev, pager, next, jumper"
                           :total="totalCount1">
            </el-pagination>
          </div>
        </el-tab-pane>
        <el-tab-pane label="我的回帖" name="second">

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
                bbsClass:info[i]['bbsClass']
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
            activeName:'first',
            tableData1:[],
            currentPage1:1,
            totalCount1:0,
            PageSize1:8,
            pageSizes1:[1,2,3,4],
          }
      },
      methods:{
        // 每页显示的条数
        handleSizeChange1(val) {
          // 改变每页显示的条数
          this.PageSize1=val
          // 注意：在改变每页显示的条数时，要将页码显示到第一页
          this.currentPage1=1
        },
        // 显示第几页
        handlesCurrentChange1(val) {
          // 改变默认的页数
          this.currentPage1=val
        },
        handleClick(tab, event) {
          console.log(tab, event);
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

</style>
