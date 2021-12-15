<template>
  <page-layout>
    <two-column-content>
      <template #left>
        <form-content title="Request Password Reset" action="/api/auth/password/reset/" submit="Request Reset"
                      @success="onSuccess">
          <easy-input-block id="email" name="email" type="text" autocomplete="email" required=""
                            label="Email Address" />
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
 * Request a Password Reset page. The user comes here when they first select that they have forgotten their password.
 */
export default {
  name: 'PasswordReset',

  components: {
    TwoColumnContent,
    EasyInputBlock,
    PageLayout,
    FormContent,
    ImageContent
  },

  methods: {
    // Password reset request sent successfully
    onSuccess () {
      FlashMessage.setFlashMessage('Password reset request sent. If there is a user with that email address in our ' +
        'system, you should soon receive an email with instructions on how to proceed.')
      this.$router.push('/login')
    }
  }
}
</script>
