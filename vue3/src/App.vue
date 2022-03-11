<template>
  <!--
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
  -->
  <div><RouterView /></div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>