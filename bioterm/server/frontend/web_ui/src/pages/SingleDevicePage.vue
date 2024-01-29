<template>
  <q-page class="q-pa-md">
    <div v-if="device">
      <DeviceComponent :device="device" />
    </div>
    <div v-else>
      <p>Loading or device not found...</p>
    </div>
  </q-page>
</template>

<script lang="ts">
import { onMounted, ref } from 'vue';
import { useLocalStore } from 'src/stores/localStore';
import { Device } from 'src/types/types';
import DeviceComponent from 'src/components/DeviceComponent.vue';

interface SingleDevicePageProps {
  uuid: string;
}

export default {
  name: 'SingleDevicePage',
  components: { DeviceComponent },
  props: {
    uuid: {
      type: String,
      required: true,
    },
  },
  setup(props: SingleDevicePageProps) {
    const localStore = useLocalStore();
    const device = ref<Device | null>(null);

    onMounted(() => {
      // After component is mounted, find the device with the provided UUID
      const foundDevice = localStore.devices.find((d) => d.uuid === props.uuid);

      if (foundDevice) {
        device.value = foundDevice;
      } else {
        console.log('Cannot find device');
      }
    });

    return {
      device,
    };
  },
};
</script>

<style scoped></style>
