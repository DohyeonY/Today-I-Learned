<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>소득세 계산기</h1>
    <Income/>
    <Finaltax/>

  </div>
</template>

<script>

import Income from '@/components/Income'

export default {
  name: 'App',
  components: {
    Income,
    // Finaltax,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
