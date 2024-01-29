<template>
  <q-page class="bg-primary row justify-center items-center">
    <div class="q-pa-md text-white" style="max-width: 800px">
      <div v-html="legalContent.legal" class="legal-content"></div>
    </div>
  </q-page>
</template>

<script lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useQuasar } from 'quasar';

export default {
  name: 'ImprintPage',
  setup() {
    const $q = useQuasar();
    const legalContent = ref({
      legal: '',
      id: null,
    });
    const loading = ref(false);

    const fetchLegalContent = async () => {
      loading.value = true;
      $q.loading.show();
      try {
        const res = await axios.get(`${process.env.API_URL}/api/v0/gdpr/`);

        legalContent.value = res.data;
      } catch (err) {
        console.error(err);
      } finally {
        loading.value = false;
        $q.loading.hide();
      }
    };

    onMounted(fetchLegalContent);

    return {
      legalContent,
      loading,
      fetchLegalContent,
    };
  },
};
</script>

<style scoped></style>
