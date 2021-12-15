<template>
  <authentication-provider>
    <router-view v-bind="$attrs" />
  </authentication-provider>
</template>

<script>
import AuthenticationProvider from '@/providers/AuthenticationProvider'

export default {
  inheritAttrs: false,

  components: {
    AuthenticationProvider
  }
}
</script>

<style src="./assets/styles/app.css" lang="css" />
