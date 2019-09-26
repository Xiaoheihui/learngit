import axios from './http';
import qs from 'qs'

const comp = {
  //用户注册
  register(params){
    return axios.post('/api/register', qs.stringify(params))
  },
  //用户登录
  getCompInfoByClassId(params){
    return axios.post('/api/getCompInfoByClassId', qs.stringify(params))
  }
}

export default comp;
