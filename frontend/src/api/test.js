import axios from './http';
import qs from 'qs'

const test = {
  test(){
    return axios.post('/api/test')
  }
}

export default test;
