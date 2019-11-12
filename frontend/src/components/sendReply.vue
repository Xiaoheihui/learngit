<template>
    <div class="sendReply">
      <el-input placeholder="请在这输入你的评论..." type="textarea"></el-input>
      <el-button type="primary">评论</el-button>
    </div>
</template>

<script>
    export default {
        name: "sendReply"
    }
</script>

<style lang="scss">
  .sendReply{
    margin-top:30px;
    width:86%;
    margin-left: 7%;
    .el-button{
      margin-top:20px;
      border-radius: 30px;
      width:20%;
    }
  }
</style>
