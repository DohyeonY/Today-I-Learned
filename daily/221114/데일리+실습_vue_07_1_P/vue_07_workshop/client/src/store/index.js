import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000/'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    articles: [
    ],
    token : null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, data) {
      state.articles = data
    },
    SAVE_TOKKEN1(state, token) {
      state.token = token
      router.push({name: 'TodoList'})
    },
    SAVE_TOKKEN2(state, token) {
      
      state.token = token
      router.push({name: 'Login'})
    },
    DELETE_TOKKEN(state) {
      state.token = null
      alert('로그아웃 되었습니다.')
      router.push({ name: 'Login'})
    }

  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}todos/`,
        headers : {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then(response => {
        // console.log(response, context)
        context.commit('GET_ARTICLES', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}accounts/signup/`,
        data: {
          username: payload.username,
          password1 : payload.password1,
          password2 : payload.password2,
        }
      })
      .then(response => {
        console.log(response, context)
        context.commit('SAVE_TOKKEN2', response.data.key)
      })
      .catch(error => {
        console.log(error)
      })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,

        }
      })
      .then(response => {
        console.log(response)
        context.commit('SAVE_TOKKEN1', response.data.key)
      })
    } 
  },
  modules: {
  }
})
