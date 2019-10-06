<template>
    <div class="myBBS">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="我的发帖" name="first">
          <el-table :data="tableData1">
            <el-table-column prop="bbsName"
                             label="帖子标题"></el-table-column>
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
                bbsName:info[i]['TTopic']
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
        }
      }
    }
</script>

<style lang="scss">

</style>
