<template>
    <div class="myBBS">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="我的发帖" name="first">
          <el-table :data="tableData1">
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
          }
      },
      methods:{
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
