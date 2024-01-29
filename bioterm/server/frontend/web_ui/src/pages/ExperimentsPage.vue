<template>
  <q-page
    padding
    class="full-width column no-wrap justify-start items-stretch content-start q-gutter-y-md"
  >
    <div class="row" padding>
      <h1>Experiments</h1>
    </div>

    <div
      class="fit row wrap justify-start items-start content-start q-gutter-x-md"
    >
      <q-select
        v-model="perPage"
        :options="options"
        style="min-width: 175px"
        label="Experiments per page"
      />
    </div>

    <q-separator color="purple" inset />

    <div id="experimentList">
      <q-list separator class="q-gutter-y-xs">
        <div v-for="(experiment, index) in store.experiments" :key="index">
          <template
            v-if="index >= itemIndexLowerLimit && index <= itemIndexUpperLimit"
          >
            <q-expansion-item popup expand-separator group="experimentgroup">
              <template v-slot:header>
                <q-item-section avatar>
                  <q-avatar rounded icon="fa-solid fa-flask"> </q-avatar>
                </q-item-section>
                <q-item-section>
                  <q-item-label class="text-bold">
                    {{ experiment.title }}
                  </q-item-label>
                  <q-item-label caption>
                    <q-badge :style="'background:#' + experiment.color">
                      {{ experiment.category }}</q-badge
                    >
                  </q-item-label>
                  <q-item-label>
                    Next step: <i> {{ experiment.next_step }} </i></q-item-label
                  >
                </q-item-section>
                <q-item-section
                  side
                  avatar
                  clickable
                  @click="
                    onClick(
                      `https:////${process.env.ELN_DOMAIN}/experiments.php?mode=view&id=${experiment.id}`,
                    )
                  "
                >
                  <q-icon name="open_in_new" />
                </q-item-section>
              </template>
              <q-card>
                <q-card-section class="bg-grey-3">
                  <p v-html="experiment.body"></p>
                </q-card-section>
              </q-card>
            </q-expansion-item>
          </template>
        </div>
      </q-list>
    </div>

    <q-separator color="purple" inset />
    <div class="q-pa-md-xs flex flex-center">
      <q-pagination
        v-model="current"
        color="purple"
        :max="pagesRequired"
        input
        input-class="text-purple"
        gutter="xl"
      />
    </div>
  </q-page>
</template>

<script lang="ts">
import { ref } from 'vue';
import { openURL } from 'quasar';
import { useUIContentStore } from 'stores/UIContentStore';

const store = useUIContentStore();

export default {
  name: 'ExperimentsPage',
  setup() {
    return {
      current: ref(1),
      perPage: ref(5),
      options: ['5', '10', '15', '20', '50'],
    };
  },
  data() {
    return {
      store,
    };
  },
  computed: {
    pagesRequired() {
      return Math.ceil(this.store.experiments.length / this.perPage);
    },
    itemIndexLowerLimit() {
      return this.current * this.perPage - this.perPage;
    },
    itemIndexUpperLimit() {
      return this.current * this.perPage - 1;
    },
  },
  methods: {
    onClick: function (link: string) {
      console.log(link);
      openURL(link);
    },
  },
};
</script>

<style scoped></style>
