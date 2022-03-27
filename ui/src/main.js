import { createApp } from 'vue'


import App from './App.vue'
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import router from './router'
import store from './_store'
console.log("-----------------------")
console.log (store);
   
const app = createApp(App)
app.config.compilerOptions.delimiters = ['${', '}']  
app.use(router)
  .use(store)
  .use(Quasar, quasarUserOptions)
  .mount('#app')
