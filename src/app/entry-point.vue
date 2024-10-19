<script setup lang="ts">
import { RouterView } from "vue-router";
</script>
<template lang="html">
  <main class="main">
    <RouterView></RouterView>
  </main>
</template>
<style scoped lang="css">
.main {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
