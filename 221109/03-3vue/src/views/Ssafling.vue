<template>
  <div>
    <h3>1단계</h3>
    <img src="../assets/happling.png" alt="11" style="width:300px; height:300px;">
    <h3>해플링</h3>
    <span>
      <button @click="leftClick"><<</button>
      <button @click="rightClick">>></button>
    </span>
  </div>
</template>

<script>
export default {
    name:'Seafling',
    methods: {
      leftClick() {
        this.$router.push({name: 'Nocolor'})
      },
      rightClick() {
        this.$router.push({name: 'Ssafleaf'})
      }
    }
}
</script>

<style>

</style>