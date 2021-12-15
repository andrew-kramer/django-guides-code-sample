<template>
  <div />
</template>

<script>
/**
 * Displays an animated spinner to indicate that something is happening.
 *
 * Based on "Pure CSS Loaders" from "https://loading.io/css" under the CC0 License
 */
export default {
  name: 'AnimatedSpinner'
}
</script>

<style scoped lang="css">
div {
  display: inline-block;
}
div:after {
  content: " ";
  display: block;
  border-radius: 50%;
  width: 0;
  height: 0;
  margin: 8px;
  box-sizing: border-box;
  border-width: 32px;
  border-color: #888 transparent #888 transparent;
  animation: lds-hourglass 1.2s infinite;
}
@keyframes lds-hourglass {
  0% {
    transform: rotate(0);
    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }
  50% {
    transform: rotate(900deg);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  100% {
    transform: rotate(1800deg);
  }
}
</style>
