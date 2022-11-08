<template>
  <div id="app">
    <SideBar />
    <main>
      <div class="container">
        <router-view/>
        
      </div>
    </main>
  </div>
</template>

<script>
import SideBar from './components/SideBar.vue'

export default {
  components: {
    SideBar
  },
  computed : {
    todoList () {
      return this.$store.state.list
    }
  },

}
</script>


<style>
#app {
  color: #2c3e50;
  height: 100vh;
  display: grid;
  grid-template-columns: 1fr 4fr;
  column-gap: 1rem;
  padding: 3rem;
}

main {
  border-radius: .5rem;
  border: 2px solid #2c3e50;
  padding: 2rem 1.25rem;
}
</style>
