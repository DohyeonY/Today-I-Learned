import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Nocolor from '@/views/Nocolor'
import Ssafleaf from '@/views/Ssafleaf'
import Ssafling from '@/views/Ssafling'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/Nocolor',
    name: 'Nocolor',
    component: Nocolor
  },
  {
    path: '/Ssafleaf',
    name: 'Ssafleaf',
    component: Ssafleaf
  },
  
  {
    path: '/Ssafling',
    name: 'Ssafling',
    component: Ssafling
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
