import axios from './http';
import qs from 'qs'

const test = {
  test(params){
    return axios.post('/api/test', qs.stringify(params))
  }
}

export default test;
