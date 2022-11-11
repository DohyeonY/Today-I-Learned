<template>
  <div>
    <div class="col">
      <div class="card h-100">
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
  name:'MovieCard',
  props: {
    movie: Object,
  },
  computed: {
    movieUrl () {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    }
  }
}
</script>

<style>

</style>