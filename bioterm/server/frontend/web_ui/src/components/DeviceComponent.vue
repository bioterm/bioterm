<template>
  <div>
    <q-card class="device-card q-pt-xs q-mb-xs">
      <q-card-section class="q-pt-xs q-mb-xs">
        <q-item-section>
          <q-item-label class="text-h5 text-accent">{{
            device.display_name || device.uuid
          }}</q-item-label>
          <q-item-label caption>{{ device.uuid }} </q-item-label>
        </q-item-section>
      </q-card-section>
      <q-card-section class="q-pt-xs q-mb-xs">
        <q-list>
          <div class="row">
            <div
              class="col-12 col-sm-6 col-md-4 q-pa-md"
              v-for="(iframeSrc, index) in iframeLinks"
              :key="index"
            >
              <GrafanaPanelIFrameComponent
                :iframeLink="iframeSrc"
              ></GrafanaPanelIFrameComponent>
            </div>
          </div>
        </q-list>
      </q-card-section>

      <div class="q-pa-md">
        <div class="q-gutter-y-md">
          <q-tabs v-model="tab" class="text-teal" indicator-color="accent">
            <q-tab
              name="information"
              icon="fa-solid fa-info"
              label="Information"
            />
            <!-- <q-tab
              name="parameters"
              icon="fa-solid fa-sliders"
              label="Parameters"
            /> -->
            <q-tab
              name="functions"
              icon="fa-solid fa-diagram-next"
              label="Methods"
            />
          </q-tabs>
        </div>
      </div>

      <q-separator color="purple" inset />
      <q-card-section class="q-pt-xs q-mb-xs">
        <q-tab-panels
          v-model="tab"
          animated
          vertical
          transition-prev="jump-left"
          transition-next="jump-right"
        >
          <q-tab-panel name="information">
            <p>{{ device.description }}</p>
          </q-tab-panel>
          <!-- <q-tab-panel name="parameters">
            <p>This is were the uploader for local edited files will be.</p>
          </q-tab-panel> -->
          <q-tab-panel name="functions">
            <q-card-section class="q-pt-xs q-mb-xs">
              <q-item-section>
                <q-item-label class="text-h5 q-pt-xs q-mb-xs"
                  >Methods</q-item-label
                >
              </q-item-section>
            </q-card-section>
            <q-card-section class="q-pa-md row item-start">
              <div
                class="col-xs-12 col-sm-6 col-md-4"
                v-for="(rpc, key) in parsedRPCs"
                :key="key"
              >
                <q-card class="q-ma-xs">
                  <q-card-section>
                    <div class="text-h6">
                      {{ formattedKey(key as string) }}
                    </div></q-card-section
                  >

                  <q-form @submit="sendData(key)">
                    <q-card-section v-for="param in rpc" :key="param.id">
                      <q-input
                        v-if="
                          PythonToTypeScriptTypes[param.return_type] === String
                        "
                        :label="param.name"
                        :model-value="paramValues[param.id] as string"
                        :rules="paramToRules(param)"
                        @update:modelValue="
                          (value) => {
                            paramValues[param.id] = value;
                            formData[key][param.id] = value;
                          }
                        "
                        clearable
                      ></q-input>
                      <q-input
                        v-if="param.return_type === '<class \'int\'>'"
                        :label="param.name"
                        type="number"
                        :model-value="parseInt(paramValues[param.id] as string)"
                        :rules="paramToRules(param)"
                        @update:modelValue="
                          (value) => {
                            const intValue = parseInt(value as string);
                            paramValues[param.id] = intValue;
                            formData[key][param.id] = intValue;
                          }
                        "
                        clearable
                      ></q-input>
                      <q-input
                        v-if="param.return_type === '<class \'float\'>'"
                        :label="param.name"
                        type="text"
                        :model-value="
                          parseFloat(paramValues[param.id] as string)
                        "
                        :rules="paramToRules(param)"
                        @update:modelValue="
                          (value) => {
                            const floatValue = parseFloat(value as string);
                            paramValues[param.id] = floatValue;
                            formData[key][param.id] = floatValue;
                          }
                        "
                        clearable
                      ></q-input>
                    </q-card-section>
                    <q-card-actions vertical align="stretch">
                      <q-btn color="accent" :label="'SEND'" type="submit">
                      </q-btn>
                    </q-card-actions>
                  </q-form>
                </q-card>
              </div>
            </q-card-section>
          </q-tab-panel>
        </q-tab-panels>
      </q-card-section>
    </q-card>
  </div>
</template>

<script lang="ts">
import { Device, Panel, RPCParam, RPCs } from "src/types/types";
import { useUserStore } from "src/stores/user";
import { useLocalStore } from "src/stores/localStore";
import { ref, onMounted, watch, computed, Teleport } from "vue";
import axios from "axios";
import auth from "src/services/AuthService";
import GrafanaPanelIFrameComponent from "src/components/GrafanaPanelIFrameComponent.vue";

