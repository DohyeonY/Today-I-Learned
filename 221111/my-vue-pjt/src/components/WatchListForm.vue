<template>
  <div style="border-bottom:0px; padding:20px; ">
    <h1>보고싶은 영화</h1>
    <span>
      <input v-model="addMovie" type="text" style="margin-right:10px">
      <button class="btn btn-outline-dark" @click="add">Add</button>

    </span>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data () {
    return {
      addMovie: null,
    }
  },
  methods: {
    add() {
      this.$store.commit("ADD_MOVIE", this.addMovie) 
      this.addMovie = null
    }
  }
}
</script>

<style>
 .padding{
  padding :0;

 }
</style>