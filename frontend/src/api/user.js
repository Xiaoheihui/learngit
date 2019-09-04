import axios from './http';
import qs from 'qs'

const user = {
  register(params){
    return axios.post('/api/register', qs.stringify(params))
  }
}

export default user;
