<template>

    <div>
    <h3>2단계</h3>
    <img src="../assets/happlossome.png" alt="11" style="width:300px; height:300px;">
    <h3>해블라섬</h3>
    <span>
      <button @click="leftClick"><<</button>
      <button @click="rightClick">>></button>
    </span>
  </div>

</template>

<script>
export default {
    name:'Seafleaf',
    methods: {
      leftClick() {
        this.$router.push({name: 'Ssafling'})
      },
      rightClick() {
        this.$router.push({name: 'Ssaflower'})
      }
    }
}
</script>

<style>

</style>