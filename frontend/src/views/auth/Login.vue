<!--suppress MagicNumberJS -->
<template>
  <page-layout>
    <two-column-content>
      <template #left>
        <form-content title="Sign in to your account" action="/api/auth/login/" method="POST" submit="Sign In"
                      @success="onSuccess">
          <easy-input-block id="username" name="username" type="text" autocomplete="username" required=""
                            label="Username" />

          <easy-input-block id="password" name="password" type="password" autocomplete="current-password"
                            required="" label="Password" />

          <div class="text-center text-sm">
            <router-link to="/password-reset" class="font-medium text-primary-600 hover:text-primary-500">
              Forgot your password?
            </router-link>
          </div>
          <div class="text-sm text-center text-secondary-600">
            Don't have an account?
            <router-link to="/register" class="font-medium text-primary-600 hover:text-primary-500">
              Sign Up
            </router-link>
          </div>
        </form-content>
        <!--
        <div class="mt-3 flex flex-col items-center justify-center space-y-2">
          <div class="flex-grow block font-bold text-secondary-500">OR</div>
          <div class="flex-shrink">
            <a href="/social-auth/steam/" class="opacity-75 hover:opacity-100">
              <img src="../../assets/img/steam_sits_wide.png" alt="Sign in through Steam" />
            </a>
          </div>
        </div>
        -->
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
 * Login page
 */
export default {
  name: 'Login',

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
      this.auth.login(user)
      this.$router.push('/')
    }
  }
}
</script>
