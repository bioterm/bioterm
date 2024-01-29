<template>
  <q-page class="flex">
    <div class="q-pa-md">
      <div class="q-mb-md">
        <div class="text-h6">Imprint</div>
        <ckeditor
          :editor="editor"
          v-model="legalContent.legal"
          :config="editorConfig"
        ></ckeditor>
      </div>

      <q-btn label="Save" color="primary" @click="saveContent" />
    </div>
  </q-page>
</template>

<script>
import { ref, onMounted } from 'vue';
import CKEditor from '@ckeditor/ckeditor5-vue';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import axios from 'axios';
import { useQuasar } from 'quasar';
import auth from 'src/services/AuthService';
import { showError, showSuccess } from 'src/services/NotificationService';

export default {
  name: 'ContentEditor',
  components: {
    ckeditor: CKEditor.component,
  },
  setup() {
    const $q = useQuasar();
    const editor = ClassicEditor;
    const legalContent = ref({
      legal: '',
      id: null,
    });
    const editorConfig = ref({
      // Add CKEditor configuration here
    });
    const loading = ref(false);

    const fetchLegalContent = async () => {
      loading.value = true;
      $q.loading.show();
      try {
        const accessToken = await auth.getAccessToken();
        const res = await axios.get(`${process.env.API_URL}/api/v0/gdpr/`, {
          headers: { Authorization: `Bearer ${accessToken}` },
        });

        legalContent.value = res.data;
        console.log(res.data);
      } catch (err) {
        console.error(err);
        showError('Error retrieving data from API.');
      } finally {
        loading.value = false;
        $q.loading.hide();
      }
    };

    const saveContent = async () => {
      loading.value = true;
      $q.loading.show();
      try {
        const accessToken = await auth.getAccessToken();
        const res = await axios.put(
          `${process.env.API_URL}/api/v0/gdpr/`,
          { legal: legalContent.value.legal },
          {
            headers: { Authorization: `Bearer ${accessToken}` },
          },
        );
        fetchLegalContent();
        console.log('Successfully updated entry:', res.data);
      } catch (err) {
        console.error(err);
        showError('Error adding entry.');
      } finally {
        loading.value = false;
        $q.loading.hide();
        showSuccess('Successfully updated entry.');
      }
    };

    onMounted(fetchLegalContent);

    return {
      editor,
      legalContent,
      editorConfig,
      loading,
      fetchLegalContent,
      saveContent,
    };
  },
};
</script>

<style scoped>
/* Add any additional styles if necessary */
</style>
