<template>
  <div class="gameUserInfo">
    <el-form :model='form' label-width="50px">
      <el-form-item label="昵称:" prop="nickName">
        {{this.form.nickName}}
      </el-form-item>
      <el-form-item label="性别:" prop="sex">
        {{this.form.sex}}
      </el-form-item>
      <el-form-item label="生日:" prop="birthday">
        {{this.form.birthday}}
      </el-form-item>
      <el-form-item label="签名:" prop="selfInfo">
        {{this.form.selfInfo}}
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
    export default {
      name: "gameUserInfo",
      mounted(){
        this.$api.user.getMessage({
          id:this.userId
        }).then((res)=>{
          if(res.data.status==0){
            console.log(res)
            let info = res.data
            this.form.nickName = info['Unickname'];
            let sex = info['USex']
            if(sex == 'M')
              this.form.sex = '男'
            else
              this.form.sex = '女'
            if(info['UBirthday'] !== 0)
              this.form.birthday = info['UBirthday']
            else this.form.birthday = new Date()
            this.form.selfInfo = info['UStatement']
          }
          else{
            this.$message.error(res.data.message)
          }
        })
      },
      props:{
        userId:{
          type:Number
        }
      },
      data(){
        return{
          form:{
            nickName:'',
            sex:'',
            birthday:'',
            selfInfo:''
          }
        }
      }
    }
</script>

<style scoped>

</style>
