import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    moviesList : [],
    addMovie: [],
  },
  getters: {
    // randomMovie (state) {
    //   return state.moviesList[Math.floor(Math.random() * state.moviesList.length)]
    // }
  },
  
  mutations: {
    GET_MOVIES_LIST (state, data) {
      // console.log(data)
      state.moviesList = data
    },
    ADD_MOVIE(state, data) {
      // console.log(data)
      const movie = {
        content : data,
        isClicked : false,
      }
      state.addMovie.push(movie)
    }
},
  actions: {
    getMoviesList(context) {
      axios({
        method: 'get',
        url: "https://api.themoviedb.org/3/movie/top_rated?api_key=b38eab9e566911474038dee3caf82c37&language=ko-KR&page=1",
      })
      .then(response =>{
        context.commit('GET_MOVIES_LIST', response.data.results)
        // console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
    },
    getWeatherList(context) {
      axios({
        method: 'get',
        url: "https://api.themoviedb.org/3/movie/top_rated?api_key=b38eab9e566911474038dee3caf82c37&language=ko-KR&page=1",
      })
      .then(response =>{
        context.commit('GET_MOVIES_LIST', response.data.results)
        // console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
    },
    },
  
  modules: {
  }
})
