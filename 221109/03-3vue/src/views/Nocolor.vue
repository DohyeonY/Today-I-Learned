<template>
  <div>
    <h2>시작</h2>
    <div>
      <img src="../assets/1.png" alt="11" style="width:300px; height:300px;">
    </div>
    <h3>해피드</h3>
    <span>
      <button @click="leftClick"><-</button>
      <button @click="rightClick">-></button>
    </span>
  </div>
</template>

<script>
export default {
    name: 'Nocolor',
    methods: {
      leftClick() {
        this.$router.push({name: 'home'})
      },
      rightClick() {
        this.$router.push({name: 'Ssafling'})
      }
    }
}

</script>

<style>

</style>