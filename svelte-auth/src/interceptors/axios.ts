import axios from "axios";

axios.defaults.baseURL = 'http://localhost:8000/api/'

let refresh = false;

axios.interceptors.response.use((resp) => resp, async err => {
  if (err.response.status === 401) {
    console.log(`interceptor: got 401 status, refresh = ${refresh}`);
    if (!refresh) {
      refresh = true;
      console.log(`interceptor: will refresh token, refresh = ${refresh}`)
      const { data, status } = await axios.post('refresh', {}, { withCredentials: true })
      if (status == 200) {
        axios.defaults.headers.common["Authorization"] = `Bearer ${data.token}`;
        // retry previous request:
        console.log('interceptor: will retry previous request');
        let a1 = axios(err.config)
        console.log(a1)
        return a1
      }
    }
  }
  refresh = false;
  return err;
} );