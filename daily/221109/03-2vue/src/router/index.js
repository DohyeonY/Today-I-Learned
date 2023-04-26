import Vue from 'vue'
import VueRouter from 'vue-router'
import LunchView from '../views/LunchView.vue'
import LottoView from '../views/LottoView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'lunch',
    component: LunchView
  },
  {
    path: '/lotto',
    name: 'lotto',
    component: LottoView
  },
  // {
  //   path: '/lotto',
  //   name: 'Lotto',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/LottiView.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
