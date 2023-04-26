import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import RandomView from '@/views/RandomView'
import WatchListView from '@/views/WatchListView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView,
  },
  {
    path: '/random',
    name: 'RandomView',
    component: RandomView,
  },
  {
    path: '/watch',
    name: 'WatchListView',
    component: WatchListView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
