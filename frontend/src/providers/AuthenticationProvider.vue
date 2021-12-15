<!--suppress MagicNumberJS -->
<template>
  <slot />
</template>

<script>
import axios from 'axios'

/**
 * Authentication Provider component. By wrapping this around the App, we get authentication information to any child
 * components that need it.
 */
export default {
  name: 'AuthenticationProvider',

  data () {
    return {
      // The main Object provided to child components
      auth: {
        // Has the authentication stuff loaded yet?
        hasLoaded: false,

        // User information (pk, username, email, first_name, last_name)
        user: null,

        // We provide the login function so that the Login page can easily pass information up.
        login: this.login,

        // We provide the logout function so that the Logout page can easily pass information up.
        logout: this.logout
      },

      // Cancel token for the interval we create to periodically refresh the API token
      cancelToken: null
    }
  },

  provide () {
    return {
      // Provide the auth object to child components
      auth: this.auth
    }
  },

  methods: {
    // Query the server for the user data associated with this authentication token
    async getUser () {
      try {
        const response = await axios.get('/api/auth/user/')
        return response.data
      } catch {
        return null
      }
    },

    // Attempt to refresh a token
    async tryRefresh () {
      try {
        const response = await axios.post('/api/auth/token/refresh/', {})
        return response.data
      } catch {
        return null
      }
    },

    // Load Authentication information from the stored Refresh token (if any)
    async loadFromRefresh () {
      const refreshResults = await this.tryRefresh()

      if (refreshResults) {
        // noinspection JSUnresolvedVariable
        const tokenDurationMs = new Date(refreshResults.access_token_expiration)?.getTime() - new Date()?.getTime()
        // Refresh 30 seconds early, but not less than 5 seconds
        this.setRefreshTimeout(Math.max(tokenDurationMs - 30000, 5000))
      }
      return !!refreshResults
    },

    // Load Authentication
    async loadAuthentication () {
      if (await this.loadFromRefresh()) {
        this.auth.user = await this.getUser()
      }
      this.auth.hasLoaded = true
    },

    // Clear the timeout for token refreshes
    clearRefreshTimeout () {
      if (this.cancelToken) {
        clearTimeout(this.cancelToken)
      }
    },

    // Set the timeout for the next token refresh
    setRefreshTimeout (milliseconds) {
      this.clearRefreshTimeout()
      this.cancelToken = setTimeout(this.loadAuthentication, milliseconds)
    },

    // Logout and forget all authentication information. Note that this is passed down to other components and can be
    // called from, e.g. the Logout page.
    logout () {
      // Internal Data
      this.auth.user = null
    },

    // Login and store all authentication information. Note that this is passed down to other components and can be
    // called from, e.g. the Login and Register pages.
    login (loginData) {
      // Internal Data
      this.auth.user = loginData.user
      this.setRefreshTimeout(270000) // 4.5 minutes by default
    }
  },

  // Lifecycle Hook: Before mounting this component, start loading the Authentication
  beforeMount () {
    this.loadAuthentication()
  },

  // Lifecycle Hook: After unmounting, clear the timeout
  unmounted () {
    this.clearRefreshTimeout()
  }
}
</script>
