<template>
  <div class="table-container">
    <q-table
      ref="tableRef"
      v-if="data"
      :rows="data"
      :columns="tableColumns"
      row-key="id"
      table-class="my-table"
    >
      <template v-slot:body-cell-actions="props">
        <q-td align="center">
          <q-btn-group flat>
            <q-btn
              color="warning"
              round
              flat
              dense
              :icon="'adjust'"
              @click="modifyItem(props.row.id, props.row)"
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
              @click="confirmDelete(props.row.id)"
              ><q-tooltip
                class="bg-negative text-white shadow-4"
                :offset="[10, 10]"
              >
                Delete entry
              </q-tooltip>
            </q-btn>
          </q-btn-group>
        </q-td>
      </template>
    </q-table>
    <q-space />
    <div class="row q-gutter-sm q-pa-md fit">
      <div>
        <q-btn color="positive" text-white @click="handleAddButtonClick"
          >New Entry</q-btn
        >
      </div>
      <div>
        <q-btn color="info" @click="fetchData">Refresh</q-btn>
      </div>
    </div>
  </div>
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
  <q-dialog v-model="showAddForm" :persistent="loading">
    <CustomFormComponent
      :prompt="addEntryPrompt"
      :inputs="formInputsCreate"
      :locked="loading"
      @submit="handleFormSubmit"
    ></CustomFormComponent>
  </q-dialog>
  <q-dialog v-model="showModifyForm" :persistent="loading">
    <CustomFormComponent
      :prompt="modifyEntryPrompt"
      :inputs="modifyFormInputs"
      :locked="loading"
      :defaultValues="(modifyData?.value as ItemData) /* prettier-ignore */"
      :fielderrors="fieldErrors"
      @submit="handleModifySubmit"
    ></CustomFormComponent>
  </q-dialog>
</template>

<script lang="ts">
import { ref, defineComponent, computed, watch } from 'vue';
import axios, { AxiosError } from 'axios';
import auth from 'src/services/AuthService';
import { QTable } from 'quasar';
import CustomFormComponent from './CustomFormComponent.vue';
import { InputTypes, ItemData, FieldErrors } from './CustomFormComponent.vue';
import { useQuasar } from 'quasar';
import { showError, showSuccess } from 'src/services/NotificationService';

type FormElement = {
  type: InputTypes;
  label: string;
  model: string;
  autocomplete?: boolean;
  defaultValue?: unknown;
};

type TableColumn = {
  name: string;
  label: string;
  align?: 'left' | 'right' | 'center' | undefined;
  // lambda required for fields which should be displayed differently from raw object data
  field: string | ((row: ItemData) => string);
  sortable?: boolean;
};

