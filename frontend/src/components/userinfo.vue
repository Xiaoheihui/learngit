<template>
    <div class="userInfo">
      <el-form ref="'form" :model="form" :rules="rules" label-width="80px">
        <el-form-item label="昵称" prop="nickName">
          <el-input v-model="form.nickName" autocomplete="off" :disabled="!judge"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="sex">
          <el-switch v-model="form.sex" active-text="男" inactive-text="女" inactive-color="#f56c6c" :disabled="!judge"></el-switch>
        </el-form-item>
        <el-form-item label="生日" prop="birthday">
          <el-date-picker type="date" placeholder="选择日期" :picker-options="pickerOptions" v-model="form.birthday" style="width:100%;" :disabled="!judge"></el-date-picker>
        </el-form-item>
        <el-form-item label="备注" prop="selfInfo">
          <el-input type="textarea" v-model="form.selfInfo"  placeholder="最长不能超过150个字符" autocomplete="off" :disabled="!judge"></el-input>
        </el-form-item>
      </el-form>
      <el-button type="primary" @click="judge=true" :disabled="judge">编辑</el-button>
      <el-button type="primary" @click="submitForm('form')" :disabled="!judge">保存</el-button>
    </div>
</template>

<script>
    export default {
        name: "userinfo",
      mounted(){
          this.userId = sessionStorage.getItem('userId')
        this.$api.user.getMessage({
          id:this.userId
        }).then((res)=>{
          if(res.data.status==0){
            let info = res.data
            this.form.nickName = info['nickname']
            let sex = info['sex']
            if(sex=='M')
              this.form.sex = true
            else this.form.sex = false
            this.form.birthday = new Date(Date.parse(info['birthday']))
            this.form.selfInfo = info['statement']
          }
          else{
            console.log(res.data.message)
          }
        })
      },
      data(){
        var checkNickName = (rule, value, callback) => {
          if (!value) {
            return callback(new Error('用户昵称不能为空'));
          }
          setTimeout(()=>{
            callback();
          },1000);
        };
          return{
            judge:false,
            userId:null,
            form:{
              nickName:'',
              sex:true,
              birthday:'',
              selfInfo:'',
              sexString:''
            },
            rules:{
              nickName: [
                { validator: checkNickName, trigger: 'blur' }
              ],
            },
            pickerOptions: {
              disabledDate(time) {
                return time.getTime() > Date.now();
              },
            }
          }
      },
      methods:{
        submitForm(formName) {
          this.$refs[formName].validate((valid) => {
            if (valid) {
              if(this.form.sex)
                this.sexString = 'M'
              else this.sexString = 'F'
              this.$api.user.alterMessage({
                nickname:this.form.nickname,
                sex:this.sexString,
                statement:this.form.selfInfo,
                birthday:this.form.birthday
              }).then((res)=>{
                  if(res.data.status==0){
                    this.$message.success('用户信息修改成功！')
                    this.judge = false
                  }else {
                    this.$message.error(res.data.message);
                  }
                }
              )
            } else {
              this.$message.error('请完善信息！');
            }

          })

        },
      }
    }
</script>

<style scoped>

</style>
