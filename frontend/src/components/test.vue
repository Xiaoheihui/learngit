<template>
  <div class="about">
    <h1>This is DataTest</h1>
    {{d2}}
    <p v-for="d in d1">
      {{d}}
    </p>
    <button @click="init">点击获取数据</button>
    <el-upload
      class="avatar-uploader"
      action="no"
      :show-file-list="false"
      :on-success="handleAvatarSuccess"
      :before-upload="beforeAvatarUpload">
      <img v-if="imageUrl" :src="imageUrl" class="avatar">
      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
    </el-upload>

  </div>
</template>

<script>
  export default {
    name:'test',
    data:function () {
      return{
        d1:['默认列表数据1','默认列表数据2'],
        d2:'默认字符串',
        imageUrl:''
      }
    },
    methods:{
      handleAvatarSuccess(res, file) {
        this.imageUrl = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        let fd = new FormData()
        fd.append('img', file)
        fd.append('id', 1)
        console.log(fd.get('img'))
        let config = {
          headers:{'Content-Type':'multipart/form-data'} //这里是重点，需要和后台沟通好请求头，Content-Type不一定是这个值
        };
        this.$axios.post('http://127.0.0.1:8080/api/api/upLoadImage', fd, config).then((res)=>{

        })
        return isJPG && isLt2M;
      },
      init:function(){
        this.$api.user.register({
          username:'xzh161',
          email:'1432564581@qq.com',
          password:'xzh123'
        }).then((res)=>{
          if(res.data.status==0)
          {
            console.log(res)
            let info = res.data.content
            this.d1 = info
            this.$message.success('注册成功！')
          }
          else{
            this.$message.error(res.data.message)
          }

        })
      }
    }
  }
</script>
<style lang="scss">
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>
