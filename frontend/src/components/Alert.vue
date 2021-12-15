<template>
  <div :class="boxClasses">
    <div class="flex items-center gap-3">
      <div class="flex-shrink-0" v-if="isIconActive">
        <CheckCircleIcon :class="iconClasses" aria-hidden="true" v-if="effectiveVariant === 'success'" />
        <FireIcon :class="iconClasses" aria-hidden="true" v-else-if="effectiveVariant === 'danger'" />
        <ExclamationIcon :class="iconClasses" aria-hidden="true" v-else-if="effectiveVariant === 'alert'" />
        <InformationCircleIcon :class="iconClasses" aria-hidden="true" v-else />
      </div>
      <div class="flex-grow text-left">
        <p :class="textClasses">
          <slot />
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { CheckCircleIcon, ExclamationIcon, FireIcon, InformationCircleIcon } from '@heroicons/vue/solid'

/**
 * An Alert box with a message
 *
 * @property accent   Boolean  Show a small accent border along the left-hand side?
 * @property icon     Boolean  Show an icon to the left of the text?
 * @property variant  String   Which variant to show? Can be Danger, Warning, or Info (default).
 */
export default {
  name: 'Alert',

  components: {
    CheckCircleIcon,
    ExclamationIcon,
    FireIcon,
    InformationCircleIcon
  },

  props: {
    // Show a small accent border along the left-hand side?
    accent: Boolean,

    // Show an icon to the left of the text?
    icon: Boolean,

    // Which variant to show? Can be Danger, Warning, or Info (default).
    variant: String
  },

  computed: {
    // Compute the classes to use on the main div
    boxClasses () {
      return [
        'bg-' + this.color + '-50',
        'p-4',
        this.isAccentActive ? 'border-' + this.color + '-200' : '',
        this.isAccentActive ? 'border-l-4' : ''
      ]
    },

    // Compute the classes to use on the icons
    iconClasses () {
      return ['h-5', 'w-5', 'text-' + this.color + '-400']
    },

    // Compute the classes to use on the text
    textClasses () {
      return [
        'text-sm',
        'text-' + this.color + '-700'
      ]
    },

    // Is the accent actually active?
    isAccentActive () {
      // Default true
      return (this.accent !== undefined && this.accent)
    },

    // Is the icon actually active?
    isIconActive () {
      // Default false
      return (!!(this.icon === undefined || this.icon))
    },

    // Finds the standardized version of the variant name
    effectiveVariant () {
      if (typeof this.variant !== 'string') {
        return 'info'
      }
      const lower = this.variant.toLowerCase()
      switch (lower) {
        case 'alert': return 'alert'
        case 'danger': return 'danger'
        case 'info': return 'info'
        case 'success': return 'success'
        default: return 'info'
      }
    },

    // Gets the color associated with the variant
    color () {
      switch (this.effectiveVariant) {
        case 'alert': return 'yellow'
        case 'danger': return 'red'
        case 'info': return 'blue'
        case 'success': return 'green'
        default: return 'blue'
      }
    }
  }
}
</script>
