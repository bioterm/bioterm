<template>
  <q-layout view="hHh LpR fFf">
    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          <q-avatar square>
            <img src="~assets/bioterm_icon.svg" />
          </q-avatar>
          bioterm
        </q-toolbar-title>

        <q-btn-dropdown class="glossy" color="purple" label="Account">
          <div class="row no-wrap q-pa-md">
            <div class="column">
              <div class="text-h6 q-mb-md">Settings</div>
              <q-toggle v-model="localStore.darkMode" label="Use Dark Mode" />
              <q-toggle
                v-if="userStore.isAdmin"
                v-model="userStore.adminView"
                label="Use Admin View"
              />
            </div>

            <q-separator vertical inset class="q-mx-lg" />

            <div class="column items-center">
              <q-avatar size="72px">
                <img :src="userStore.gravatarURI" />
              </q-avatar>

              <div class="text-subtitle1 q-mt-md q-mb-xs">
                {{ userStore.userName }}
              </div>

              <q-btn
                color="primary"
                label="Logout"
                push
                size="sm"
                v-close-popup
                @click="logout"
              />
            </div>
          </div>
          <q-tooltip>Account</q-tooltip>
        </q-btn-dropdown>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered>
      <q-scroll-area class="fit">
        <q-list>
          <template v-for="(menuItem, index) in menuList" :key="index">
            <div
              v-if="
                !menuItem.adminOnly ||
                (menuItem.adminOnly && userStore.isAdmin && userStore.adminView)
              "
            >
              <q-item
                clickable
                :active="menuItem.label === 'Home'"
                v-ripple
                :to="menuItem.to"
              >
                <q-item-section avatar>
                  <q-icon :name="menuItem.icon" />
                </q-item-section>
                <q-item-section>
                  {{ menuItem.label }}
                </q-item-section>
              </q-item>
              <q-separator :key="'sep' + index" v-if="menuItem.separator" />
            </div>
          </template>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <div class="row justify-center items-center q-pa-md q-gutter-sm">
        <q-banner
          rounded
          class="bg-orange text-white text-center"
          style="max-width: 400px"
        >
          <q-icon name="warning" left /><span
            >Alpha-Release. Data integrity not guaranteed.</span
          ><q-icon name="warning" right />
        </q-banner>
      </div>
      <router-view />
    </q-page-container>

    <q-footer reveal elevated class="bg-dark text-white" q-pa-md>
      <q-toolbar>
        <q-btn-dropdown color="accent" dropdown-icon="change_history">
          <template v-slot:label>
            <div
              style="
                display: flex;
                flex-direction: column;
                align-items: start;
                overflow: hidden;
              "
            >
              <span style="font-size: 0.6rem; white-space: nowrap"
                >Selected setup</span
              >
              <span style="white-space: nowrap">{{
                localStore.selectedController?.display_name ||
                localStore.selectedController?.uuid ||
                'Select Setup'
              }}</span>
            </div>
          </template>
          <template
            v-for="(item, index) in localStore.controllers"
            :key="item.id"
          >
            <q-item
              clickable
              v-close-popup
              @click="handleControllerSelection(item)"
            >
              <q-item-section>
                {{ item.display_name || item.uuid }}
              </q-item-section>
            </q-item>
            <q-separator
              v-if="index !== localStore.controllers.length - 1"
            ></q-separator>
          </template>
        </q-btn-dropdown>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script lang="ts">
import { onMounted, ref, watch } from 'vue';
import { useUserStore, initializeUserStore } from 'src/stores/user';
import auth from 'src/services/AuthService';
import { useLocalStore } from 'src/stores/localStore';
import { useQuasar } from 'quasar';
import { Controller } from 'src/types/types';

export default {
  setup() {
    const leftDrawerOpen = ref(false);
    const userStore = useUserStore();
    const localStore = useLocalStore();

    const $q = useQuasar();
    // $q.addressbarColor.set();
    ($q.addressbarColor.set as (color?: string) => void)();

    $q.dark.set(localStore.darkMode);
    watch(
      () => localStore.darkMode,
      (darkMode) => $q.dark.set(darkMode),
    );

    async function handleControllerSelection(controller: Controller) {
      localStore.setSelectedController(controller);
      localStore.updateDevices();
      localStore.updateDashboard();
    }

    onMounted(async () => {
      await localStore.updateControllers();
      if (localStore.selectedController) {
        await localStore.updateDashboard();
        await localStore.updateDevices();
      }
    });

    const menuList = [
      {
        icon: 'home',
        label: 'Home',
        to: '/home',
        separator: true,
      },
      // {
      //   icon: 'class',
      //   label: 'Setups',
      //   separator: false,
      // },
      {
        icon: 'devices',
        label: 'Devices',
        to: '/devices',
        separator: false,
      },
      {
        icon: 'analytics',
        label: 'Data',
        to: '/data',
        separator: true,
      },
      {
        icon: 'rule',
        label: 'Rules',
        to: '/rules',
        separator: true,
      },
      // {
      //   icon: 'assignment',
      //   label: 'Experiments',
      //   to: '/experiments',
      //   separator: false,
      // },
      // {
      //   icon: 'precision_manufacturing',
      //   label: 'Protocols',
      //   to: '/protocols',
      //   separator: true,
      // },
      {
        icon: 'help',
        iconColor: 'primary',
        label: 'Help',
        to: '/help',
        separator: true,
      },
      {
        icon: 'admin_panel_settings',
        label: 'Administration',
        to: '/admin',
        adminOnly: true,
        separator: false,
      },
    ];

    return {
      leftDrawerOpen,
      handleControllerSelection,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
      userStore,
      localStore,
      menuList,
    };
  },
  methods: {
    logout() {
      auth.logout();
      console.log('logged out');
    },
  },
  async mounted() {
    initializeUserStore();
    // store.fetchExperiments();
  },
};
</script>
