<template>
  <div id="app">
    <nav>
      <Head/>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { mapActions } from "vuex"
import Head from '@/components/Head'

export default {
  name: "App",
  components: {
    Head
  },
  data () {
    return {
      moviesList : [],
    }
  },
  computed : {
    
  },
  methods: {

    ...mapActions(['getMoviesList']),
  //   getMoviesList () {
  //     this.$store.dispatch('getMoviesList')

  },
  created () {
    this.getMoviesList()
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  margin-bottom: 5rem;
  padding: 30px;
}

a {
  font-weight: bold;
  color: #2c3e50;
}

</style>
