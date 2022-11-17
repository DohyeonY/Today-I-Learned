import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const store = new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  // state: {
  // },
  // mutations: {
  // },
  // actions: {
  // },
  modules: {
    auth,
  }
})

export default store;