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

}

export default user;
