<template>
  <div>
    <button class="btn btn-primary" style="width:300px" @click="randomMovie" >PICK</button>
    <div class="randomBox">

      <div v-if="movie" class="card h-100">
          <img :src= "movieUrl" alt="" style="height:80%">
          <div class="card-body">
            <h5 class="card-title text-center fw-bold"> 제목 : {{ movie.title }}</h5>
            <p class="card-text">⭐ 평점 : {{ movie.vote_average }}</p>
          </div>
      </div>

    </div>
  </div>

</template>

<script>
export default {
  name: "RandomView",
  data() {
    return {
      movie: null,
    }
  },
  methods: {
    randomMovie() {
      this.movie = this.moviesList[Math.floor(Math.random() * this.moviesList.length)]
    },
  },
  computed: {
    movieUrl () {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    },
    moviesList() {
      return this.$store.state.moviesList
    }
  },
  created () {
    this.randomMovie()
  }
}
</script>

<style>
  .randomBox {
    margin: 30px auto;
    text-align: center;
    width: 300px;
  }
</style>