import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    count: 0,
  },
  getters: {
    countDouble(state) {
      return state.count * 2
    },

  },
  mutations: {
    INCREASE(state) {
      console.log(111)
      state.count ++
    },

    DECREASE(state) {
      state.count --
    },


  },
  actions: {

    
  },
  modules: {
  }
})
