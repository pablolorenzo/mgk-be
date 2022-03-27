import { ServicesService } from '../../_services';
ServicesService.getServices();
const state = {
  services: [],
};

const getters = {};

const actions = {
  getServices({commit}){
    return ServicesService.getServices()
      .then((services) => {
        console.log(services)
        commit('setServices', services);
      });

  }

};

const mutations = {
  setServices(state, services) {
    state.services = services;
  },
};

export const services = {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};

