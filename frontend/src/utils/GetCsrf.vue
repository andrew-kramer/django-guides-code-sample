<!--suppress JSUnresolvedFunction-->
<script>
import Cookie from 'js-cookie'

function getCsrf () {
  let tempCsrf = Cookie.get('csrftoken')
  if (!tempCsrf) {
    const csrfElement = document.querySelector('[name=csrfmiddlewaretoken]')
    if (csrfElement) {
      tempCsrf = csrfElement.value
    }
  }
  return tempCsrf
}
export default getCsrf
</script>
