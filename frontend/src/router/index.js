import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import test from '@/components/test'
import index from '@/components/index'
import login from '@/components/login'
import register from '@/components/register'
import userInfo from '@/components/userInfo'
import classInfo from '@/components/classInfo'

Vue.use(Router)

export default new Router({
  mode:"history",
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/user',
      name: 'userInfo',
      component: userInfo
    },
    {
      path: '/classInfo',
      name: 'classInfo',
      component: classInfo
    },
  ]
})
