import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import test from '@/components/test'
import index from '@/components/index'
import login from '@/components/login'
import register from '@/components/register'
import userInfo from '@/components/userInfo'
import classInfo from '@/components/classInfo'
import gameDetail from '@/components/gameDetail'
import community from '@/components/community'
import bbsDetail from '@/components/bbsDetail'

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
      path: '/classInfo/:classNum',
      name: 'classInfo',
      component: classInfo
    },
    {
      path: '/gameDetail/:gameId',
      name: 'gameDetail',
      component: gameDetail
    },
    {
      path: '/community',
      name: 'community',
      component: community
    },
    {
      path: '/bbsDetail/:bbsId',
      name: 'bbsDetail',
      component: bbsDetail
    },
  ]
})
