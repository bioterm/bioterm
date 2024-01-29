<template>
  <q-page class="fullscreen bg-primary text-white text-center q-pa-md flex flex-center">
    <div>
      <div class="err404__hero flex flex-center no-wrap q-gutter-sm text-brand-primary">
        <div class="text-h1">404</div>
      </div>
      <div class="err404__punch-line text-grey-8">Dude, where's my page?</div>
      <q-btn class="q-mt-xl" color="white" text-color="primary" unelevated to="/" label="Go Home" no-caps/>
    </div>
  </q-page>
  </template>
  
  <script lang="ts">
  import {defineComponent} from 'vue';
  
  export default defineComponent({
    name: 'ErrorNotFound'
  });
  </script>
  