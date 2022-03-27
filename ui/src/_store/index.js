import { createStore } from 'vuex'

import { services } from './_modules';

console.log(services);

// eslint-disable-next-line import/prefer-default-export
const store = createStore({
  modules: {
    services
  },
});

console.log(store);
export default store;
