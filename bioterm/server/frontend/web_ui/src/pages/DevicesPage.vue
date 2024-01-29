<template>
  <q-page class="q-pa-md"
    ><q-table
      :rows="devices"
      :columns="columns"
      row-key="name"
      :pagination="pagination"
    >
      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td key="name" :props="props">
            {{ props.row.display_name }}
          </q-td>
          <q-td key="uuid" :props="props">
            {{ props.row.uuid }}
          </q-td>
          <q-td key="status" :props="props">
            <q-icon :name="statusIcon(props.row.status)" />
          </q-td>
          <q-td key="action" :props="props">
            <q-btn
              label="Details"
              @click="goToDeviceDetails(props.row.uuid)"
              color="primary"
            />
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </q-page>
</template>

<script lang="ts">
import { useLocalStore } from "src/stores/localStore";
import { computed, ref, ComputedRef } from "vue";
import { Device } from "src/types/types";
import { useRouter } from "vue-router";

export default {
  name: "DevicePage",
  setup() {
    const localStore = useLocalStore();

    // define computed devices property, since vue can't seem to track changes in the store properly
    // (most likely to the fact, that we're replacing the entire array instead of just mutating it)
    const devices: ComputedRef<Device[]> = computed(() => localStore.devices);
    const reloadDevices = () => {
      componentKey.value += 1;
    };
    const router = useRouter();
    const goToDeviceDetails = (uuid: string) => {
      router.push({ name: "device", params: { uuid: uuid } });
    };
    const componentKey = ref(0);
    const columns = [
      {
        name: "name",
        required: true,
        label: "Device Name",
        align: "left",
        field: "name",
        sortable: true,
      },
      {
        name: "uuid",
        required: true,
        label: "Device UUID",
        align: "left",
        field: "uuid",
        sortable: true,
      },
      {
        name: "status",
        required: true,
        label: "Status",
        align: "left",
        field: (row: Device) => row.display_name,
        sortable: true,
      },
      { name: "action", label: "Action", align: "left" },
    ];
    const statusIcon = (status: string) => {
      switch (status) {
        case "OK":
          return "check_circle";
        case "ERROR":
          return "error";
        case "UNKNOWN":
        default:
          return "help_outline";
      }
    };

    const pagination = {
      sortBy: "name",
      descending: false,
      page: 1,
      rowsPerPage: 0,
    };

    return {
      devices,
      pagination,
      reloadDevices,
      componentKey,
      columns,
      statusIcon,
      goToDeviceDetails,
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
