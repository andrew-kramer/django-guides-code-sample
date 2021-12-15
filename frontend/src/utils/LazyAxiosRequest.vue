<script>
import axios from 'axios'
import GetCsrf from '@/utils/GetCsrf'

/**
 * Make a POST request through Axios, but delay requesting the CSRF token until the very last moment. This should
 * ideally be used for things like the Logout button, where we display a form and have no idea how long it will be
 * if/when the user finally clicks it.
 *
 * @param url     String  URL to send the data to
 * @param data    Object  The data package to send as the body of the POST request
 * @param method  String  Axios method (HTTP verb) to use
 *
 * @returns {Promise<AxiosResponse<any>>}
 */
export default async function (url, data, method = 'post') {
  const config = {
    headers: {
      'X-CSRFToken': GetCsrf(),
      credentials: 'same-origin'
    }
  }
  let promise
  switch (method.toLowerCase()) {
    case 'post':
      promise = axios.post(url, data, config)
      break
    case 'put':
      promise = axios.put(url, data, config)
      break
    case 'delete':
      promise = axios.delete(url, config)
      break
    default:
      console.error('Invalid axios method. NOT sending request')
  }
  return promise
}
</script>
