<template>
  <div class="q-pa-xs q-gutter-md">
    <q-card :key="reRenderKey" class="q-pa-xs q-gutter-xs">
      <q-select
        label="Operator"
        hint="Select Operator"
        v-model="operator"
        :options="operators"
        map-options
        emit-value
      />
      <div v-if="showEnumWarning" class="text-negative">
        Warning: Selected operator is neither 'equal' nor 'not equal' for an
        enum type.
      </div>
      <!-- <q-input type="number" label="dwell" v-model="dwell" /> -->
      <div v-if="operatorType == 'ValueCondition'">
        <q-select
          label="Device"
          hint="Select Device of which to read Measurement or Parameter"
          v-model="device"
          :options="availableDevices"
          map-options
          emit-value
        />
        <q-select
          label="Variable Name"
          hint="Select the measurement or parameter name"
          v-model="variable"
          :options="availableVariables"
          map-options
          emit-value
        />
        <q-input
          v-if="isIntegerType"
          label="Integer"
          type="number"
          v-model="variableValue"
          clearable
          emit-value
          :rules="paramToRules(variableDetails as PropertyDefinition)"
        ></q-input>
        <q-input
          v-if="isFloatType"
          label="Float"
          type="number"
          v-model="variableValue"
          clearable
          emit-value
          :rules="paramToRules(variableDetails as PropertyDefinition)"
        ></q-input>
        <q-select
          v-if="isEnumType"
          label="Enum Value"
          hint="Select from the enum values"
          v-model="variableValue"
          :options="enumOptions"
          map-options
          emit-value
        />
      </div>

      <div v-if="operatorType == 'LogicCondition'">
        <div
          v-for="(nestedCondition, index) in nestedConditions"
          :key="index"
          class="row items-center"
        >
          <q-btn
            v-if="canRemoveCondition"
            round
            icon="remove"
            color="negative"
            @click="removeCondition(index)"
            class="q-mr-sm"
            size="sm"
          ></q-btn>
          <div class="col">
            <condition-component
              :model-value="nestedCondition"
              @update:modelValue="updateNestedCondition(index, $event)"
            ></condition-component>
          </div>
        </div>
        <div class="row justify-center">
          <q-btn
            round
            icon="add"
            @click="addValueCondition"
            color="primary"
            size="sm"
          ></q-btn>
        </div>
      </div>
    </q-card>
  </div>
</template>

<script setup lang="ts">
import { Condition, ValueCondition, LogicCondition } from 'src/types/rules';
import { ref, computed, watch } from 'vue';
import { useLocalStore } from 'src/stores/localStore';
import { Device } from 'src/types/types';

// Import the component itself for recursion
import ConditionComponent from './ConditionComponent.vue';

type AvailableDevice = {
  label: string;
  value: string;
};

interface EnumDefinition {
  enum: string[];
  type: string;
  title: string;
}

interface PropertyDefinition {
  type?: string;
  title?: string;
  maximum?: number;
  minimum?: number;
  $ref?: string;
}

interface MeasurementModel {
  properties: {
    [key: string]: PropertyDefinition;
  };
  $defs?: {
    [key: string]: EnumDefinition;
  };
}

const localStore = useLocalStore();
const showEnumWarning = ref(false);
const reRenderKey = ref(0);

const availableDevices = computed<Array<AvailableDevice>>(() =>
  localStore.devices.map((device: Device) => {
    return {
      label: (device.display_name ?? '') + ` (${device.uuid})`,
      value: device.uuid,
    };
  }),
);

const availableVariables = computed<Array<string>>(() => {
  const selectedDevice = localStore.devices.find(
    (d) => d.uuid === device.value,
  );
  return selectedDevice
    ? (selectedDevice.measurement_model.required as string[])
    : [];
});

const variableDetails = computed<PropertyDefinition | EnumDefinition | null>(
  () => {
    const selectedDevice = localStore.devices.find(
      (d: Device) => d.uuid === device.value,
    );
    if (!selectedDevice || !variable.value) return null;

    const measurementModel =
      selectedDevice.measurement_model as unknown as MeasurementModel;
    const properties = measurementModel.properties;
    const variableName = variable.value;

    if (variableName in properties) {
      const detail = properties[variableName];

      if (detail.$ref) {
        const refKey = detail.$ref.split('/').pop();
        if (!refKey || !measurementModel.$defs) return null;

        const enumDefinition = measurementModel.$defs[refKey] as EnumDefinition;
        if (enumDefinition) {
          return { ...detail, enum: enumDefinition.enum, type: 'enum' };
        }
      }

      return detail;
    }

    return null;
  },
);

const isIntegerType = computed(() => {
  return variableDetails.value?.type === 'integer';
});

const isFloatType = computed(() => {
  return variableDetails.value?.type === 'number';
});

const isEnumType = computed(() => {
  const details = variableDetails.value;
  return details && details.type === 'enum';
});

const props = defineProps<{
  modelValue: Condition;
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: Condition): void;
}>();

// internal models

const operator = ref<string>(props.modelValue?.operator ?? 'eq');

const dwell = ref<number>(props.modelValue?.dwell ?? 0);
const device = ref<string>((props.modelValue as ValueCondition)?.device ?? '');
const variable = ref<string>((props.modelValue as ValueCondition)?.meas ?? '');
const variableValue = ref<string | number>(
  (props.modelValue as ValueCondition)?.value ?? '',
);

const enumOptions = computed(() => {
  if (isEnumType.value && variableDetails.value?.type === 'enum') {
    const enumDefinition: EnumDefinition =
      variableDetails.value as EnumDefinition;
    return enumDefinition.enum.map((enumValue) => {
      return { label: enumValue, value: enumValue };
    });
  }
  return [];
});

