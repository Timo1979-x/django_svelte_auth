import axios from "axios";

axios.defaults.baseURL = 'http://localhost:8000/api/'
axios.interceptors.response.use((resp) => resp, async err => {
  if (err.response.status === 401) {
    const { data, status } = await axios.post('refresh', {}, { withCredentials: true })
    if (status == 200) {
      axios.defaults.headers.common["Authorization"] = `Bearer ${data.token}`;
      // retry previous request:
      return axios(err.config)
    }
  }
  return err;
} );