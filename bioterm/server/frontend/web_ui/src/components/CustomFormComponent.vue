<template>
  <div>
    <q-card flat>
      <q-card-section>
        {{ prompt }}
        <q-form
          @submit.prevent="handleSubmit"
          @reset="onReset"
          class="q-gutter-md"
        >
          <div v-for="input in inputs" :key="input.label">
            <q-input
              v-if="input.type === InputTypes.TEXT"
              :label="input.label"
              :model-value="typedFormData[input.model] as string"
              @update:model-value="
                (val: string | number | null | undefined) =>
                  (formData[input.model] = val)
              "
              :disable="locked"
              autogrow
              clearable
              :error="input.model in fielderrors"
              :error-message="fielderrors[input.model] ?? ''"
            ></q-input>
            <q-input
              v-if="input.type === InputTypes.NUMBER"
              :label="input.label"
              type="number"
              :model-value="typedFormData[input.model] as number"
              @update:model-value="
                (val: string | number | null | undefined) =>
                  (formData[input.model] = val)
              "
              mask="#"
              reverse-fill-mask
              :disable="locked"
              autogrow
              clearable
            ></q-input>
            <q-checkbox
              v-if="input.type === InputTypes.BOOLEAN"
              :label="input.label"
              color="primary"
              keep-color
              :model-value="typedFormData[input.model] as boolean"
              @update:model-value="
                (val: boolean) => (formData[input.model] = val)
              "
            ></q-checkbox>
            <!-- <q-select
              v-if="input.type === InputTypes.BOOLEAN"
              :label="input.label"
              :model-value="(typedFormData[input.model] as boolean)"
              :options="booleanOptions"
              :disable="locked"
              autogrow
              @update:model-value="(val) => (formData[input.model] = val)"
            ></q-select> -->

            <!-- add more conditions here for other input types e.g. textarea, select, etc. -->
          </div>
          <div>
            <q-btn
              label="Submit"
              type="submit"
              color="primary"
              :disable="locked"
            />
            <q-btn
              label="Reset"
              type="reset"
              color="primary"
              flat
              class="q-ml-sm"
              :disable="locked"
            />
          </div>
        </q-form>
      </q-card-section>
    </q-card>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, watch } from 'vue';

export type ItemData = Record<string, unknown>;

export type FieldErrors = Record<string, string | null>;

interface InputElement {
  type: string;
  label: string;
  model: string;
  autocomplete?: boolean;
  defaultValue?: unknown;
  nullable?: boolean;
}

// this probably needs to be expanded
export enum InputTypes {
  TEXT = 'text',
  BOOLEAN = 'boolean',
  NUMBER = 'number',
  JSON = 'json',
}

export default defineComponent({
  props: {
    prompt: {
      type: String,
      required: true,
    },
    inputs: {
      type: Array<InputElement>,
      required: true,
    },
    defaultValues: {
      type: Object as () => ItemData,
      default: () => ({}),
    },
    locked: {
      type: Boolean,
      required: false,
      default: false,
    },
    fielderrors: {
      type: Object as () => FieldErrors,
      default: () => ({}),
    },
  },

  setup(props, { emit }) {
    const formData = ref({} as ItemData);

    const typedFormData = computed(() => {
      const output: ItemData = {};
      Object.keys(formData.value).forEach((key) => {
        output[key] = formData.value[key];
      });
      return output;
    });

    // const initializeFormData = () => {
    //   props.inputs.forEach((input) => {
    //     (formData.value as Record<string, unknown>)[input.model] =
    //       input.defaultValue;
    //   });
    // };

    const initializeFormData = () => {
      props.inputs.forEach((input) => {
        (formData.value as ItemData)[input.model] =
          props.defaultValues[input.model] ?? input.defaultValue;
      });
    };

    watch(
      () => props.defaultValues,
      () => {
        initializeFormData();
      },
      { deep: true },
    );

    watch(
      formData,
      (newFormData) => {
        for (const [key, value] of Object.entries(newFormData)) {
          if (value === '') {
            const correspondingInput = props.inputs.find(
              (input) => input.model === key,
            );
            if (
              correspondingInput &&
              correspondingInput.type === InputTypes.NUMBER
            ) {
              formData.value[key] = null;
            }
          }
        }
      },
      { deep: true },
    );

    const onReset = () => {
      initializeFormData();
    };

    const handleSubmit = () => {
      // Emit the form data to the parent component
      emit('submit', formData.value);
    };

    initializeFormData();

    return {
      formData,
      typedFormData,
      InputTypes,
      handleSubmit,
      onReset,
    };
  },
});
</script>

<style scoped>
/* Add any required styles for the form here */
</style>
