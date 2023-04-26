<template>
  <div class="nopadding">
    <ul 
    style="border:none;"
    class="list-group-item nopadding" 
    v-for="(movie, index) in addMovie" 
    :key="index">
      <li 
      style="padding-top:5px; padding-bottom:5px;"
      @click="line(movie)"
      :class="{ 'changebg': movie.isClicked, 'click': movie.isClicked, 'newbg': !movie.isClicked, 'text-muted':!movie.isClicked}"
      ><h4>{{ movie.content }}</h4></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  computed : {
    addMovie() {
      return this.$store.state.addMovie
    }
  },
  methods : {
    line(movie) {
      movie.isClicked = !movie.isClicked
    }
  }
}
</script>

<style>
  .click{
    text-decoration: line-through;

  }
  .changebg{
    background-color: #DCDCDC;
    color:rgba(130,130,130, 0.5);
  }
  .newbg{
    background-color:#EEEEEE;  
  }
  li{
    list-style: none;
  }
   .nopadding{
  padding :0 !important;

 }
</style>