<script setup lang="ts"></script>

<template lang="pug">
section.container
    a(href="/post") Страница отправки данных
    a(href="/view") Страница просмотра данных
</template>

<style scoped lang="sass">
.container
    display: flex
    flex-direction: column
    gap: 16px
a
    padding: 8px
    outline: 1px solid blue
</style>
