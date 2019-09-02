<template>
  <div class="about">
    <h1>This is DataTest</h1>
    {{d2}}
    <p v-for="d in d1">
      {{d}}
    </p>
    <button @click="init">点击获取数据</button>
  </div>
</template>

<script>
  export default {
    name:'test',
    data:function () {
      return{
        d1:['默认列表数据1','默认列表数据2'],
        d2:'默认字符串',
      }
    },
    methods:{
      init:function(){
        this.$api.test.test({
        }).then((res)=>{
          if(res.data.status==200)
            console.log(res)
          let info = res.data.content
          console.log(info)
          this.d1 = info
        })
      }
    }
  }
</script>
<style scoped>

</style>
