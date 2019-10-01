<template>
    <div class="bbsInfo">
      <div class="search-header">
        <div class="search">
          <el-input v-model="search_input" placeholder="请输入内容" style="width:70%;"></el-input>
          <el-button type="primary" style="width:25%;">搜索</el-button>
        </div>
        <div class="send">
          <el-button type="primary"><i class="el-icon-edit-outline"></i>发帖</el-button>
          <el-button type="primary"><i class="el-icon-refresh"></i>刷新</el-button>
        </div>
      </div>
      <h1>欢迎进入{{this.bbsClassName}}板块！</h1>
    </div>
</template>

<script>
    export default {
      name: "bbsInfo",
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
            search_input:''
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
  }
</style>
