<template>
    <div class="sendReply">
      <el-input placeholder="请在这输入你的评论..." type="textarea" v-model="replyString"></el-input>
      <div class="buttonGroup">
        <el-button type="primary" @click="sendReply">评论</el-button>
      </div>

    </div>
</template>

<script>
    export default {
      name: "sendReply",
      props:{
        userId:{
          type:Number
        },
        bbsId:{
          type:Number
        }
      },
      data(){
        return{
          replyString:'',
        }
      },
      methods:{
        sendReply(){
          if(!this.userId){
            this.$message.error('请先登录后再回复哦！')
            return false
          }
          else{
            if(!this.replyString){
              this.$message.error('回复内容不能为空哦！')
            }
            else{
              this.$api.bbs.uploadReply({
                userId:this.userId,
                bbsId:this.bbsId,
                content:this.replyString
              }).then((res)=>{
                if(res.data.status===0){
                  this.$message.success('回复成功！')
                }
                else{
                  this.$message.error('回复失败，请重试！')
                }
              })
            }
          }
        }
      }
    }
</script>

<style lang="scss">
  .sendReply{
    margin-top:50px;
    width:86%;
    margin-left: 7%;
    .el-button{
      margin-top:20px;
      border-radius: 30px;
      width:20%;
    }
    .buttonGroup{
      display:flex;
      align-items:center;
      justify-content:flex-end;
      flex-direction: row;
    }
  }
</style>
