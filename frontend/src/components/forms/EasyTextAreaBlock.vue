<template>
  <div class="space-y-1">
    <label :for="$attrs.id" class="block text-sm font-medium text-secondary-700" v-if="$slots.label || label">
      <slot name="label">{{ label }}</slot>
    </label>
    <div class="mt-1">
        <textarea :class="['appearance-none block w-full px-3 py-2 border border-secondary-300 rounded-md shadow-sm ' +
                           'placeholder-secondary-400 focus:outline-none focus:ring-primary-500 ' +
                           'focus:border-primary-500 sm:text-sm resize-none'].concat(this.$attrs.class)"
                  v-bind="attrsWithoutClass" :disabled="isDisabled ? 'disabled' : false" :rows="rows"
                  v-model="presentValue" />
    </div>
    <div class="mt-1 text-sm text-secondary-400 text-right">
      You have {{ charsLeft }} characters remaining.
    </div>
    <div class="mt-1" v-if="$slots.errors || (errorMessages.length)">
      <slot name="errors">
        <ul class="text-sm text-red-600 ml-3">
          <li v-for="item in errorMessages" :key="item">{{ item }}</li>
        </ul>
      </slot>
    </div>
  </div>
</template>

<script>
/**
 * An input block with containing div and an internal textarea, plus character counter. The slots are all optional and
 * intended to allow customization:
 *   - If you omit the label slot, it will try to use the label property to fill the slot but will otherwise leave it
 *     blank.
 *   - If you omit the errors slot, this component will present any errors in the standard <ul><li> format.
 *
 * @property  label      String  The text of the label to apply. If the "label" slot is filled, this is ignored.
 * @property  errors     Array   A list of error messages to display for this field.
 * @property  rows       Number  How many rows of the textarea should we display? (Default: 3)
 * @property  maxLength  Number  How many characters are allowed in the textarea? (Default: 500)
 * @property  value      String  The INITIAL value of the field.
 *
 * @template  label   Overrides the default display of the label
 * @template  errors  Overrides the default <ul><li> list for displaying validation errors
 */
export default {
  name: 'EasyTextAreaBlock',

  inheritAttrs: false,

  props: {
    // The text of the label to apply. If the "label" slot is filled, this is ignored
    label: String,

    // A list of error messages to display for this field
    errors: Array,

    // How many rows of the textarea should we display? (Default: 3)
    rows: {
      type: Number,
      default: 3
    },

    // How many characters are allowed in the textarea? (Default: 500)
    maxLength: {
      type: Number,
      default: 500
    },

    // The INITIAL value of the field
    value: {
      type: String,
      default: ''
    }
  },

  data () {
    return {
      // Characters remaining before we hit the max length
      presentValue: this.value
    }
  },

  inject: [
    // Errors returned from the server regarding the input fields
    'fieldErrors',

    // Whether the form is disabled
    'disabled'
  ],

  computed: {
    // Array to use for v-bind instead of $attrs
    attrsWithoutClass () {
      // Because $attrs is a Proxy, we enumerate it and assign instead of a more direct copy method
      const clone = {}
      for (const i in this.$attrs) {
        if (Object.prototype.hasOwnProperty.call(this.$attrs, i) && i !== 'class') {
          clone[i] = this.$attrs[i]
        }
      }
      return clone
    },

    charsLeft () {
      return Math.max(this.maxLength - this.presentValue.length, 0)
    },

    // Is this field disabled?
    isDisabled () {
      return this.disabled?.value
    },

    // Combine our sources of error messages into one list of messages to display
    errorMessages () {
      const allErrors = []
      if (this.errors !== undefined) {
        for (const i in this.errors) {
          allErrors.push(this.errors[i])
        }
      }
      const errorList = this.fieldErrors?.value[this.$attrs.name]
      for (const i in errorList) {
        if (Object.prototype.hasOwnProperty.call(errorList, i)) {
          allErrors.push(errorList[i])
        }
      }
      return allErrors
    }
  }
}
</script>
