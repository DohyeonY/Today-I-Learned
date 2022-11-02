<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <div>
      <button>Home</button>
      <button>Start</button>


    </div>


    <!-- 3. 보여주기 -->

    <!-- <MyComponent/> -->
    <!-- <h3><HelloWorld msg="Welcome to Your Vue.js App"/></h3> -->

    <!-- <h3>SSAFY 여러분을 응원합니다!</h3> -->
  </div>
</template>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
// import HelloWorld from './components/HelloWorld.vue'
// 1. 불러오기
// import MyComponent from './components/MyComponet.vue'
import MyComponent from '@/components/MyComponent'
// import MyComponet from './components/MyComponet.vue'
export default {
  name: 'App',
  components: {
    // HelloWorld,
    // 2. 등록하기
    MyComponent,
  }
}
const app = new Vue({
  el: '#app',
  data: {
    pageNum : 1,
    isStarted : false,
  },
})
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
