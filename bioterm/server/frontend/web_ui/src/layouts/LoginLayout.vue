<template>
  <q-layout view="hHh lpR fFf">
    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer reveal elevated class="bg-dark text-white" q-pa-md>
      <q-toolbar class="justify-center">
        <router-link to="/imprint" class="text-white"
          >Imprint & Privacy Policy
        </router-link>

        <div
          class="q-mx-md"
          style="border-left: 1px solid white; height: 20px"
        ></div>
        <!-- Vertical line separator -->
        <a
          href="https://github.com/bioterm/bioterm"
          class="text-white"
          target="_blank"
          >Powered by bioterm</a
        >
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script lang="ts">
import { useQuasar } from 'quasar';

export default {
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
