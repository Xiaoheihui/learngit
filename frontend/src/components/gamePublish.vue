<template>
    <div class="gamePublish">
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <el-form-item label="比赛名称" prop="gameName">
          <el-input v-model="form.gameName" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="比赛类型"  prop="gameClass">
          <el-select v-model="form.gameClass" placeholder="请选择比赛类型">
            <el-option label="科技创新" value="科技创新"></el-option>
            <el-option label="创业商业" value="创业商业"></el-option>
            <el-option label="艺术爱好" value="艺术爱好"></el-option>
            <el-option label="游戏动漫" value="游戏动漫"></el-option>
            <el-option label="广告公益" value="广告公益"></el-option>
            <el-option label="学科竞赛" value="学科竞赛"></el-option>
            <el-option label="体育竞赛" value="体育竞赛"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="比赛地区"  prop="gameArea">
          <el-select v-model="form.gameArea" placeholder="请选择比赛地区">
            <el-option label="全国" value="全国"></el-option>
            <el-option label="北京" value="北京"></el-option>
            <el-option label="天津" value="天津"></el-option>
            <el-option label="上海" value="上海"></el-option>
            <el-option label="重庆" value="重庆"></el-option>
            <el-option label="河北" value="河北"></el-option>
            <el-option label="山西" value="山西"></el-option>
            <el-option label="辽宁" value="辽宁"></el-option>
            <el-option label="吉林" value="吉林"></el-option>
            <el-option label="黑龙江" value="黑龙江"></el-option>
            <el-option label="江苏" value="江苏"></el-option>
            <el-option label="浙江" value="浙江"></el-option>
            <el-option label="安徽" value="安徽"></el-option>
            <el-option label="福建" value="福建"></el-option>
            <el-option label="江西" value="江西"></el-option>
            <el-option label="山东" value="山东"></el-option>
            <el-option label="海南" value="海南"></el-option>
            <el-option label="四川" value="四川"></el-option>
            <el-option label="贵州" value="贵州"></el-option>
            <el-option label="云南" value="云南"></el-option>
            <el-option label="陕西" value="陕西"></el-option>
            <el-option label="甘肃" value="甘肃"></el-option>
            <el-option label="青海" value="青海"></el-option>
            <el-option label="台湾" value="台湾"></el-option>
            <el-option label="内蒙古" value="内蒙古"></el-option>
            <el-option label="广西" value="广西"></el-option>
            <el-option label="西藏" value="西藏"></el-option>
            <el-option label="宁夏" value="宁夏"></el-option>
            <el-option label="新疆" value="新疆"></el-option>
            <el-option label="香港" value="香港"></el-option>
            <el-option label="澳门" value="澳门"></el-option>
            <el-option label="全球" value="全球"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="比赛级别"  prop="gameLevel">
          <el-select v-model="form.gameLevel" placeholder="请选择比赛级别">
            <el-option label="A类" value="A类"></el-option>
            <el-option label="B类" value="B类"></el-option>
            <el-option label="C类" value="C类"></el-option>
            <el-option label="D类" value="D类"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="报名开始" prop="signUpBegin">
          <el-date-picker type="date" placeholder="选择日期"  v-model="form.signUpBegin" ></el-date-picker>
        </el-form-item>
        <el-form-item label="报名结束" prop="signUpEnd">
          <el-date-picker type="date" placeholder="选择日期"  v-model="form.signUpEnd" ></el-date-picker>
        </el-form-item>
        <el-form-item label="主办单位" prop="gameOrganizers">
          <el-input v-model="form.gameOrganizers" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="参赛对象" prop="gameObject">
          <el-input v-model="form.gameObject" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="参赛方法" prop="gameMethods">
          <el-input v-model="form.gameMethods" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="比赛时间" prop="gameSchedule">
          <el-input v-model="form.gameSchedule" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="参赛形式" prop="gameForm">
          <el-input v-model="form.gameForm" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="比赛官网" prop="gameUrl">
          <el-input v-model="form.gameUrl" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="比赛说明" prop="gameStatement">
          <el-input type="textarea" v-model="form.gameStatement" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <el-button type="primary" @click="submitForm('form')">发布</el-button>
    </div>
</template>

<script>
    export default {
      name: "gamePublish",
      data(){
        return{
          form:{
            gameName:'',
            gameClass:'',
            gameArea:'',
            gameLevel:'',
            signUpBegin:'',
            signUpEnd:'',
            gameOrganizers:'',
            gameObject:'',
            gameMethods:'',
            gameSchedule:'',
            gameForm:'',
            gameUrl:'',
            gameStatement:''
          },
          rules: {
            gameName: [
              { required: true, message: '请输入比赛名称', trigger: 'blur' },
              { min: 3, max: 20, message: '长度在 3 到 20 个字符', trigger: 'blur' }
            ],
            gameClass: [
              { required: true, message: '请选择比赛类型', trigger: 'change' }
            ],
            gameLevel: [
              { required: true, message: '请选择比赛级别', trigger: 'change' }
            ],
            gameArea: [
              { required: true, message: '请选择比赛地区', trigger: 'change' }
            ],
            signUpBegin: [
              { type: 'date', required: true, message: '请选择日期', trigger: 'change' }
            ],
            signUpEnd: [
              { type: 'date', required: true, message: '请选择日期', trigger: 'change' }
            ],
            gameOrganizers: [
              { required: true, message: '请输入主办单位', trigger: 'blur' },
            ],
            gameObject: [
              { required: true, message: '请输入参赛对象', trigger: 'blur' },
            ],
            gameMethods: [
              { required: true, message: '请输入参赛方法', trigger: 'blur' },
            ],
            gameSchedule: [
              { required: true, message: '请输入比赛时间', trigger: 'blur' },
            ],
            gameForm: [
              { required: true, message: '请输入参赛形式', trigger: 'blur' },
            ],
            gameUrl: [
              { required: true, message: '请输入比赛官网', trigger: 'blur' },
            ],
            gameStatement: [
              { required: true, message: '请输入比赛说明', trigger: 'blur' },
            ],
          }
        }
      },
      methods:{
        submitForm(formName){
          this.$refs[formName].validate((valid)=>{
            if(valid){
              this.$api.comp.uploadCompInfo({
                compName:this.form.gameName,
                compClass:this.form.gameClass,
                area:this.form.gameArea,
                level:this.form.gameLevel,
                startTime:this.form.signUpBegin,
                endTime:this.form.signUpEnd,
                organizers:this.form.gameOrganizers,
                object:this.form.gameObject,
                methods:this.form.gameMethods,
                schedule:this.form.gameSchedule,
                form:this.form.gameForm,
                compUrls:this.form.gameUrl,
                statement:this.form.gameStatement
              }).then((res)=>{
                if(res.data.status==0){
                  this.$message.success('比赛发布成功！')
                }
                else{
                  this.$message.error('发布失败，请重试！')
                }
              })
            }
            else{
              return false;
            }
          })
        }
      }
    }
</script>

<style scoped>

</style>
