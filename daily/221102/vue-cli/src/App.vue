<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <div>
      <button @click="clickHome">Home</button>
      <button @click="clickStart">Start</button>

    </div>

    <div v-if="!isStarted && pageData==1"><Home/></div>

    <container v-else-if="isStarted && pageData==1">
      <button @click="clickLeft">왼쪽</button>
      <Nocolor/>
      <button @click="clickRight">오른쪽</button>
      </container>

    <container v-else-if="pageData==2">
      <button @click="clickLeft">왼쪽</button>
      <Ssafling/>
      <button @click="clickRight">오른쪽</button>
      </container>

    <container v-else-if="pageData==3">
      <button @click="clickLeft">왼쪽</button>
      <Ssafleaf/>
      <button @click="clickRight">오른쪽</button>
      </container>

    <container v-else-if="pageData==4">
      <button @click="clickLeft">왼쪽</button>
      <Ssaflower/>
      <button @click="clickRight">오른쪽</button>
      </container>

  </div>
</template>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
import Home from '@/components/Home'
import Nocolor from '@/components/Nocolor'
import Ssafleaf from '@/components/Ssafleaf'
import Ssafling from '@/components/Ssafling'
import Ssaflower from '@/components/Ssaflower'
export default {
  name: 'App',
  components: {
    Home,
    Ssaflower,
    Ssafling,
    Ssafleaf,
    Nocolor,
  },
  data: function () {
      return {
        pageData : 1,
        isStarted : false,

      }
  },
  methods: {
    clickHome : function() {
      this.isStarted = false
      this.pageData = 1
    },
    clickStart : function() {
      this.isStarted = true

    },
    clickLeft : function() {
      if (this.pageData == 1) {
        this.isStarted = false
      } else {
        this.pageData -= 1
      }
    },
    clickRight : function() {
      if (this.pageData == 4) {
        window.alert('Home으로 돌아갑니다!')
        this.pageData = 1
        this.isStarted = false
      } else {
        this.pageData += 1
      }
    }
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
