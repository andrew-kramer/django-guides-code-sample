<!--suppress MagicNumberJS -->
<template>
  <div class="flex">
    <div :class="['flex-1', 'flex', 'flex-col', 'justify-center', 'py-12', 'px-4', 'sm:px-6', 'lg:px-20', 'xl:px-24',
                  flexLeft ? 'hidden' : 'lg:flex-none', flexLeft ? 'lg:block' : '']">
      <slot name="left" />
    </div>
    <div :class="[flexLeft ? 'lg:flex-none' : 'hidden', flexLeft ? '' : 'lg:block',
                  'relative', 'w-0', 'flex-1']">
      <slot name="right" />
    </div>
  </div>
</template>

<script>
/**
 * Page layout with two columns
 *
 * @property  flexLeft  Boolean  If the screen is not large-sized, we have to hide one side or the other; should it be
 *                               the left side that we hide?
 *
 * @template  left   Column on the left
 * @template  right  Column on the right
 */
export default {
  name: 'TwoColumnContent',

  props: {
    // If the screen is not large-sized, we have to hide one side or the other; should it be the left side that we hide?
    flexLeft: Boolean
  }
}
</script>