export default defineComponent({
  components: {
    CustomFormComponent,
  },
  props: {
    apiUrl: {
      type: String,
      required: true,
    },
    columns: {
      type: Array<TableColumn>,
      required: true,
    },
    formElementsCreate: {
      type: Array<FormElement>,
      required: true,
    },
    formElementsUpdate: {
      type: Array<FormElement>,
      required: true,
    },
  },

  setup(props) {
    const $q = useQuasar();
    const addEntryPrompt = 'Enter required data for new entry';
    const modifyEntryPrompt = 'Enter required data to modify entry';

    const showDialog = ref(false);
    const showAddForm = ref(false);
    const showModifyForm = ref(false);

    const data = ref<object[] | null>(null);
    const loading = ref<boolean>(false);
    const newItemName = ref<string>('');
    const tableRef = ref<typeof QTable | null>(null);

    //const modifyData = ref<object | null>(null);
    //const modifyData = ref<{ [key: string]: any }>();
    const modifyData = ref<ItemData | null>(null);
    const selectedRowId = ref<number | null>(null);
    const itemToDelete = ref<number | string | null>(null);
    const fieldErrors = ref<FieldErrors>({});

    // add an extra column for the the update and delete buttons
    const actionsColumn: TableColumn = {
      name: 'actions',
      label: 'Actions',
      align: 'center',
      field: () => 'Actions', // required by quasar table
    };
    const tableColumns = ref([...props.columns, actionsColumn]);

    const formInputsCreate = ref([...props.formElementsCreate]);
    const formInputsUpdate = ref([...props.formElementsUpdate]);

    // Pre-populate data
    const prepopulatedData = ref<object | null>(null);

    const fetchData = async () => {
      loading.value = true;
      $q.loading.show();
      try {
        const res = await auth.getAccessToken().then((access_token) =>
          axios.get(props.apiUrl, {
            headers: { Authorization: `Bearer ${access_token}` },
          }),
        );

        data.value = res.data;
        console.log(data.value);
      } catch (err) {
        console.error(err);
        showError('Error retrieving data from API.');
      } finally {
        loading.value = false;
        $q.loading.hide();
      }
    };

    // Reset the defaultValues for all formInputs
    // const resetFormInputs = () => {
    //   formInputsCreate.value.forEach((input) => {
    //     input.defaultValue = '';
    //   });
    // };

    // Trigger this function when Add button is clicked
    const handleAddButtonClick = () => {
      // resetFormInputs();
      showAddForm.value = true;
    };

    const handleFormSubmit = async (formData: ItemData) => {
      loading.value = true;
      $q.loading.show();
      try {
        const res = await auth.getAccessToken().then((access_token) =>
          axios.post(`${props.apiUrl}`, formData, {
            headers: { Authorization: `Bearer ${access_token}` },
          }),
        );
        // await delay(5000);
        fetchData();
        console.log('Successfully added entry:', res.data);
      } catch (err) {
        console.error(err);
        showError('Error adding entry.');
      } finally {
        loading.value = false;
        $q.loading.hide();
        showSuccess('Successfully added entry.');
      }
      loading.value = false;
      $q.loading.hide();

      showAddForm.value = false;
    };

    // Handle modification of items

    const modifyItem = (id: number, item: ItemData) => {
      selectedRowId.value = id;
      modifyData.value = item;
      formInputsUpdate.value.forEach((input) => {
        if (item.hasOwnProperty(input.model)) {
          input.defaultValue = item[input.model];
        }
      });
      showModifyForm.value = true;
    };

    const modifyFormInputs = computed(() => {
      if (modifyData.value) {
        const modifiedInputs = [...formInputsUpdate.value];
        modifiedInputs.forEach((input) => {
          if (modifyData.value && input.model in modifyData.value) {
            input.defaultValue = modifyData.value[input.model];
          }
        });
        return modifiedInputs;
      }
      return formInputsUpdate.value;
    });

    const handleModifySubmit = async (formData: ItemData) => {
      if (selectedRowId.value !== null) {
        console.log('Modifying row with ID:', selectedRowId.value);
        console.log('Modified entry:', formData);
        loading.value = true;
        $q.loading.show();
        try {
          const res = await auth.getAccessToken().then((access_token) =>
            axios
              .put(`${props.apiUrl}${selectedRowId.value}`, formData, {
                headers: { Authorization: `Bearer ${access_token}` },
              })
              .catch((err: Error | AxiosError) => {
                if (axios.isAxiosError(err)) {
                  if (err.response?.status === 422) {
                    fieldErrors.value = err.response?.data?.detail.reduce(
                      (
                        o: FieldErrors,
                        x: { loc: Array<string>; msg: string }, //err422 of fastapi response always contains loc and msg
                      ) => {
                        return { ...o, [x.loc[1]]: x.msg };
                      },
                      {},
                    );
                    console.log(fieldErrors.value);
                    throw err.response.data?.detail
                      .map(
                        (
                          x: { loc: Array<string>; msg: string }, //err422 of fastapi response always contains loc and msg
                        ) => `${x.msg} for ${x.loc[1]}.`,
                      )
                      .join(' ');
                  }
                }
                throw err;
              }),
          );
          // await delay(5000);
          fetchData();
          console.log('Successfully modified entry:', res.data);
          showSuccess('Successfully modified entry');
          showModifyForm.value = false;
        } catch (err) {
          console.error(err);
          showError(`Error modifying entry.\n${err}`);
        } finally {
          loading.value = false;
          $q.loading.hide();
        }
        loading.value = false;
        $q.loading.hide();
      }
    };

    // Handle delete requests by asking for confirmation first

    const deleteItem = async (id: number | string) => {
      loading.value = true;
      $q.loading.show();

      try {
        await auth.getAccessToken().then((access_token) =>
          axios.delete(`${props.apiUrl}${id}`, {
            headers: { Authorization: `Bearer ${access_token}` },
          }),
        );
        await fetchData();
      } catch (err) {
        console.error(err);
        showError('Error deleting entry.');
      } finally {
        loading.value = false;
        $q.loading.hide();
        showSuccess('Successfully deleted entry.');
      }
    };

    const confirmDelete = (id: number | string) => {
      itemToDelete.value = id;
      showDialog.value = true;
    };

    const performDelete = async () => {
      if (itemToDelete.value !== null) {
        await deleteItem(itemToDelete.value);
        itemToDelete.value = null;
      }
      showDialog.value = false; // Close the confirmation dialog
    };

    // reset fieldErrors when visibility changes to false
    watch(showAddForm, (newValue) => {
      if (!newValue) {
        fieldErrors.value = {};
      }
    });

    watch(showModifyForm, (newValue) => {
      if (!newValue) {
        fieldErrors.value = {};
      }
    });

    // Fetch data on component mount
    fetchData();

    return {
      CustomFormComponent,
      data,
      loading,
      newItemName,
      tableColumns,
      tableRef,
      formInputsCreate,
      showDialog,
      fieldErrors,
      showAddForm,
      addEntryPrompt,
      modifyEntryPrompt,
      showModifyForm,
      modifyFormInputs,
      prepopulatedData,
      modifyData,
      selectedRowId,
      deleteItem,
      confirmDelete,
      performDelete,
      fetchData,
      handleFormSubmit,
      modifyItem,
      handleModifySubmit,
      handleAddButtonClick,
    };
  },
});
</script>

<style lang="scss">
// .add-item {
//   margin-top: 20px;
// }
.table-container {
  overflow-x: auto;
}
.q-table {
  /* specifying max-width so the example can
      highlight the sticky column on any browser window */
  // max-width: 600px;

  thead tr:first-child th:first-child {
    /* bg color is important for th; just specify one */
    background-color: $accent;
    color: white;
  }
  td:first-child {
    background-color: $accent;
    color: white;
  }
  th:first-child,
  td:first-child {
    position: sticky;
    left: 0;
    z-index: 1;
  }
}
</style>
