<!--suppress MagicNumberJS -->
<template>
  <div class="mx-auto w-full max-w-sm">
    <title-block :title="title" :show-logo="showLogo" />

    <div class="mt-8">
      <div class="mb-2">
        <Alert variant="danger" :accent="true" :icon="true"
               v-if="displayedErrorMessages && displayedErrorMessages.length > 0">
          <div v-if="displayedErrorMessages.length === 1">
            <div v-for="item in displayedErrorMessages" :key="item">
              <p>{{ item}}</p>
            </div>
          </div>
          <div v-else>
            <div>The following errors have occurred:</div>
            <ul class="ml-5 list-disc" v-for="item in displayedErrorMessages" :key="item">
              <li>{{ item }}</li>
            </ul>
          </div>
        </Alert>
      </div>
      <div :class="'mt-2' + (isDisabled ? ' opacity-50' : '')">
        <easy-form :action="action" :method="method ? method : 'POST'" class="space-y-6" @success="onSuccess"
                   @error="onError" @disabled="setFormDisabled" @badRequest="onBadRequest">
          <div class="relative">
            <div class="relative space-y-6">
              <slot />
            </div>
            <div class="absolute top-0 left-0 right-0 bottom-0" v-if="isDisabled">
              <div class="flex justify-center items-center w-full h-full">
                <animated-spinner />
              </div>
            </div>
          </div>
          <div class="mt-1 flex flex-row-reverse justify-between gap-4">
            <button :class="['flex-1 py-1 px-2 border border-transparent rounded-md shadow-sm text-sm font-semibold ' +
                            'focus:outline-none focus:ring-2 focus:ring-offset-2', variantCancelClasses]"
                    :disabled="isDisabled" v-if="cancel" @click.prevent="onCancel">
              {{ cancel }}
            </button>
            <button type="submit"
                    :class="['flex-1 py-1 px-2 border border-transparent rounded-md shadow-sm text-sm font-bold ' +
                             'focus:outline-none focus:ring-2 focus:ring-offset-2', variantSubmitClasses]"
                    :disabled="isDisabled">
              {{ submit }}
            </button>
          </div>
        </easy-form>
      </div>
    </div>
  </div>
</template>

<script>
import Alert from '@/components/Alert'
import EasyForm from '@/components/forms/EasyForm'
import AnimatedSpinner from '@/components/AnimatedSpinner'
import { ref } from 'vue'
import TitleBlock from '@/components/TitleBlock'

/**
 * Standard Layout for a page with a form element
 *
 * @property   action        String  Where is the form sent? Equivalent to the HTML action property
 * @property   errorMessage  String  A generic error message to display instead of the specific messages if something
 *                                   goes wrong
 * @property  method         String  Method field just like in HTML - denotes the HTTP verb to use
 * @property  submit         String  The text to display on the submit button
 * @property  title          String  The text to display at the top of the content
 * @property  variant        String  Which variant of the form should we display? (default: none)
 *
 * @emits  disabled  Boolean  The form's disabled status has changed
 * @emits  error     Object   The form encountered an error
 * @emits  success   Null     The form was successfully submitted
 * @emits  cancel    Null     The form was canceled
 */
export default {
  name: 'FormContent',

  components: {
    TitleBlock,
    Alert,
    AnimatedSpinner,
    EasyForm
  },

  props: {
    // Where is the form sent? Equivalent to the HTML action property
    action: String,

    // A generic error message to display instead of the specific messages if something goes wrong
    errorMessage: String,

    // Method field just like in HTML - denotes the HTTP verb to use
    method: String,

    // The text to display on the submit button
    submit: String,

    // The text to display at the top of the content
    title: String,

    // Should we show the Site Logo?
    showLogo: {
      type: Boolean,
      default: true
    },

    // Cancel Button text
    cancel: {
      type: String,
      default: ''
    },

    // Which variant of the form should we display? (default: none)
    variant: {
      type: String,
      default: ''
    }
  },

  emits: {
    // The form's disabled status has changed
    disabled: payload => {
      return (payload === true || payload === false)
    },

    // The form encountered an error
    error: null,

    // The form was successfully submitted
    success: null,

    // The user exited the form without submitting
    cancel: null
  },

  data () {
    return {
      // General error messages received from the most recent form submission
      responseErrorMessages: [],

      // Field error messages received from the most recent form submission
      fieldErrors: ref({ value: { } }),

      generalErrors: [],

      // Is the form in a disabled state?
      disabled: ref({ value: false })
    }
  },

  computed: {
    // Which of the general error messages should be shown, given which ones we have stored?
    displayedErrorMessages () {
      let errors = []
      if (this.responseErrorMessages.length > 0 || this.generalErrors.length > 0) {
        if (this.errorMessage) {
          errors = [this.errorMessage]
        } else {
          errors = this.generalErrors.concat(this.responseErrorMessages)
        }
      }
      return errors
    },

    // Is the form disabled?
    isDisabled () {
      return this.disabled.value
    },

    // Cancel button color classes for the different variants
    variantCancelClasses () {
      switch (this.variant.toLowerCase()) {
        case 'danger':
          return 'text-secondary-700 bg-secondary-300 hover:bg-secondary-400 focus:ring-secondary-500'
        default:
          return 'text-secondary-700 bg-secondary-300 hover:bg-secondary-400 focus:ring-secondary-500'
      }
    },

    // Submit button color classes for the different variants
    variantSubmitClasses () {
      switch (this.variant.toLowerCase()) {
        case 'danger':
          return 'text-secondary-50 bg-red-700 hover:bg-red-800 focus:ring-red-600'
        default:
          return 'text-secondary-50 bg-primary-600 hover:bg-primary-700 focus:ring-primary-500'
      }
    }
  },

  methods: {
    // The form's Disabled status has changed, so update ours.
    setFormDisabled (newVal) {
      this.disabled.value = newVal
      this.$emit('disabled', newVal)
    },

    onCancel () {
      this.generalErrors = []
      this.responseErrorMessages = []
      this.$emit('cancel')
    },

    // The form was submitted successfully
    onSuccess (data) {
      this.generalErrors = []
      this.responseErrorMessages = []
      this.$emit('success', data)
    },

    // The login form or the API had some sort of problem.
    onError (error) {
      this.generalErrors = ['Something went wrong on our end. Sorry!']
      this.responseErrorMessages = []
      this.$emit('error', error)
    },

    // The user's submission was rejected.
    onBadRequest: function (errors) {
      let responseErrors = []
      // noinspection JSUnresolvedVariable
      if (errors.non_field_errors) {
        responseErrors = responseErrors.concat(errors.non_field_errors)
      }
      this.responseErrorMessages = responseErrors
      if (responseErrors.length === 0) {
        this.generalErrors = ['There was a problem submitting your information.']
      } else {
        this.generalErrors = []
      }
      this.fieldErrors.value = (errors || {})
    }
  },

  // Provide these two fields to children using the inject() method
  provide () {
    return {
      fieldErrors: this.fieldErrors,
      disabled: this.disabled
    }
  }
}
</script>