// Computed property for nested conditions
const nestedConditions = computed(() => {
  if (props.modelValue && 'conditions' in props.modelValue) {
    return (props.modelValue as LogicCondition).conditions;
  }
  return [];
});

const canRemoveCondition = computed(() => {
  return nestedConditions.value.length > 1;
});

// Method to add a new ValueCondition
function addValueCondition() {
  const defaultValueCondition: ValueCondition = {
    // Set default properties for new ValueCondition
    operator: 'eq', // Example default operator
    device: '', // Default device
    meas: '', // Default measurement
    value: 0, // Default value
    dwell: 0, // Default dwell
  };

  if (props.modelValue && 'conditions' in props.modelValue) {
    (props.modelValue as LogicCondition).conditions.push(defaultValueCondition);
    emit('update:modelValue', props.modelValue);
  }
}

function removeCondition(index: number) {
  if (
    canRemoveCondition.value &&
    props.modelValue &&
    'conditions' in props.modelValue
  ) {
    (props.modelValue as LogicCondition).conditions.splice(index, 1);
    emit('update:modelValue', props.modelValue);
    reRenderKey.value++; // Increment to trigger re-render
  }
}

// Method to handle updates in nested conditions
function updateNestedCondition(index: number, updatedCondition: Condition) {
  if (props.modelValue && 'conditions' in props.modelValue) {
    (props.modelValue as LogicCondition).conditions[index] = updatedCondition;
    emit('update:modelValue', props.modelValue);
  }
}

// q-input ALWAYS returns strings
type Rule = (val: string) => boolean | string;

function paramToRules(param: PropertyDefinition) {
  const rules: Array<Rule> = [];
  const maxValue = param.maximum ?? Infinity;
  const minValue = param.minimum ?? -Infinity;

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
  if (param.type == 'integer') {
    rules.push(
      (val: string) =>
        (val !== null &&
          val !== undefined &&
          !isNaN(Number(val)) &&
          Number.isInteger(Number(val))) ||
        'Must be an integer (that means a number without decimals)',
    );
  }
  return rules;
}

function update() {
  // Check if operatorType is defined
  if (operatorType.value) {
    let condition: Condition;

    if (operatorType.value === 'ValueCondition') {
      // For ValueCondition, include device and dwell
      condition = {
        operator: operator.value,
        dwell: dwell.value,
        device: device.value,
        meas: variable.value,
        value: variableValue.value,
      } as ValueCondition;
    } else {
      condition = {
        operator: operator.value,
        dwell: dwell.value,
        conditions: nestedConditions.value,
      } as LogicCondition;
    }

    emit('update:modelValue', condition);
  }
}

watch(device, (newValue, oldValue) => {
  if (newValue !== oldValue) {
    variableValue.value = '';
    // If the device changes, update the variable selection
    const newAvailableVariables = availableVariables.value;
    variable.value =
      newAvailableVariables.length > 0 ? newAvailableVariables[0] : '';
  }
});

watch(operator, (newOperator, oldOperator) => {
  const defaultValueCondition: ValueCondition = {
    operator: 'eq',
    device: '',
    meas: '',
    value: 0,
    dwell: 0,
  };

  const currentOperatorType = operators.find((op) => op.value === oldOperator)
    ?.type;
  const newOperatorType = operators.find((op) => op.value === newOperator)
    ?.type;

  if (newOperatorType === 'LogicCondition') {
    let newConditions: Condition[];
    console.log('props.modelValue', props.modelValue);
    if (currentOperatorType === 'ValueCondition') {
      // Switching from ValueCondition to LogicCondition
      console.log('Switching from ValueCondition to LogicCondition');
      newConditions = [defaultValueCondition];
    } else if (props.modelValue && 'conditions' in props.modelValue) {
      // Already in LogicCondition
      console.log('Switching from LogicCondition to LogicCondition');
      newConditions = props.modelValue.conditions as Condition[];
    } else {
      // Default case if conditions are not present
      console.log('This should not happen');
      newConditions = [];
    }

    let newModelValue: LogicCondition = {
      operator: newOperator as 'AND' | 'OR',
      conditions: newConditions,
      dwell: dwell.value,
    };

    emit('update:modelValue', newModelValue);
  }
});

watch([operator, variableValue], () => {
  const isOperatorForValueCondition =
    operators.find((op) => op.value === operator.value)?.type ===
    'ValueCondition';

  // Check if the selected type is an enum and operator is not 'eq' or 'neq'
  if (
    isEnumType.value &&
    isOperatorForValueCondition &&
    operator.value !== 'eq' &&
    operator.value !== 'neq'
  ) {
    showEnumWarning.value = true;
  } else {
    showEnumWarning.value = false;
  }
});

watch([operator, dwell, device, variable, variableValue], () => {
  update();
});

const operators = [
  {
    label: 'equal',
    value: 'eq',
    type: 'ValueCondition',
  },
  {
    label: 'less than',
    value: 'le',
    type: 'ValueCondition',
  },
  {
    label: 'less than or equal to',
    value: 'leq',
    type: 'ValueCondition',
  },
  {
    label: 'greater than',
    value: 'ge',
    type: 'ValueCondition',
  },
  {
    label: 'greater than or equal to',
    value: 'geq',
    type: 'ValueCondition',
  },
  {
    label: 'not equal',
    value: 'neq',
    type: 'ValueCondition',
  },
  {
    label: 'logic AND',
    value: 'AND',
    type: 'LogicCondition',
  },
  {
    label: 'logic OR',
    value: 'OR',
    type: 'LogicCondition',
  },
];

const operatorType = computed<string | null>(() => {
  const value = operator.value;
  return operators.find((item) => item.value === value)?.type ?? null;
});
</script>
