import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000/'

export default new Vuex.Store({
  state: {
    articles: [
    ],
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, data) {
      state.articles = data
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}api/v1/articles/`
      })
      .then(response => {
        // console.log(response, context)
        context.commit('GET_ARTICLES', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  modules: {
  }
})
