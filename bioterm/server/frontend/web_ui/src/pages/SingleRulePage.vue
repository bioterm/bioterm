<template>
  <q-page class="q-pa-md">
    <q-card class="q-pa-md">
      <q-item-label class="text-h5 text-accent">
        Rule: {{ rule.display_name }}
      </q-item-label>
      <q-form @submit="submit">
        <div v-if="rule">
          <RuleComponent :rule="rule" />
        </div>
        <div v-else>
          <p>Loading or rule not found...</p>
        </div>
        <!-- Form Submit and Cancel Buttons -->
        <div class="q-pa-xs">
          <q-btn label="Submit" type="submit" color="primary" />
          <q-btn
            label="Cancel"
            color="primary"
            flat
            class="q-ml-sm"
            @click="cancel"
          />
        </div>
      </q-form>
    </q-card>
  </q-page>
</template>

<script lang="ts">
import { computed } from 'vue';
import { useLocalStore } from 'src/stores/localStore';
import {
  RuleModel,
  Rule,
  Condition,
  Method,
  RuleCreate,
  RuleUpdate,
} from 'src/types/rules';
import RuleComponent from 'src/components/RuleComponent.vue';
import { useRouter } from 'vue-router';
import apiservice from 'src/services/ApiService';

interface SingleRulePageProps {
  uuid: string | undefined;
}

export default {
  name: 'SingleRulePage',
  components: { RuleComponent },
  props: {
    uuid: {
      type: String,
      required: false,
    },
  },
  setup(props: SingleRulePageProps) {
    const router = useRouter();

    const localStore = useLocalStore();
    const rule = computed<RuleModel>(() => {
      if (props.uuid) {
        const foundRule = localStore.rules.find((d) => d.uuid === props.uuid);
        if (foundRule) {
          return JSON.parse(JSON.stringify(foundRule)) as RuleModel;
        }
      }
      return {
        sync: false,
        display_name: '',
        description: '',
        rule: {
          device: '',
          trigger_condition: {} as Condition,
          trigger_method: {} as Method,
          release_condition: {} as Condition,
          release_method: {} as Method,
        } as Rule,
      } as RuleModel;
    });

    async function createOrUpdateRule(rule: RuleModel) {
      if (props.uuid) {
        console.log('Editing existing rule...');
        const dto: RuleUpdate = {
          sync: rule.sync,
          display_name: rule.display_name,
          description: rule.description,
          rule: rule.rule,
        };
        if (localStore.selectedController) {
          await apiservice
            .updateRule(
              localStore.selectedController.uuid,
              rule.uuid as string,
              dto,
            )
            .then(() => {
              router.push('/rules');
            });
        }
      } else {
        console.log('Adding new rule...');
        const dto: RuleCreate = {
          sync: rule.sync,
          display_name: rule.display_name,
          description: rule.description,
          rule: rule.rule,
        };
        if (localStore.selectedController) {
          await apiservice
            .addRule(localStore.selectedController.uuid, dto)
            .then(() => {
              router.push('/rules');
            })
            .catch();
        }
      }
    }

    async function cancel() {
      router.push('/rules');
    }

    async function submit(event: Event) {
      console.log(rule.value);
      event.preventDefault();
      await createOrUpdateRule(rule.value);
    }

    return {
      rule,
      cancel,
      submit,
    };
  },
};
</script>

<style scoped></style>
