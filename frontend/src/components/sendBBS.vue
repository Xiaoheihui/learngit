<template>
    <div class="sendBBS">
      <el-form ref="form" :model="form" :rules="rules" label-width="70px">
        <el-form-item label="板块:">
          {{this.bbsClassName}}
        </el-form-item>
        <el-form-item label="标题:" prop="bbsName">
          <el-input v-model="form.bbsName" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="内容:" prop="bbsContent">
          <el-input type="textarea" v-model="form.bbsContent"  placeholder="最长不能超过1500个字哦" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <el-button type="primary" style="width:50%;margin-left:25%;" @click="send('form')">发送</el-button>
    </div>
</template>

<script>
    export default {
      name: "sendBBS",
      props:{
        bbsClass:{
          type:Number
        },
        bbsClassName:{
          type:String
        }
      },
      mounted(){
        this.userId = sessionStorage.getItem('userId')
      },
      data(){
        var checkBBSName = (rule, value, callback) => {
          if (!value) {
            return callback(new Error('发帖标题不能为空'));
          }
          setTimeout(()=>{
            callback();
          },1000);
        };
        var checkBBSContent = (rule, value, callback) => {
          if (!value) {
            return callback(new Error('发帖内容不能为空'));
          }
          setTimeout(()=>{
            callback();
          },1000);
        };
        return{
          userId:null,
          tableData:[],
          form:{
            bbsName:'',
            bbsContent:''
          },
          rules:{
            bbsName: [
              { validator: checkBBSName, trigger: 'blur' }
            ],
            bbsContent: [
              { validator: checkBBSContent, trigger: 'blur' }
            ],
          },
        }
      },
    methods:{
        send(formName){
          if(!this.userId){
            this.$message.warning('登录后才可以发帖哦！')
            return
          }
          this.$refs[formName].validate((valid)=>{
            if(valid){
              this.$api.bbs.sendBBS({
                userId:this.userId,
                bbsClass:this.bbsClass,
                bbsName:this.form.bbsName,
                bbsContent:this.form.bbsContent,
              }).then((res)=>{
                if(res.data.status==0){
                  this.$emit('childsay', res.data.bbsinfo)
                  this.$message.success(res.data.message)
                }
                else{
                  this.$message.error(res.data.message)
                }
              })
            }
            else{
              this.$message.error('请完善发帖信息哦！')
            }
          })
        }
    }
    }
</script>

<style lang="scss">
  .el-button{
    border-radius:30px;
  }
</style>
