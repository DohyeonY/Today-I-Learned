<template>
  <v-col class="home">
    <!-- <h1>Movie List</h1> -->
    <MovieList :movies="movies"/>
  </v-col>
</template>

<script>
// @ is an alias to /src
import MovieList from '@/components/MovieList.vue'
// import router from '@/router'
import axios from 'axios'


export default {
  name: 'home',

  data () {
    return {
      bottom: false,
      movies: [],
      page_num: 1
    }
  },

  components: {
    MovieList,
  },

  methods: {
    bottomVisible() {
      const scrollY = window.scrollY
      const visible = document.documentElement.clientHeight
      const pageHeight = document.documentElement.scrollHeight
      const bottomOfPage = visible + scrollY >= pageHeight
      return bottomOfPage || pageHeight<visible
    },

    addMovies() {
      const token = sessionStorage.getItem('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }

      axios.get(`http://localhost:8000/api/v1/movie/list/?page=${this.page_num}`, options)
      .then(res => {
        this.movies = this.movies.concat(res.data.results)
        this.page_num++
      })
      .catch(error => {
        console.log(error.response)
      })
    }, // end of addMovies()

  }, // end of methods

  watch: {
    bottom(bottom) {
      if(bottom) {
        this.addMovies()
      }
    }
  },

  created() {
   window.addEventListener('scroll', () => {
     this.bottom = this.bottomVisible()
   })
   this.addMovies()
   this.page_num++
  }

}
</script>
