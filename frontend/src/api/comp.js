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
  },
  //筛选获取赛事信息
  getCompInfoBySelect(params){
    return axios.post('/api/getCompInfoBySelect', qs.stringify(params))
  },
  //获取最新赛事信息
  getNewestComp(params){
    return axios.post('/api/getNewestComp', qs.stringify(params))
  },
  //获取最热赛事信息
  getHotestComp(params){
    return axios.post('/api/getHotestComp', qs.stringify(params))
  }
}

export default comp;
