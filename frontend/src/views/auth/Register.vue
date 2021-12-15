<!--suppress MagicNumberJS -->
<template>
  <page-layout>
    <two-column-content>
      <template #left>
        <form-content title="Sign Up" action="/api/auth/registration/" method="POST" submit="Sign Up"
                      @success="onSuccess">
          <easy-input-block id="username" name="username" type="text" autocomplete="username" required=""
                            label="Username">
            <template #info>Your username will be publicly viewable.</template>
          </easy-input-block>

          <easy-input-block id="email" name="email" type="email" autocomplete="email" required=""
                            label="Email Address">
            <template #info>
              We will never share your information with third parties (more details in our
              <router-link to="/privacy" class="text-primary-400 hover:text-primary-500">Privacy Policy</router-link>).
            </template>
          </easy-input-block>

          <easy-input-block id="password1" name="password1" type="password" autocomplete="new-password"
                            required="" label="Password" />

          <easy-input-block id="password2" name="password2" type="password" autocomplete="new-password"
                            required="" label="Confirm Password" />

          <div class="text-sm text-center text-secondary-600">
            Already have an account?
            <router-link to="/login" class="font-medium text-primary-600 hover:text-primary-500">
              Sign In
            </router-link>
          </div>
        </form-content>
      </template>
      <template #right>
        <image-content>
          <template #image>
            <img src="../../assets/img/milky-way-placeholder.jpg"
                 alt="Photo by Rodrigo Soares - unsplash.com/@rodri01">
          </template>
          <template #caption>
            Photo by
            <a class="text-primary-300 hover:text-primary-200 underline" target="_blank"
               href="https://unsplash.com/@rodi01">Rodrigo Soares</a>
          </template>
        </image-content>
      </template>
    </two-column-content>
  </page-layout>
</template>

<script>
import EasyInputBlock from '@/components/forms/EasyInputBlock'
import FormContent from '@/layouts/FormContent'
import ImageContent from '@/layouts/ImageContent'
import PageLayout from '@/layouts/PageLayout'
import TwoColumnContent from '@/layouts/TwoColumnContent'

/**
 * Register page
 */
export default {
  name: 'Register',

  components: {
    EasyInputBlock,
    FormContent,
    ImageContent,
    PageLayout,
    TwoColumnContent
  },

  inject: ['auth'],

  methods: {
    // We logged in. Redirect and reload the new page.
    onSuccess (user) {
      if (this.auth && this.auth.login) {
        this.auth.login(user)
        this.$router.push('/')
      }
    }
  }
}
</script>
