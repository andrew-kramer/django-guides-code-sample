<template>
  <div class="relative bg-primary-400 mb-2" v-if="visible">
    <div class="max-w-7xl mx-auto py-3 px-3 sm:px-6 lg:px-8">
      <div class="pr-16 sm:text-center sm:px-16">
        <p class="font-medium text-secondary-50">
          <span v-if="$slots.smallText">
            <span class="md:hidden">
              <slot name="smallText" />
            </span>
            <span class="hidden md:inline">
              <slot />
            </span>
          </span>
          <span v-else>
            <slot />
          </span>
          <span class="block sm:ml-2 sm:inline-block" v-if="$slots.link">
            <span class="text-secondary-50 font-bold underline hover:text-secondary-200">
              <slot name="link" />
            </span>
          </span>
        </p>
      </div>
      <div class="absolute inset-y-0 right-0 pt-1 pr-1 flex items-start sm:pt-1 sm:pr-2 sm:items-start">
        <button type="button" @click="visible=false"
                :class="'flex p-2 rounded-md hover:bg-primary-500 focus:outline-none focus:ring-2 ' +
                    'focus:ring-secondary-50'">
          <span class="sr-only">Dismiss</span>
          <XIcon class="h-6 w-6 text-secondary-50" aria-hidden="true" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { XIcon } from '@heroicons/vue/outline'

/**
 * Displays a Banner with text (especially at the top of the <main> element)
 *
 * @template  smallText  If provided, this is what the Banner displays INSTEAD of the main text on a small display
 * @template  default    The contents of the Banner
 * @template  link       A link to be shown to the right of the main text (underneath on small displays)
 */
export default {
  name: 'Banner',

  components: {
    XIcon
  },

  data: function () {
    return {
      // Is the Banner visible?
      visible: true
    }
  }
}
</script>
