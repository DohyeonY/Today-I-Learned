<template>
    <div class="home">
      <img alt="Vue logo" src="../assets/logo.png">
      <br>
      <h1>점심메뉴</h1>
        <button @click="createLunch">Pick Lunch</button>
        <p>{{ selected }}</p>
        <br>

    </div>
  </template>
  
  <script>
  // @ is an alias to /src

  
  export default {
    name: 'LunchView',
    data () {
        return {
            allLunch : ['짬뽕', '짜장', '볶음밥', '김치찌개', '국밥'],
            selected : ''
        }
    },
    components: {
      
    },
    methods : {
        createLunch() {

            const lunchs = []
            for (let i = 0; i <= 4; i++) {
                lunchs.push(i)
            }
            console.log(lunchs)
            let num = Math.floor(Math.random() * lunchs.length)
            console.log(num)
            this.selected = this.allLunch[num]

        }
    }
  }
  </script>
  