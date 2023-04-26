<template>
  <!-- <v-responsive
    class="overflow-y-auto"
    max-height="600"
  > -->
  <div class="movie-list">
    <v-card
      class="mx-auto"
      max-width="800"
    >
      <v-toolbar
        color="grey darken-1"
        dark
      >
        <v-toolbar-title>Movie List</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-toolbar>

      <v-container fluid v-if="movies.length">
        <!-- <v-lazy> -->
        <v-row dense>
          <!-- <v-lazy> -->
            <v-col
              v-for="movie in movies"
              :key="movie.id"
              :cols="col_flex"
              md="3"
            >
              <v-lazy
                transition="fade-transition"
              >
                <MovieCard :movie="movie"/>
              </v-lazy>
            </v-col>
          <!-- </v-lazy> -->
        </v-row>
        <!-- </v-lazy> -->
      </v-container>
    </v-card>

  </div>
  <!-- </v-responsive> -->
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'MovieList',
  components: {
    MovieCard,
  },
  props: {
    movies: {
      type: Array,
    }
  },
  data() {
    return {
      col_flex: 3,
    }
  },
}


</script>

<style>

</style>