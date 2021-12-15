<!--suppress MagicNumberJS -->
<template>
  <form action="#" @submit.prevent="onSubmit">
    <slot />
  </form>
</template>

<script>
import axios from 'axios'
import GetCsrf from '@/utils/GetCsrf'

/**
 * Provides much of the functionality of an HTML form for use with our API
 *
 * @property  action            String    Where is the form sent? Equivalent to the HTML action property.
 * @property  method            String    How is the form sent? [POST, PUT]
 * @property  formDataCallback  Function  Function to gather all the form data and return it as { field: value }
 *
 * @emits badRequest  Object   The form submitted properly but the API says there was something wrong with the
 *                             submission
 * @emits disabled    Boolean  The form has become either disabled or enabled
 * @emits error       Error    Something went wrong submitting the form
 * @emits success     Object   Submitted successfully
 */
export default {
  name: 'EasyForm',

  props: {
    // Where is the form sent? Equivalent to the HTML action property.
    action: String,

    // How is the form sent? [POST, PUT, etc.]
    method: String,

    // Function to gather all the form data and return it as { field: value }
    formDataCallback: Function
  },

  data () {
    return {
      // Is the form waiting on a response from the API?
      isAwaitingResponse: false
    }
  },

  emits: {
    // The Disabled status of this form has changed
    disabled: payload => {
      return (payload === true || payload === false)
    },

    // The form was successfully submitted
    success: payload => {
      return (payload instanceof Object)
    },

    // There was an error submitting the form
    error: payload => {
      return (payload instanceof Error)
    },

    // The form was submitted successfully but rejected by the API because of problems with the inputs
    badRequest: payload => {
      return (payload instanceof Object)
    }
  },

  computed: {
    // Get the value of the CSRF token
    csrf () {
      return GetCsrf()
    },

    // Is this form in a disabled state?
    isDisabled () {
      return this.isAwaitingResponse
    }
  },

  methods: {
    // The form came back with a response. We're no longer waiting.
    clearAwaiting () {
      this.isAwaitingResponse = false
      this.$emit('disabled', this.isDisabled)
    },

    // Gather the values from the form elements
    getFormValues (event) {
      if (this.formDataCallback !== undefined) {
        return this.formDataCallback(event)
      }

      const values = {}
      const elements = event.target.elements

      for (const i in elements) {
        if (Object.prototype.hasOwnProperty.call(elements, i) && elements[i] !== undefined) {
          if (!isNaN(parseInt(i)) && elements[i].type !== 'submit') {
            if (elements[i].type.toLowerCase() === 'checkbox') {
              values[elements[i].name] = !!elements[i].checked
            } else if (elements[i].name && elements[i].value) {
              values[elements[i].name] = elements[i].value
            }
          }
        }
      }
      return values
    },

    // Wrapper for axios methods post, put, delete, etc.
    submitForm (formData, config) {
      switch (this.method.toLowerCase()) {
        case 'post': return axios.post(this.action, formData, config)
        case 'put': return axios.put(this.action, formData, config)
        case 'delete': return axios.delete(this.action, config)
        default:
          console.error('Warning: Invalid submit method: ' + this.method)
          return new Promise(function () {
            throw Error('Invalid submit method: ' + this.method)
          })
      }
    },

    // Send in the form
    trySubmission (formData) {
      const headers = {
        'X-CSRFToken': this.csrf
      }
      this.submitForm(formData, {
        headers: headers
      }).then((response) => {
        this.$emit('success', response.data)
      }).catch((error) => {
        if (error.response && error.response.status === 400) {
          this.$emit('badRequest', error.response.data)
        } else {
          this.$emit('error', error)
        }
      }).finally(() => {
        this.clearAwaiting()
      })
    },

    // User submitted the form
    onSubmit (event) {
      const formData = this.getFormValues(event)

      this.isAwaitingResponse = true
      this.$emit('disabled', this.isDisabled)
      this.trySubmission(formData)
      event.stopPropagation()
    }
  }
}
</script>
