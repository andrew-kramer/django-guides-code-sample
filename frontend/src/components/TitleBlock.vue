<template>
  <div>
    <div class="text-primary-700 flex items-center justify-left cursor-default" v-if="showLogo === true">
        <logo class="h-12 w-12" alt="Django Guides Code Sample" />
        <span class="hidden lg:inline ml-3 text-4xl font-bold font-brand">Django Guides Code Sample</span>
    </div>
    <h2 class="mt-6 text-4xl font-extrabold text-secondary-800 font-title ml-3">
      <slot>{{ title }}</slot>
    </h2>
  </div>
</template>

<script>
import Logo from '@/components/Logo'

/**
 * Block for displaying a title (with or without logo)
 *
 * @property  showLogo  Boolean  Show the logo?
 * @property  title     String   Title to display (can be overridden by the default slot)
 *
 * @template  default  Title to display (overrides the title property)
 */
export default {
  name: 'TitleBlock',

  components: {
    Logo
  },

  props: {
    // Show the logo?
    showLogo: Boolean,

    // Title to display (can be overridden by the default slot)
    title: String
  }
}
</script>
