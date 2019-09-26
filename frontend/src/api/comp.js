import axios from './http';
import qs from 'qs'

const comp = {
  //获取单个赛事信息
  getCompInfoByCompId(params){
    return axios.post('/api/getCompInfoByCompId', qs.stringify(params))
  },
  //获取分类赛事信息
  getCompInfoByClassId(params){
    return axios.post('/api/getCompInfoByClassId', qs.stringify(params))
  }
}

export default comp;
