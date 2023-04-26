import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import Profile from '../views/Profile.vue'
import Worldcup from '../views/Worldcup.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/worldcup',
    name: 'worldcup',
    component: Worldcup
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
