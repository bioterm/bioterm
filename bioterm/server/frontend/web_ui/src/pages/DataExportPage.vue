<template>
  <q-page
    class="flex q-pa-md fit row justify-start items-start content-start q-gutter-xs"
  >
    <q-card class="full-width q-pa-md fit flat bordered">
      <q-card-section>
        <div class="q-pa-md" style="max-width: 300px">
          <q-input filled v-model="start_date" label="Start Date">
            <template v-slot:prepend>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-date v-model="start_date" mask="YYYY-MM-DD HH:mm">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>

            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-time
                    v-model="start_date"
                    mask="YYYY-MM-DD HH:mm"
                    format24h
                    :now-btn="true"
                  >
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>
        <div class="q-pa-md" style="max-width: 300px">
          <q-input filled v-model="end_date" label="End Date">
            <template v-slot:prepend>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-date v-model="end_date" mask="YYYY-MM-DD HH:mm">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>

            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-time
                    v-model="end_date"
                    mask="YYYY-MM-DD HH:mm"
                    format24h
                    :now-btn="true"
                  >
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>
      </q-card-section>
      <!-- Devices Table -->
      <q-table
        :rows="devices"
        row-key="uuid"
        :columns="columns"
        :hide-pagination="true"
        :pagination="pagination"
      >
        <template v-slot:body-cell-select="props">
          <q-td :props="props">
            <q-checkbox v-model="selectedDevices[props.row.uuid]" />
          </q-td>
        </template>
      </q-table>

      <q-card-actions>
        <q-btn @click="downloadData" color="primary" label="Download Data" />
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<script lang="ts">
import { useLocalStore } from "src/stores/localStore";
import { ref, Ref, reactive } from "vue";
import { Device } from "src/types/types";
import { useQuasar, date } from "quasar";
import apiservice from "src/services/ApiService";
import { storeToRefs } from "pinia";

type SelectedDevices = {
  [key: string]: boolean;
};

interface TableColumn {
  name: string;
  label: string;
  field: string | ((row: Device) => boolean | string);
  align: "center" | "left" | "right";
  sortable?: boolean;
}

export default {
  name: "DataExportPage",
  components: {},
  setup() {
    const $q = useQuasar();
    const localStore = useLocalStore();

    const { devices } = storeToRefs(localStore);
    const selectedDevices: SelectedDevices = reactive({});

    devices.value.forEach((device) => {
      selectedDevices[device.uuid] = true; // default to checked
    });

    const pagination = {
      sortBy: "name",
      descending: false,
      page: 1,
      rowsPerPage: 0,
    };

    const columns: TableColumn[] = [
      {
        name: "select",
        label: "Select",
        field: (row: Device) => selectedDevices[row.uuid],
        align: "center",
        sortable: false,
      },
      {
        name: "name",
        label: "Device Name",
        field: "display_name",
        align: "left",
      },
      {
        name: "uuid",
        label: "Device UUID",
        field: "uuid",
        align: "left",
      },
    ];

    const currentDate = new Date();
    const currentDateUTC = date.addToDate(currentDate, {
      minutes: currentDate.getTimezoneOffset(),
    });
    const twoWeeksEarlierUTC = date.subtractFromDate(currentDateUTC, {
      days: 14,
    });

    const start_date: Ref<string> = ref(
      date.formatDate(twoWeeksEarlierUTC, "YYYY-MM-DD HH:mm"),
    );
    const end_date: Ref<string> = ref(
      date.formatDate(currentDateUTC, "YYYY-MM-DD HH:mm"),
    );

    const downloadData = async () => {
      $q.loading.show();
      let uuids = Object.entries(selectedDevices)
        .filter(([, isSelected]) => isSelected)
        .map(([uuid]) => uuid)
        .join(",");

      try {
        if (localStore.selectedController) {
          const response = await apiservice.getDataExport(
            localStore.selectedController.uuid as string,
            start_date.value as string,
            end_date.value as string,
            uuids as string,
          );
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", "bioterm_data.zip");
          document.body.appendChild(link);
          link.click();
          link.remove();
          window.URL.revokeObjectURL(url);
        }
      } finally {
        $q.loading.hide();
      }
    };

    return {
      devices,
      start_date,
      end_date,
      selectedDevices,
      downloadData,
      columns,
      pagination,
    };
  },
  data() {
    return {
      response: null,
    };
  },
  methods: {
    logout() {
      console.log("logged out");
    },
  },
};
</script>

<style scoped></style>
