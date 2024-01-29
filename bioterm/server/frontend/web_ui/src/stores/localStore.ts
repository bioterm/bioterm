import { defineStore } from 'pinia';
import { Controller, Dashboard, Device } from 'src/types/types';
import { RuleModel } from 'src/types/rules';
import apiservice from 'src/services/ApiService';

export const useLocalStore = defineStore('localStore', {
  state: () => ({
    darkMode: false,
    selectedController: null as Controller | null,
    controllers: [] as Controller[],
    devices: [] as Device[],
    dashboard: null as Dashboard | null,
    rules: [] as RuleModel[],
  }),
  getters: {},
  actions: {
    setControllers(controllers: Controller[]) {
      this.controllers = controllers;
    },
    setSelectedController(controller: Controller) {
      this.selectedController = controller;
    },
    clearSelectedController() {
      this.selectedController = null;
    },
    setDevices(devices: Device[]) {
      this.devices = devices;
    },
    setDashboard(dashboard: Dashboard) {
      this.dashboard = dashboard;
    },
    async updateRules() {
      if (this.selectedController) {
        this.rules = await apiservice.getRules(this.selectedController.uuid);
      }
    },
    async updateDashboard() {
      if (this.selectedController) {
        this.dashboard = await apiservice.getDashboard(
          this.selectedController.uuid,
        );
      }
    },
    async updateControllers() {
      this.controllers = await apiservice.getControllers();
    },
    async updateDevices() {
      if (this.selectedController) {
        this.devices = await apiservice.getDevices(
          this.selectedController.uuid,
        );
      }
    },
  },
  persist: true,
});
