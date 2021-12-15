<template>
  <page-layout>
    <template v-slot:title>Page Not Found</template>
    Oopsy daisy! Your page doesn't seem to be here.
  </page-layout>
</template>

<script>
import PageLayout from '../layouts/PageLayout'

export default {
  name: 'PageNotFound',

  components: {
    PageLayout
  }
}
</script>

<style scoped>

</style>
