import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import auth from './modules/auth'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)
const SERVER_URL = 'http://127.0.0.1:8000/'

const store = new Vuex.Store({
  
  plugins: [
    createPersistedState()
  ],

  state: {
    // accounts
    isLogin: false,

  },

  getters: {

  },

  mutations: {
    // ACCOUNTS MUTATIONS
    LOGIN(state) {
      state.isLogin = true
    },
    LOGOUT(state) {
      state.isLogin = false
    },

  },

  actions: {
    // ACCOUNTS ACTIONS
    login({commit}, credentials) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}accounts/api-token-auth/`,
        data: credentials,
      })
      .then(res => {
        localStorage.setItem('jwt', res.data.token)
        commit('LOGIN')
        router.push({name: 'Home'})
      })
      .catch(err => console.log(err))
    },
    checkLogin({commit}, token) {
      if (token) {
        commit('LOGIN')
      }
    },
    logout({commit}) {
      localStorage.removeItem('jwt')
      commit('LOGOUT')
      router.push({ name: 'Login' })
    },

  },

  modules: {
    auth,
  }
})

export default store;