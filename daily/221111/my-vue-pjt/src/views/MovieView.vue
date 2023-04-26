<template>
  <div class="movieList">
    <Main/>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <MovieCard 
      v-for="movie in getMoviesList" 
      :key="movie.id"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import Main from '@/components/Main'

export default {
  name: "MovieView",
  data () {
    return {
      moviesList : [],
    }
  },
  components: {
    MovieCard,
    Main,
  },
  computed : {
    getMoviesList() {
      console.log(this.$store.state.moviesList)
      return this.$store.state.moviesList
    }
  },
}
</script>

<style>

</style>