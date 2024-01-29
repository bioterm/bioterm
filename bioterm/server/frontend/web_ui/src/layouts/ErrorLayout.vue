<template>
  <q-layout view="hHh lpR fFf">
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { useQuasar } from 'quasar';

export default {
  name: 'ErrorLayout',
  setup() {
    const $q = useQuasar();
    // $q.addressbarColor.set();
    ($q.addressbarColor.set as (color?: string) => void)();
  },
};
</script>

<style>
::-webkit-scrollbar {
  display: none;
}
</style>
