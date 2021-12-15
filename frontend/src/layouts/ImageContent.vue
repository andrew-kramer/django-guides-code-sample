<template>
  <div :class="'absolute inset-0 h-auto w-full ' + classId">
    <slot name="image" />
    <div v-if="$slots.caption" class="absolute bottom-0 w-full z-10 text-center">
      <span class="text-sm w-auto text-secondary-200 bg-secondary-800 w-auto pr-4 pl-4 opacity-75">
        <slot name="caption" />
      </span>
    </div>
  </div>
</template>

<script>

/**
 * Content for an image with optional caption
 *
 * @template  image    The image to display. It does NOT need a class attribute, as this will be overridden anyway.
 * @template  caption  Text (can be styled) to display as the caption of the image. Mainly for attribution to the
 *                     creator.
 */
export default {
  name: 'ImageContent',

  inheritAttrs: false,

  data () {
    return {
      // Random id to avoid collisions in case we have more than one of these (although theoretically collisions won't
      // mess us up
      classId: 'image-content-container-' + Math.floor(Math.random() * Number.MAX_SAFE_INTEGER)
    }
  },

  methods: {
    setImageClasses () {
      const classes = 'absolute inset-0 h-full w-full object-cover rounded-3xl border-primary-500 border-2 ' +
        'border-solid bg-secondary-200' + (this.$attrs.class ? this.$attrs.class : '')

      // This kludge replaces the classes on all img elements within the image slot
      const childImages = document.querySelectorAll('.' + this.classId + ' img')
      for (const i in childImages) {
        if (Object.prototype.hasOwnProperty.call(childImages, i)) {
          childImages[i].setAttribute('class', classes)
        }
      }
    }
  },

  mounted () {
    this.setImageClasses()
  },

  updated () {
    this.setImageClasses()
  }
}
</script>
