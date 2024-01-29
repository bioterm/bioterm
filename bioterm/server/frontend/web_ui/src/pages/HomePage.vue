<template>
  <q-page
    class="flex flex-center q-pa-md fit column items-center justify-center"
    :style="{ backgroundColor: localStore.selectedController ? '' : '#08a29e' }"
  >
    <div v-if="localStore.selectedController" class="full-height full-width">
      <iframe
        style="width: 100%; height: calc(100vh - 142px); border: none"
        :src="dashboardLink"
      />
    </div>
    <div v-else class="text-white text-center q-pa-md flex flex-center">
      <div
        v-if="localStore.controllers.length > 0"
        class="err404__hero flex flex-center no-wrap q-gutter-sm text-brand-primary"
      >
        SELECT SETUP
      </div>
      <div
        v-else
        class="err404__hero flex flex-center no-wrap q-gutter-sm text-brand-primary"
      >
        NO ACCESS TO SETUPS, CONTACT ADMINISTRATOR
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
import { useLocalStore } from 'src/stores/localStore';
import { computed } from 'vue';

export default {
  name: 'HomePage',
  setup() {
    const localStore = useLocalStore();
    const controllers = localStore.controllers;
    const selectedController = localStore.selectedController;

    const params = computed(() => ({
      theme: localStore.darkMode === true ? 'dark' : 'light',
      refresh: '1s',
      kiosk: 'true',
      from: 'now-5m',
    }));

    // Convert the params object to a query string
    const queryString = computed(() =>
      new URLSearchParams(params.value).toString(),
    );

    const dashboardLink = computed(
      () =>
        `https://${process.env.GRAFANA_DOMAIN}${localStore.dashboard?.link}?${queryString.value}`,
    );
    console.log(dashboardLink);
    return {
      controllers,
      selectedController,
      dashboardLink,
      localStore,
    };
  },
};
</script>

<style scoped>
.full-height {
  height: 100%;
}
.full-width {
  width: 100%;
}
</style>
