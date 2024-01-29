<template>
  <div class="single-iframe-component">
    <div class="iframe-container">
      <div class="iframe-shim" @pointerdown="openModal"></div>
      <iframe
        class="iframe-content"
        :class="{ 'iframe-modal-position': modalOpened }"
        :src="iframeLink"
        frameborder="0"
        style="width: 100%; height: 20vh; min-height: 200px"
      ></iframe>
    </div>

    <!-- <q-dialog v-model="modalOpened" fullscreen>
      <q-card>
        <q-card-section class="bg-primary text-white">
          <div class="text-h6">Details</div>
        </q-card-section>

        <q-card-section>
          <iframe
            class="iframe-content"
            :class="{ 'iframe-modal-position': modalOpened }"
            :src="iframeLink"
            frameborder="0"
          ></iframe>
        </q-card-section>

        <q-card-section>
          <q-btn flat label="Close" @click="closeModal" v-close-popup></q-btn>
        </q-card-section>
      </q-card>
    </q-dialog> -->
  </div>
</template>

<script lang="ts">
import { ref } from "vue";

export default {
  name: "SingleIframeComponent",
  props: {
    iframeLink: {
      type: String,
      required: true,
    },
  },
  setup() {
    const modalOpened = ref(false);

    const openModal = () => {
      modalOpened.value = true;
    };

    const closeModal = () => {
      modalOpened.value = false;
    };

    return {
      modalOpened,
      openModal,
      closeModal,
    };
  },
};
</script>
<style scoped>
.iframe-container {
  position: relative;
  width: 100%;
  height: 20vh;
  min-height: 200px;
}

.iframe-content {
  width: 100%;
  height: 100%;
  border: none;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}

.iframe-shim {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 2;
  background-color: transparent;
  /* cursor: pointer; */
}

/* .iframe-modal-position {
  position: fixed;
  top: 10%;
  left: 10%;
  width: 60%;
  height: 60%;
  z-index: 1000;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
} */
</style>
