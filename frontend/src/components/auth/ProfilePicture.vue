<template>
  <img v-if="!!user && !!user.profile_picture" v-bind:class="['rounded-full']" :src="user.profile_picture"
       :alt="user.first_name + ' ' + user.last_name" />
  <div v-else-if="!!user"
       class="rounded-full h-8 w-8 flex items-center justify-center bg-secondary-50 text-primary-800 font-bold">
    {{ initials }}
  </div>
  <user-circle-icon v-else />
</template>

<script>
import { UserCircleIcon } from '@heroicons/vue/solid'

// Get the first letter of a string
function getFirstLetter (s) {
  return (s.substr ? s.substr(0, 1) : '')
}

/**
 * Displays a profile picture for a provided user object
 *
 * @property user  Number  User object
 */
export default {
  name: 'ProfilePicture',

  components: {
    UserCircleIcon
  },

  props: {
    // User object
    user: {
      first_name: String,
      last_name: String,
      profile_picture: [String, null]
    }
  },

  computed: {
    // Get the user's initials
    initials () {
      let initials = ''
      if (this.user.first_name || this.user.last_name) {
        initials += getFirstLetter(this.user.first_name)
        initials += getFirstLetter(this.user.last_name)
      } else {
        initials += getFirstLetter(this.user.username)
      }
      return initials.toUpperCase()
    }
  }
}
</script>
