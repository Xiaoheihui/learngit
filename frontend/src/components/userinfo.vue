<template>
    <div class="userInfo">
      <el-form ref="'form" :model="form" :rules="rules" label-width="80px">
        <el-form-item label="昵称" prop="nickName">
          <el-input v-model="form.nickName" autocomplete="off" :disabled="!judge"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="sex">
          <el-switch v-model="form.sex" active-text="男" inactive-text="女" inactive-color="#13ce66" :disabled="!judge"></el-switch>
        </el-form-item>
        <el-form-item label="生日" prop="birthday">
          <el-date-picker type="date" placeholder="选择日期" v-model="form.birthday" style="width:100%;" :disabled="!judge"></el-date-picker>
        </el-form-item>
        <el-form-item label="备注" prop="selfInfo">
          <el-input type="textarea" v-model="form.selfInfo" autocomplete="off" :disabled="!judge"></el-input>
        </el-form-item>
      </el-form>
      <el-button type="primary" @click="judge=true" :disabled="judge">编辑</el-button>
      <el-button type="primary" @click="test" :disabled="!judge">保存</el-button>
    </div>
</template>

<script>
    export default {
        name: "userinfo",
      mounted(){
          this.form.birthday = new Date()
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
            form:{
              nickName:'',
              sex:false,
              birthday:'',
              selfInfo:''
            },
            rules:{
              nickName: [
                { validator: checkNickName, trigger: 'blur' }
              ],
            }
          }
      },
      methods:{
          test(){

          }
      }
    }
</script>

<style scoped>

</style>
