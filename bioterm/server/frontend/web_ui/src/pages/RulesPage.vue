<template>
  <q-page class="q-pa-md">
    <div class="text-left q-pa-md">
      <q-btn-group flat class="q-gutter-xs">
        <q-btn label="ADD RULE" color="primary" @click="createRule" />
        <q-btn label="SYNC RULES" color="info" @click="syncRules()" />
      </q-btn-group>
    </div>
    <q-table :rows="rules" :columns="columns" row-key="name">
      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td key="name" :props="props">
            <q-icon :name="statusIcon(props.row.sync)" />
          </q-td>
          <q-td key="name" :props="props">
            {{ props.row.display_name }}
          </q-td>
          <q-td key="action" :props="props">
            <q-btn-group flat>
              <q-btn
                color="warning"
                round
                flat
                dense
                :icon="'adjust'"
                @click="goToRuleDetails(props.row.uuid)"
                ><q-tooltip
                  class="bg-warning text-white shadow-4"
                  :offset="[10, 10]"
                >
                  Update entry
                </q-tooltip>
              </q-btn>
              <q-btn
                color="negative"
                round
                flat
                dense
                :icon="'delete'"
                @click="confirmDelete(props.row.uuid)"
                ><q-tooltip
                  class="bg-negative text-white shadow-4"
                  :offset="[10, 10]"
                >
                  Delete entry
                </q-tooltip>
              </q-btn>
            </q-btn-group>
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </q-page>
  <q-dialog v-model="showDialog">
    <q-card>
      <q-card-section>
        Are you sure you want to delete this item?
      </q-card-section>
      <q-card-actions align="right">
        <q-btn flat label="Cancel" @click="showDialog = false" />
        <q-btn flat label="Delete" color="negative" @click="performDelete" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script lang="ts">
import { useLocalStore } from 'src/stores/localStore';
import { ref, onMounted } from 'vue';
import { RuleModel } from 'src/types/rules';
import { useRouter } from 'vue-router';
import { useQuasar } from 'quasar';
import apiservice from 'src/services/ApiService';
import { storeToRefs } from 'pinia';

export default {
  name: 'RulesPage',
  setup() {
    const localStore = useLocalStore();
    const $q = useQuasar();
    const showDialog = ref(false);
    const itemToDelete = ref<string | null>(null);

    const { rules } = storeToRefs(localStore);

    const reloadRules = () => {
      componentKey.value += 1;
    };
    const router = useRouter();

    const createRule = () => {
      router.push('rule/create');
    };

    const goToRuleDetails = (uuid: string) => {
      router.push({ name: 'rule', params: { uuid: uuid } });
    };
    const componentKey = ref(0);
    const columns = [
      {
        name: 'sync',
        required: true,
        label: 'Sync',
        align: 'left',
        field: (row: RuleModel) => row.sync,
        sortable: true,
      },
      {
        name: 'name',
        required: true,
        label: 'Rule Name',
        align: 'left',
        field: 'name',
        sortable: true,
      },
      { name: 'action', label: 'Actions', align: 'left' },
    ];

    const statusIcon = (sync: boolean) => {
      switch (sync) {
        case true:
          return 'done';
        case false:
          return 'disabled_by_default';
        default:
          return 'help_outline';
      }
    };

    const confirmDelete = (uuid: string) => {
      itemToDelete.value = uuid;
      showDialog.value = true;
    };

    const performDelete = async () => {
      $q.loading.show();
      if (itemToDelete.value !== null) {
        if (localStore.selectedController) {
          await apiservice
            .deleteRule(localStore.selectedController.uuid, itemToDelete.value)
            .then(() => {
              itemToDelete.value = null;
              localStore.updateRules();
              $q.loading.hide();
              showDialog.value = false;
            });
        }
      }
    };

    const syncRules = async () => {
      if (localStore.selectedController) {
        $q.loading.show();
        await apiservice
          .syncRules(localStore.selectedController?.uuid)
          .finally(() => {
            $q.loading.hide();
          });
      }
    };

    onMounted(async () => {
      await localStore.updateRules();
    });

    return {
      rules,
      reloadRules,
      componentKey,
      columns,
      goToRuleDetails,
      showDialog,
      confirmDelete,
      performDelete,
      statusIcon,
      syncRules,
      createRule,
    };
  },
  data() {
    return {
      response: null,
    };
  },
};
</script>

<style scoped></style>
