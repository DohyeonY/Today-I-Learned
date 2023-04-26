import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Nocolor from '@/views/Nocolor'
import Ssafleaf from '@/views/Ssafleaf'
import Ssafling from '@/views/Ssafling'
import Ssaflower from '@/views/Ssaflower'
import NotFound404 from '@/views/NotFound404'

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
  {
    path: '/Ssaflower',
    name: 'Ssaflower',
    component: Ssaflower
  },

  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },

  {
    path: '*',
    redirect: '/404'
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