export default {
  name: "DeviceComponent",
  order: 0,
  components: { GrafanaPanelIFrameComponent },
  props: {
    device: {
      type: Object as () => Device,
      required: true,
    },
  },
  setup(props: { device: Device }) {
    const userStore = useUserStore();
    const localStore = useLocalStore();
    const thisDevice = ref(props.device);
    const iframeLinks = ref<string[]>([]);
    const slide = ref("0");
    const expanded = ref(false);
    const modalOpened = ref(false);
    const selectedIframe = ref("");

    const PythonToTypeScriptTypes = ref({
      "<class 'int'>": Number,
      "<class 'float'>": Number,
      "<class 'str'>": String,
      // ... other type mappings
    });

    const paramValues = ref<{ [id: string]: unknown }>({});
    const formData = ref<{ [key: string]: { [paramId: string]: unknown } }>({});

    const openModal = (iframeLink: string) => {
      selectedIframe.value = iframeLink;
      modalOpened.value = true;
    };

    const fetchIframes = async () => {
      try {
        const access_token = await auth.getAccessToken();
        const response = await axios.get(
          `${process.env.API_URL}/api/v0/devices/${thisDevice.value.uuid}/panels`,
          {
            headers: { Authorization: `Bearer ${access_token}` },
          },
        );
        iframeLinks.value = response.data.map((panel: Panel) => {
          const iframeSrc = panel.link;

          if (iframeSrc) {
            try {
              // Assuming iframeSrc is a string that contains the entire '<iframe ...></iframe>' element
              // We create a DOM parser to parse the string and extract the 'src' attribute
              const parser = new DOMParser();
              const doc = parser.parseFromString(iframeSrc, "text/html");
              const iframeElement = doc.querySelector("iframe");

              if (iframeElement) {
                const srcAttributeValue = iframeElement.getAttribute("src");

                if (srcAttributeValue) {
                  // Now use the 'src' attribute value to create a new URL object
                  const srcUrl = new URL(srcAttributeValue);

                  const params = srcUrl.searchParams;
                  params.set(
                    "theme",
                    localStore.darkMode === true ? "dark" : "light",
                  );
                  params.set("refresh", "1s");
                  params.set("from", "now-1m");
                  params.set("to", "now");

                  return srcUrl.toString();
                } else {
                  console.error(
                    "No src attribute found in the iframe tag:",
                    iframeSrc,
                  );
                  return "";
                }
              } else {
                console.error(
                  "No <iframe> element found in the provided string:",
                  iframeSrc,
                );
                return "";
              }
            } catch (error) {
              console.error(
                "An error occurred while processing the iframe string:",
                error,
              );
              return "";
            }
          } else {
            console.error("iframeSrc is null for panel:", panel);
            return "";
          }
        });
      } catch (error) {
        console.error("An error occurred while fetching metadata:", error);
      }
    };

    // q-input ALWAYS returns strings
    type Rule = (val: string) => boolean | string;

    function paramToRules(param: RPCParam) {
      const rules: Array<Rule> = [];
      if (
        param.return_type == "<class 'int'>" ||
        param.return_type == "<class 'float'>"
      ) {
        const maxValue = param.maxValue ?? Infinity;
        const minValue = param.minValue ?? -Infinity;
        if (param.return_type == "<class 'int'>") {
          rules.push(
            (val: string) =>
              (val !== null &&
                val !== undefined &&
                !isNaN(Number(val)) &&
                Number.isInteger(Number(val))) ||
              "Must be an integer (that means a number without decimals)",
          );
        }

        if (!isNaN(maxValue)) {
          rules.push(
            (val: string) =>
              (val !== null && val !== undefined && Number(val) <= maxValue) ||
              `Max: ${maxValue}`,
          );
        }
        if (!isNaN(minValue)) {
          rules.push(
            (val: string) =>
              (val !== null && val !== undefined && Number(val) >= minValue) ||
              `Min: ${minValue}`,
          );
        }
      } else if (param.return_type == "<class 'str'>") {
        const regex = param.regex;
        if (regex) {
          const re = new RegExp(regex);
          rules.push((val: string) => (val && re.test(val)) || "Wrong format");
        }
      }
      return rules;
    }

    const parsedRPCs = computed<RPCs>(() => {
      if (typeof props.device.rpc === "object" && props.device.rpc !== null) {
        return props.device.rpc as RPCs;
      }
      return {};
    });

    const formattedKey = (key: string): string => {
      return key
        .replace(/_/g, " ")
        .split(" ")
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
        .join(" ");
    };

    const sendData = async (keyName: string) => {
      const endpoint = `${process.env.API_URL}/api/v0/devices/${thisDevice.value.uuid}/rpc`;
      const payload = {
        key: keyName,
        params: formData.value[keyName],
        // ... other data if required
      };

      // Log the request details
      console.log("Making POST request to:", endpoint);
      console.log("Payload:", payload);
      try {
        const access_token = await auth.getAccessToken();
        const response = await axios.post(
          endpoint,
          payload, // Passing the payload data
          {
            headers: { Authorization: `Bearer ${access_token}` },
          },
        );

        // Handle the response if necessary
        console.log("Response:", response.data);
      } catch (error) {
        console.error("An error occurred while sending data:", error);
      }
    };

    onMounted(() => {
      for (const key in parsedRPCs.value) {
        formData.value[key] = {};
      }
      fetchIframes();
    });

    watch(() => localStore.darkMode, fetchIframes);
    // watch(() => props.selectedTime, fetchIframes);

    return {
      userStore,
      slide,
      iframeLinks,
      parsedRPCs,
      formattedKey,
      PythonToTypeScriptTypes,
      paramValues,
      expanded,
      sendData,
      formData,
      openModal,
      selectedIframe,
      modalOpened,
      Teleport,
      tab: ref("information"),
      paramToRules,
    };
  },
};
</script>

<style scoped>
.iframe-container {
  position: relative;
  /* Ensure the container takes up the full width/height of the iframe */
  width: 100%;
  height: 20vh; /* Adjust to be the same as the iframe height */
  min-height: 200px; /* Adjust as per your requirement */
}

.iframe-content {
  width: 100%;
  height: 100%;
  border: none;
  /* Ensuring the iframe has absolute positioning can remove some potential issues */
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1; /* Lower z-index than the shim */
}

.iframe-shim {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 2; /* Higher z-index than the iframe content, but below anything interactive */
  background-color: transparent; /* Ensure the shim doesn't obscure the iframe */
  /* Add cursor indication if the shim is meant to be interactive */
  /* cursor: pointer; */
}
</style>
