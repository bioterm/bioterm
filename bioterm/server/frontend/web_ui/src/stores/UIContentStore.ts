import { defineStore } from 'pinia';
// import axios from 'axios'

export const useUIContentStore = defineStore('UIContentStore', {

  state: () => {

    return {

      experiments: [],

    };
  },
  getters: {
    getExperiments(state){
        return state.experiments
      }
  },

  actions: {
    // async fetchExperiments() {
    //     try {
    //       const data = await axios.get(`https://${process.env.ELN_DOMAIN}/api/v2/experiments', {headers: {'Authorization': `${process.env.elnToken}`}})
    //         this.experiments = data.data
    //       }
    //       catch (error) {
    //         alert(error)
    //         console.log(error)
    //     }
    //   }


  }






});
