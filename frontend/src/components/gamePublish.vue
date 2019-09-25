<template>
    <div class="gamePublish">
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <el-form-item label="比赛名称" prop="gameName">
          <el-tag>{{this.username}}</el-tag>
        </el-form-item>
        <el-form-item label="报名开始时间" prop="signUpBegin">
          <el-tag>{{this.email}}</el-tag>
        </el-form-item>
        <el-form-item label="报名结束时间" prop="signUpEnd">
          <el-tag>{{this.email}}</el-tag>
        </el-form-item>
        <el-form-item label="比赛等级" prop="gameLevel">
          <el-input v-model="form.nickName" autocomplete="off" :disabled="!judge"></el-input>
        </el-form-item>
        <el-form-item label="比赛地区" prop="gameArea">
          <el-input v-model="form.nickName" autocomplete="off" :disabled="!judge"></el-input>
        </el-form-item>
        <el-form-item label="主办单位" prop="gameArea">
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
    </div>
</template>

<script>
    export default {
        name: "gamePublish"
    }
</script>

<style scoped>

</style>
