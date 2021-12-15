<template>
  <page-layout>
    <div class="mb-4">
      <div class="text-primary-700 flex items-center justify-left cursor-default">
          <logo class="h-12 w-12" alt="Django Guides Code Sample" />
          <span class="hidden lg:inline ml-3 text-4xl font-bold font-brand">Django Guides Code Sample</span>
      </div>
      <h2 class="mt-6 text-4xl font-extrabold text-secondary-800 font-title ml-3">
        Confirm Email
      </h2>
    </div>
    <alert :variant="variant" :icon="true" :accent="true">
      <template #default>{{ message }}</template>
    </alert>
  </page-layout>
</template>

<script>
import axios from 'axios'
import Alert from '@/components/Alert'
import FlashMessage from '@/utils/FlashMessage'
import Logo from '@/components/Logo'
import PageLayout from '@/layouts/PageLayout'

/**
 * Confirm email address landing point.
 *
 * @property  token  String  Email confirmation token
 */
export default {
  name: 'EmailConfirm',

  components: {
    Alert,
    Logo,
    PageLayout
  },

  props: {
    // Email confirmation token
    token: String
  },

  data () {
    return {
      // Status of the email confirmation request ("waiting", "success", or "error")
      status: 'waiting'
    }
  },

  computed: {
    // Which variant of the Alert to display
    variant () {
      switch (this.status) {
        case 'waiting': return 'info'
        case 'complete': return 'success'
        default: return 'danger'
      }
    },

    // Which message to display in the alert
    message () {
      switch (this.status) {
        case 'waiting': return 'Please wait while we confirm your email address.'
        case 'complete': return 'Email address confirmed.'
        default: return 'There was a problem confirming your email address.'
      }
    }
  },

  // Vue Lifecycle Hook: After the component is instantiated and placed in the DOM
  mounted () {
    axios.post('/api/auth/registration/verify-email/', {
      key: this.token
    }).then(function () {
      this.status = 'complete'
      FlashMessage.setFlashMessage('Thank you for confirming your email address')
      this.$router.push('/')
    }.bind(this)).catch(function () {
      this.status = 'error'
    }.bind(this))
  }
}
</script>
