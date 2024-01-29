<template>
  <q-card class="full-width q-pa-md fit flat bordered">
    <q-card-section>
      <div class="text-h5 q-mt-sm q-mb-xs text-accent">
        {{ thisTitle }}
        <q-btn
          color="accent"
          round
          flat
          dense
          :icon="expanded ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
          @click="expanded = !expanded"
        />
      </div>
    </q-card-section>

    <q-slide-transition>
      <div v-show="expanded">
        <q-separator />
        <q-card-section class="text-subtitle2">
          <CRUDTable
            v-if="metaReady"
            :apiUrl="thisUrl"
            :columns="columns"
            :formElementsCreate="formElementsCreate"
            :formElementsUpdate="formElementsUpdate"
          />
        </q-card-section>
      </div>
    </q-slide-transition>
  </q-card>
</template>

<script lang="ts">
import CRUDTable from 'src/components/CRUDTable.vue';
import axios from 'axios';
import auth from 'src/services/AuthService';

import { onMounted, ref } from 'vue';

interface Props {
  title?: string;
  url?: string;
  metadataUrl?: string;
}

export default {
  name: 'CRUDTableWrapper',
  props: {
    title: String,
    url: String,
    metadataUrl: String,
  },
  components: { CRUDTable },
  setup(props: Props) {
    const thisTitle = ref(props.title);
    const formElementsCreate = ref([]);
    const formElementsUpdate = ref([]);
    const columns = ref([]);
    const thisUrl = ref(props.url ?? '');
    const thisMetadataUrl = ref(props.metadataUrl ?? '');
    const metaReady = ref(false);
    const expanded = ref(false);

    onMounted(async () => {
      try {
        const access_token = await auth.getAccessToken();
        const response = await axios.get(thisMetadataUrl.value, {
          headers: { Authorization: `Bearer ${access_token}` },
        });
        formElementsCreate.value = response.data.formElementsCreate;
        formElementsUpdate.value = response.data.formElementsUpdate;
        columns.value = response.data.columns;
        metaReady.value = true;
      } catch (error) {
        console.error('An error occurred while fetching metadata:', error);
      }
    });

    return {
      thisTitle,
      formElementsCreate,
      formElementsUpdate,
      columns,
      thisUrl,
      thisMetadataUrl,
      metaReady,
      expanded,
    };
  },
};
</script>

<style scoped></style>
