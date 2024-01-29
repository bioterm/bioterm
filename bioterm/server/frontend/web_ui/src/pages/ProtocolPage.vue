<template>
  <q-page
    padding
    class="full-width column no-wrap justify-start items-stretch content-start q-gutter-y-md"
  >
    <div class="row" padding>
      <h1>Protocols</h1>
    </div>
    <div class="q-pa-md">
      <div class="q-gutter-y-md">
        <q-tabs v-model="tab" class="text-teal" indicator-color="accent">
          <q-tab name="saved" icon="fa-solid fa-database" label="Saved" />
          <q-tab name="editor" icon="edit_square" label="Editor" />
          <q-tab name="upload" icon="upload_file" label="Upload" />
        </q-tabs>
      </div>
    </div>
    <q-separator color="purple" inset />
    <q-tab-panels
      v-model="tab"
      animated
      vertical
      transition-prev="jump-left"
      transition-next="jump-right"
    >
      <q-tab-panel name="saved">
        <p>
          This will become a list-like view similar to the experiments page.
        </p>
      </q-tab-panel>

      <q-tab-panel name="editor">
        <div class="row">
          <div class="col-2">
            <div class="form-group">
              <div
                class="btn-group-vertical buttons"
                role="group"
                aria-label="Basic example"
              >
                <button class="btn btn-secondary" @click="add">Add</button>
                <button class="btn btn-secondary" @click="clear">Clear</button>
              </div>

              <div class="form-check">
                <input
                  id="disabled"
                  type="checkbox"
                  v-model="enabled"
                  class="form-check-input"
                />
                <label class="form-check-label" for="disabled"
                  >DnD enabled</label
                >
              </div>
            </div>
          </div>

          <div class="col-6">
            <h3>Draggable {{ draggingInfo }}</h3>

            <draggable
              :list="list"
              :disabled="!enabled"
              item-key="name"
              class="list-group"
              ghost-class="ghost"
              :move="checkMove"
              @start="dragging = true"
              @end="dragging = false"
            >
              <template #item="{ element }">
                <div
                  class="list-group-item"
                  :class="{ 'not-draggable': !enabled }"
                >
                  {{ element.name }}
                </div>
              </template>
            </draggable>
          </div>
        </div>
      </q-tab-panel>

      <q-tab-panel name="upload">
        <p>This is were the uploader for local edited files will be.</p>
      </q-tab-panel>
    </q-tab-panels>
  </q-page>
</template>

<script>
import { ref } from 'vue';
import draggable from 'vuedraggable';

let id = 1;
export default {
  name: 'ProtocolPage',

  order: 0,
  components: {
    draggable,
  },
  setup() {
    return {
      tab: ref('saved'),
    };
  },
  data() {
    return {
      enabled: true,
      list: [
        { name: 'John', id: 0 },
        { name: 'Joao', id: 1 },
        { name: 'Jean', id: 2 },
      ],
      dragging: false,
    };
  },
  computed: {
    draggingInfo() {
      return this.dragging ? 'under drag' : '';
    },
  },
  methods: {
    add: function () {
      this.list.push({ name: 'Juan ' + id, id: id++ });
    },
    clear: function () {
      // this.list = [];
      if (confirm('Do you really want to clear everything?')) {
        this.list = [];
      }
    },
    checkMove: function (e) {
      window.console.log('Future index: ' + e.draggedContext.futureIndex);
    },
  },
};
</script>
<style scoped>
.buttons {
  margin-top: 35px;
}

.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}

.not-draggable {
  cursor: no-drop;
}
</style>
