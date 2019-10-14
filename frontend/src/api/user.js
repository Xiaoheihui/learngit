import axios from './http';
import qs from 'qs'

const user = {
  //用户注册
  register(params){
    return axios.post('/api/register', qs.stringify(params))
  },
  //用户登录
  login(params){
    return axios.post('/api/login', qs.stringify(params))
  },
  //修改用户信息
  alterMessage(params){
    return axios.post('/api/alterMessage', qs.stringify(params))
  },
  //获取用户信息
  getMessage(params){
    return axios.post('/api/getMessage', qs.stringify(params))
  },
  //收藏单场比赛
  addFavorite(params) {
    return axios.post('/api/markComp', qs.stringify(params))
  },
  //取消单条收藏比赛记录
  deleteFavorite(params){
    return axios.post('/api/DeleteMarkMessage', qs.stringify(params))
  },
  //获取用户收藏比赛信息
  getFavorite(params){
    return axios.post('/api/getMarkMessage', qs.stringify(params))
  },
}

export default user;
