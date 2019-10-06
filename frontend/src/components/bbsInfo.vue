<template>
    <div class="bbsInfo">
      <el-dialog title="发帖"
                 :visible.sync="bbsVisible"
                 v-if="bbsVisible===true"
                 append-to-body
                 customClass="customWidth">
        <sendBBS :bbsClass="bbsClass" :bbsClassName="bbsClassName"></sendBBS>
      </el-dialog>
      <h1>欢迎进入{{this.bbsClassName}}板块！</h1>
      <div class="search-header">
        <div class="search">
          <el-input v-model="search_input" placeholder="请输入内容" style="width:70%;"></el-input>
          <el-button type="primary" style="width:25%;">搜索</el-button>
        </div>
        <div class="send">
          <el-button type="primary" @click="bbsVisible=true"><i class="el-icon-edit-outline"></i>发帖</el-button>
          <el-button type="primary"><i class="el-icon-refresh" @click="refresh"></i>刷新</el-button>
        </div>
      </div>
      <div class="bbslist">
        <el-table :data="tableData.slice((currentPage-1)*PageSize,currentPage*PageSize)"
                  :show-header="true"
                  v-loading="loading"
                  element-loading-text="拼命加载中"
                  element-loading-spinner="el-icon-loading"
        >
          <el-table-column
            prop="bbsComments"
            label="评论数"
            width="250">
            <template slot-scope="scope">
              <i class="el-icon-chat-dot-square"></i>
              <span style="margin-left: 8px">{{ scope.row.bbsComments }}</span>
            </template>
          </el-table-column>
          <el-table-column
              prop="bbsName"
              label="帖子标题">
          </el-table-column>
          <el-table-column
            prop="bbsSender" label="发帖用户">
            <template slot-scope="scope">
              <i class="el-icon-user"></i>
              <span style="margin-left: 8px">{{ scope.row.bbsSender }}</span>
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
  import sendBBS from './sendBBS'
    export default {
      name: "bbsInfo",
      components:{sendBBS},
      mounted(){
        this.$api.bbs.getBBSByClassId({
          bbsId:this.bbsClass
        }).then((res)=>{
          if(res.data.status==0){
            this.loading = true
            let info = res.data.bbsinfo
            this.totalCount = info.length
            for(let i=0;i<info.length;++i){
              this.tableData.push({
                bbsComments:info[i]['TReplyCount'],
                bbsName:info[i]['TTopic'],
                bbsSender:info[i]['Unickname']
              })
            }
            this.loading=false
          }
          else{
            this.$message.error(res.data.message)
          }
        })
      },
      props:{
        bbsClass:{
          type:Number
        },
        bbsClassName:{
          type:String
        }
      },
      data(){
          return{
            search_input:'',
            bbsVisible:false,
            tableData:[],
            currentPage:1,
            totalCount:0,
            PageSize:8,
            pageSizes:[1,2,3,4],
            loading:false
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
        refresh(){
          this.loading = true
          let tableData = []
          this.$api.bbs.getBBSByClassId({
            bbsId:this.bbsClass
          }).then((res)=>{
            if(res.data.status==0){
              let info = res.data.bbsinfo
              this.totalCount = info.length
              for(let i=0;i<info.length;++i){
                tableData.push({
                  bbsComments:info[i]['TReplyCount'],
                  bbsName:info[i]['TTopic'],
                  bbsSender:info[i]['Unickname']
                })
              }
              this.tableData = tableData
              this.$message.success('刷新成功！')
            }
            else{
              this.$message.error(res.data.message)
            }
          })
          this.loading = false
        }
      }
    }
</script>

<style lang="scss">
  .bbsInfo{
    .el-input__inner{
      border-radius:30px;
    }
    .el-button{
      border-radius:30px;
    }
    width:100%;
    h1{
      font-size:28px;
      color:#36648B;
      text-align: left;
    }
    .search-header{
      margin-top:10px;
      width:100%;
      flex-direction: row;
      display:flex;
      justify-content: space-between;

      .search{
        width:50%;
        flex-direction: row;
        display:flex;
        justify-content: space-between;
      }
    }
    .bbslist{
      .el-table{
        margin-top:50px;
      }
    }
  }
</style>
