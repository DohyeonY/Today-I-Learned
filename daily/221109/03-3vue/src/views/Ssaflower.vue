<template>
  <div>
    <h3>3단계</h3>
    <img src="../assets/happlower.png" alt="11" style="width:300px; height:300px;">
    <h3>해플라워</h3>
    <span>
      <button @click="leftClick"><<</button>
      <button @click="rightClick">>></button>
    </span>
  </div>
</template>

<script>
export default {
    name:'Ssaflower',
    methods: {
      leftClick() {
        window.alert('이전 단계로 돌아갈 수 없습니다.')
      },
      rightClick() {
        window.alert('Home으로 돌아갑니다!')
        this.$router.push({name: 'home'})
      }
    }
}
</script>

<style>

</style>