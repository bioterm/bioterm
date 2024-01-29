<template>
  <div>
    <q-toggle v-model="myrule.sync" label="Sync" />
    <q-input
      label="Rule Name"
      v-model="myrule.display_name"
      placeholder="Enter a unique name"
    />
    <q-input
      label="Description"
      v-model="myrule.description"
      placeholder="Give a short description of this rule (max. 100 symbols)"
    />
    <q-select
      label="Device"
      hint="Select the device which will be affected by this rule"
      :multiple="false"
      v-model="myrule.rule.device"
      :options="availableDevices"
      map-options
      emit-value
    />

    <!-- Trigger Method -->
    <div v-if="selectedDevice">
      <div class="q-pa-xs">
        <q-separator color="purple" />
      </div>
      <q-card-section>
        <div class="text-h6 text-accent">
          Trigger Method
          <q-btn
            color="accent"
            round
            flat
            dense
            :icon="
              expandedTriggerMethod
                ? 'keyboard_arrow_up'
                : 'keyboard_arrow_down'
            "
            @click="expandedTriggerMethod = !expandedTriggerMethod"
          />
        </div>
      </q-card-section>
      <q-slide-transition>
        <div v-show="expandedTriggerMethod">
          <MethodComponent
            :model-value="myrule.rule.trigger_method"
            :device="selectedDevice"
            @update:modelValue="handleModelUpdateTriggerMethod"
          />
        </div>
      </q-slide-transition>
    </div>

    <div class="q-pa-xs">
      <q-separator color="purple" />
    </div>
    <q-card-section>
      <div class="text-h6 text-accent">
        Trigger Condition
        <q-btn
          color="accent"
          round
          flat
          dense
          :icon="
            expandedTriggerCondition
              ? 'keyboard_arrow_up'
              : 'keyboard_arrow_down'
          "
          @click="expandedTriggerCondition = !expandedTriggerCondition"
        />
      </div>
    </q-card-section>
    <q-slide-transition>
      <div v-show="expandedTriggerCondition">
        <ConditionComponent
          v-model="myrule.rule.trigger_condition"
          @update:modelValue="handleModelUpdateTriggerCondition"
        />
      </div>
    </q-slide-transition>

    <!-- Release Method -->
    <div v-if="selectedDevice">
      <div class="q-pa-xs">
        <q-separator color="purple" />
      </div>
      <q-card-section>
        <div class="text-h6 text-accent">
          Release Method
          <q-btn
            color="accent"
            round
            flat
            dense
            :icon="
              expandedReleaseMethod
                ? 'keyboard_arrow_up'
                : 'keyboard_arrow_down'
            "
            @click="expandedReleaseMethod = !expandedReleaseMethod"
          />
        </div>
      </q-card-section>
      <q-slide-transition>
        <div v-show="expandedReleaseMethod">
          <MethodComponent
            :model-value="myrule.rule.release_method"
            :device="selectedDevice"
            @update:modelValue="handleModelUpdateReleaseMethod"
          />
        </div>
      </q-slide-transition>
    </div>

    <!-- Release Condition -->
    <div class="q-pa-xs">
      <q-separator color="purple" />
    </div>
    <q-card-section>
      <div class="text-h6 text-accent">
        Release Condition
        <q-btn
          color="accent"
          round
          flat
          dense
          :icon="
            expandedReleaseCondition
              ? 'keyboard_arrow_up'
              : 'keyboard_arrow_down'
          "
          @click="expandedReleaseCondition = !expandedReleaseCondition"
        />
      </div>
    </q-card-section>
    <q-slide-transition>
      <div v-show="expandedReleaseCondition">
        <ConditionComponent
          v-model="myrule.rule.release_condition"
          @update:modelValue="handleModelUpdateReleaseCondition"
        />
      </div>
    </q-slide-transition>
  </div>
</template>

<script lang="ts">
import { ref, computed, PropType } from 'vue';
import { useLocalStore } from 'src/stores/localStore';
import { Condition, RuleModel, Method } from 'src/types/rules';
import { Device } from 'src/types/types';
import ConditionComponent from './ConditionComponent.vue';
import MethodComponent from './MethodComponent.vue';

interface RuleComponentProps {
  rule: RuleModel;
}

type AvailableDevice = {
  label: string;
  value: string;
};

export default {
  name: 'RuleComponent',
  props: {
    rule: {
      type: Object as PropType<RuleModel>,
      required: true,
    },
  },
  setup(props: RuleComponentProps) {
    const expandedTriggerCondition = ref(false);
    const expandedTriggerMethod = ref(false);
    const expandedReleaseCondition = ref(false);
    const expandedReleaseMethod = ref(false);
    const localStore = useLocalStore();
    const myrule = ref<RuleModel>(props.rule);

    const availableDevices = computed<Array<AvailableDevice>>(() =>
      localStore.devices.map((device: Device) => {
        return {
          label: (device.display_name ?? '') + ` (${device.uuid})`,
          value: device.uuid,
        };
      }),
    );

    const selectedDevice = computed(() => {
      return (
        localStore.devices.find(
          (device) => device.uuid === myrule.value?.rule?.device,
        ) || null
      );
    });

    const handleModelUpdateTriggerCondition = (newCondition: Condition) => {
      myrule.value.rule.trigger_condition = newCondition;
    };

    const handleModelUpdateReleaseCondition = (newCondition: Condition) => {
      myrule.value.rule.release_condition = newCondition;
    };

    const handleModelUpdateTriggerMethod = (newMethod: Method) => {
      myrule.value.rule.trigger_method = newMethod;
    };

    const handleModelUpdateReleaseMethod = (newMethod: Method) => {
      myrule.value.rule.release_method = newMethod;
    };

    return {
      myrule,
      availableDevices,
      handleModelUpdateTriggerCondition,
      handleModelUpdateReleaseCondition,
      handleModelUpdateTriggerMethod,
      handleModelUpdateReleaseMethod,
      expandedTriggerCondition,
      expandedTriggerMethod,
      expandedReleaseCondition,
      expandedReleaseMethod,
      selectedDevice,
    };
  },
  components: { ConditionComponent, MethodComponent },
};
</script>
