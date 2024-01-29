<template>
  <!-- <q-page
    class="flex q-pa-md fit row justify-start items-start content-start q-gutter-xs"
  > -->
  <q-page
    padding
    class="full-width column no-wrap justify-start items-stretch content-start q-gutter-y-md"
  >
    <div class="row" padding>
      <h1>Administration</h1>
    </div>
    <div class="q-pa-md">
      <div class="q-gutter-y-md">
        <q-tabs v-model="tab" class="text-teal" indicator-color="accent">
          <q-tab
            name="devcon"
            icon="fa-solid fa-database"
            label="Device & Controller Management"
          />
          <q-tab name="imprint" icon="fa-solid fa-section" label="Imprint" />
        </q-tabs>
      </div>
    </div>
    <q-separator color="purple" inset />
    <q-tab-panels
      v-model="tab"
      animated
      vertical
      transition-prev="jump-left"
      transition-next="jump-right"
    >
      <q-tab-panel name="devcon">
        <div class="q-pa-md flex">
          <div v-for="(table, index) in tables" :key="index" class="full-width">
            <div class="full-width">
              <CRUDTableWrapper
                :title="table.title"
                :url="table.url"
                :metadataUrl="table.metadataUrl"
              />
            </div>

            <div
              v-if="index < tables.length - 1"
              class="full-width q-mt-md q-mb-md"
            >
              <q-separator color="accent" />
            </div>
          </div>
        </div>
      </q-tab-panel>
      <q-tab-panel name="imprint">
        <div><RTEComponent></RTEComponent></div>
      </q-tab-panel>
    </q-tab-panels>
  </q-page>
</template>

<script lang="ts">
import CRUDTableWrapper from 'src/components/CRUDTableWrapper.vue';
import RTEComponent from 'src/components/RTEComponent.vue';
import { ref } from 'vue';

export default {
  name: 'AdminDashboard',
  components: { CRUDTableWrapper, RTEComponent },
  setup() {
    return {
      tables: [
        {
          title: 'API Keys',
          url: `${process.env.API_URL}/api/v0/apikeys/`,
          metadataUrl: `${process.env.API_URL}/api/v0/apikeys/metadata`,
        },
        {
          title: 'Controllers',
          url: `${process.env.API_URL}/api/v0/controller/`,
          metadataUrl: `${process.env.API_URL}/api/v0/controller/metadata`,
        },
        {
          title: 'Devices',
          url: `${process.env.API_URL}/api/v0/devices/`,
          metadataUrl: `${process.env.API_URL}/api/v0/devices/metadata`,
        },
        {
          title: 'Dashboards',
          url: `${process.env.API_URL}/api/v0/grafana/dashboards/`,
          metadataUrl: `${process.env.API_URL}/api/v0/grafana/dashboards/metadata`,
        },
        {
          title: 'Panels',
          url: `${process.env.API_URL}/api/v0/grafana/panels/`,
          metadataUrl: `${process.env.API_URL}/api/v0/grafana/panels/metadata`,
        },
      ],
      tab: ref('devcon'),
    };
  },

  beforeMount() {
    console.log('mounted');
  },
};
</script>

<style scoped>
.full-width {
  width: 100%;
}
</style>
