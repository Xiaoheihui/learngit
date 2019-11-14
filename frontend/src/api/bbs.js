import axios from './http';
import qs from 'qs'

const bbs = {
  //用户发送帖子信息
  sendBBS(params){
    return axios.post('/api/sendBBS', qs.stringify(params))
  },
  //根据板块ID获取帖子信息
  getBBSByClassId(params){
    return axios.post('/api/getBBSByClassId', qs.stringify(params))
  },
  //根据用户ID获取帖子信息
  getBBSByUserId(params){
    return axios.post('/api/getBBSByUserId', qs.stringify(params))
  },
  //根据帖子ID删除帖子信息与回帖信息
  deleteBBS(params){
    return axios.post('/api/deleteBBS', qs.stringify(params))
  },
  // 根据帖子ID获取帖子回复信息
  getReplyByBBSId(params){
    return axios.post('/api/getReplyByBBSId', qs.stringify(params))
  },
  // 根据用户ID发表评论
  uploadReply(params){
    return axios.post('/api/uploadReply', qs.stringify(params))
  },
  // 根据帖子ID获取帖子信息
  getBBSByBBSId(params){
    return axios.post('/api/getBBSByBBSId', qs.stringify(params))
  },
}

export default bbs;
