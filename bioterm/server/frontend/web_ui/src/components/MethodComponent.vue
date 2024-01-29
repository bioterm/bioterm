<template>
  <div class="q-pa-xs q-gutter-md">
    <q-card class="q-pa-xs q-gutter-xs">
      <div v-if="availableMethods.length > 0">
        <q-select
          label="Method"
          hint="Select Method"
          v-model="method"
          :options="availableMethods"
          map-options
          emit-value
        />
        <div class="col-xs-12 col-sm-6 col-md-4" v-if="rpc">
          <div v-for="param in rpc" :key="param.id" class="q-mt-md">
            <q-input
              :label="param.name"
              :type="paramToFormType(param)"
              :rules="paramToRules(param)"
              v-model="paramValues[param.id]"
              clearable
              emit-value
            ></q-input>
          </div>
        </div>
      </div>
      <div v-else class="text-negative">No methods are available.</div>
    </q-card>
  </div>
</template>

<script setup lang="ts">
import { Method } from 'src/types/rules';
import { ref, computed, watch } from 'vue';
import { Device, RPCParam } from 'src/types/types';

const availableMethods = computed<Array<string>>(() => {
  return props.device ? Object.keys(props.device.rpc) : [];
});

const props = defineProps<{
  modelValue: Method;
  device: Device;
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: Method): void;
}>();

const method = ref<string>((props.modelValue as Method)?.name ?? '');

const initialParamValues = computed<{ [id: string]: string | null }>(() => {
  if (props.modelValue.arguments) {
    return Object.assign(
      {},
      ...props.modelValue.arguments.map((arg) => ({ [arg.name]: arg.value })),
    );
  }
  return {};
});
const paramValues = ref<{ [id: string]: string | null }>(
  initialParamValues.value,
);

// q-input ALWAYS returns strings
type Rule = (val: string) => boolean | string;

function paramToFormType(param: RPCParam) {
  if (
    param.return_type == "<class 'int'>" ||
    param.return_type == "<class 'float'>"
  ) {
    return 'number';
  } else {
    return 'text';
  }
}

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
          'Must be an integer (that means a number without decimals)',
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
      rules.push((val: string) => (val && re.test(val)) || 'Wrong format');
    }
  }
  return rules;
}

const rpc = computed<RPCParam[]>(() => {
  if (props.device && method.value && props.device.rpc[method.value]) {
    return props.device.rpc[method.value] as RPCParam[];
  } else {
    return [] as RPCParam[];
  }
});

watch(method, () => {
  paramValues.value = {};
});

watch(availableMethods, (newMethods) => {
  if (newMethods.length === 0) {
    method.value = '';
  }
});

watch(
  [method, paramValues, rpc],
  () => {
    update();
  },
  { deep: true },
);

function update() {
  let m: Method = {
    name: method.value,
    arguments: [],
  };

  for (let param of rpc.value) {
    const rawValue = paramValues.value[param.id] ?? null;
    let convertedValue: string | number = rawValue ?? '';
    if (
      param.return_type == "<class 'int'>" ||
      param.return_type == "<class 'float'>"
    ) {
      convertedValue = Number(rawValue);
    }

    m.arguments.push({ name: param.id, value: convertedValue });
  }
  emit('update:modelValue', m);
}
</script>
