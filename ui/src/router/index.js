import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Services from '../views/Services.vue'
import Costs from '../views/Costs.vue'
import Stats from '../views/Stats.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  { path: '/servicios', component: Services },
  { path: '/gastos', component: Costs },
  { path: '/estadisticas', component: Stats },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
