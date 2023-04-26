import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store',
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    doubleLength(state, getters) {
      return getters.messageLength * 2
    }
  },
  mutations: {
    CHANG_MESSAGE(state, newMessage) {
      // console.log(state)
      // console.log(newMessage)
      state.message = newMessage
    }
  },
  actions: {
    chageMessage(context, newMessage) {
      // console.log(context)
      // console.log(newMessage)
      context.commit('CHANG_MESSAGE', newMessage)
    }
  },
  modules: {
  }
})
