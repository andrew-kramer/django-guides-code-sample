<template>
  <page-layout>
    <two-column-content>
      <template #left>
        <form-content title="Confirm Password Reset" action="/api/auth/password/reset/confirm/" method="POST"
                      submit="Reset Password" :error-message="generalErrorMessage" @success="onSuccess">
                    <input type="hidden" name="uid" :value="uidb64" />

                    <input type="hidden" name="token" :value="token" />

                    <easy-input-block id="new_password1" name="new_password1" type="password"
                                      autocomplete="new-password" required="" label="New Password" />

                    <easy-input-block id="new_password2" name="new_password2" type="password"
                                      autocomplete="new-password" required="" label="Confirm New Password" />
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
import PageLayout from '@/layouts/PageLayout'
import FlashMessage from '@/utils/FlashMessage'
import TwoColumnContent from '@/layouts/TwoColumnContent'
import FormContent from '@/layouts/FormContent'
import ImageContent from '@/layouts/ImageContent'

/**
 * Password Reset: Change Your Password page. After the user has requested a password reset, they get an email. The link
 * in that email refers them here with two special tokens, as properties (taken from the URL by the router).
 *
 * @property  uidb64  String  User ID in base64 encoding
 * @property  token   String  Password reset token
 */
export default {
  name: 'ResetConfirm',

  components: {
    FormContent,
    ImageContent,
    TwoColumnContent,
    EasyInputBlock,
    PageLayout
  },

  props: {
    // User ID in Base64 encoding
    uidb64: String,

    // Password reset token
    token: String
  },

  data: function () {
    return {
      generalErrorMessage: 'Unable to update your password. Your one-time token may have expired. Please check your ' +
        'inbox for a more recent email or request another reset.'
    }
  },

  methods: {
    // We logged in. Redirect and reload the new page.
    onSuccess () {
      FlashMessage.setFlashMessage('Your password has been reset.')
      this.$router.push('/login')
    },

    // The login form or the API had some sort of problem.
    onError () {
      this.errorMessage = 'A problem occurred on our end. Sorry!'
    },

    // The user supplied bad credentials.
    badRequestProcessor (errors) {
      const response = {}
      if (errors.errors.token || errors.errors.uidb64) {
        response.messages = [this.generalErrorMessage]
      } else if (errors.messages) {
        response.messages = errors.messages
      }
      if (errors.errors.password1) {
        response.errors.password1 = errors.errors.password1
      }
      if (errors.errors.password2) {
        response.errors.password2 = errors.errors.password2
      }
    }
  }
}
</script>
