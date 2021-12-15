<!--suppress JSUnresolvedFunction -->
<script>
import Cookie from 'js-cookie'

function setFlashMessage (message) {
  // NOTE: Same-Site isn't implemented yet in the latest release of js-cookie. However, it appears to be slated for
  //       release sometime soon, as documentation appears on the master branch. -- ADK 07/12/2021
  Cookie.set('__flash_message', message, { sameSite: 'strict' })
}

function getFlashMessage () {
  const message = Cookie.get('__flash_message')
  Cookie.remove('__flash_message')
  return message
}

export default {
  getFlashMessage: getFlashMessage.bind(Cookie),
  setFlashMessage: setFlashMessage.bind(Cookie)
}
</script>
