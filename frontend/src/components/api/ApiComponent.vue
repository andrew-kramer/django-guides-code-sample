<template>
  <div class="hidden" />
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

/**
 * Handles a single query to the API and refreshes the data at regular intervals.
 *
 * @property  url      String  URL to query for the API.
 * @property  refresh  Number  How long (in milliseconds) to wait between querying the API. Defaults to 2000.
 * @property  queryId  Object  Set this to any arbitrary value; change it to invalidate the token and re-query
 *
 * @emits change  {queryId, data}  The data returned by the API query is different from what it was before
 * @emits error   Error            Something went wrong loading the query
 */
export default {
  name: 'ApiComponent',

  props: {
    // URL to query for the API
    url: String,

    // How long (in milliseconds) to wait between querying the API. Defaults to 2000.
    refresh: [String, Number],

    // Set this to any arbitrary value; change it to invalidate the token and re-query
    queryId: [String, Number]
  },

  data () {
    return {
      // Tokens for cancelling all pending Axios requests
      axiosCancelTokens: [],

      // Token so we can cancel the Interval when we shut down
      intervalToken: null,

      // Data models from the last query for comparison
      models: [],

      // Should we send errors up the chain? (Used mainly for shutting down)
      suppressErrors: false
    }
  },

  emits: {
    // The data returned by the API query is different from what it was before
    change: payload => {
      return (payload instanceof Object && payload.queryId !== undefined && payload.data instanceof Object)
    },

    // Something went wrong loading the query
    error: payload => {
      return (payload instanceof Error)
    }
  },

  computed: {
    // Integer value of the refresh property. (Defaults to 2000)
    intRefresh () {
      if (this.refresh === undefined) {
        // noinspection MagicNumberJS
        return 2000
      }
      return parseInt(this.refresh)
    },

    // Get a String representation of the QueryId
    stringQueryId () {
      if (this.queryId === undefined) {
        return ''
      }
      if (this.queryId instanceof String) {
        return this.queryId
      }
      const floatVal = parseFloat(this.queryId.toString())
      if (!isNaN(floatVal)) {
        return floatVal.toString()
      }
      return JSON.stringify(this.queryId)
    }
  },

  methods: {
    // Send an Axios query to the API
    queryApi () {
      if (this.url !== '') {
        const newToken = axios.CancelToken.source()
        this.axiosCancelTokens.push(newToken)
        axios.get(this.url, { cancelToken: newToken.token })
          .then(function (result) {
            if (!_.isEqual(result.data, this.models)) {
              this.models = result.data
              this.$emit('change', { queryId: this.stringQueryId, data: result.data })
            }
          }.bind(this))
          .catch(function (reason) {
            if (!this.suppressErrors) {
              this.$emit('error', reason)
            }
          }.bind(this))
      }
    },

    // Cancel all API requests
    cancelApiRequests () {
      for (const i in this.axiosCancelTokens) {
        if (Object.prototype.hasOwnProperty.call(this.axiosCancelTokens, i)) {
          this.axiosCancelTokens[i].cancel()
        }
      }
    },

    // Create an interval to repeatedly query the API every few seconds
    startInterval () {
      this.queryApi()
      if (this.intRefresh > 0 && this.intervalToken == null) {
        this.intervalToken = setInterval(function () {
          this.queryApi()
        }.bind(this), this.intRefresh)
      }
    },

    // Clear if there is an outstanding interval
    clearInterval () {
      if (this.intervalToken) {
        clearInterval(this.intervalToken)
        this.intervalToken = null
      }
    }
  },

  watch: {
    // If Refresh changes, we have to redo the intervals
    refresh (val, old) {
      if (!_.isEqual(val, old)) {
        this.clearInterval()
        this.startInterval()
      }
    },

    // QueryId has changed; this is useful for reloading the query when refresh is not enabled
    queryId (val, old) {
      if (!_.isEqual(val, old)) {
        this.startInterval()
      }
    }

    // NOTE: We don't have to do anything special if the URL changes, as the queryApi function will automatically
    // start using the new URL
  },

  // Lifecycle Hook. This fires after this component is instantiated.
  mounted () {
    this.startInterval()
  },

  // Lifecycle Hook. This fires after this component is removed from the DOM.
  unmounted () {
    this.suppressErrors = true
    this.clearInterval()
    this.cancelApiRequests()
  }
}
</script>
