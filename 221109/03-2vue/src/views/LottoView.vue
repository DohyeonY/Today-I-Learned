<template>
    <div class="home">
      <img alt="Vue logo" src="../assets/logo.png">
      <br>
      <h1>로또</h1>
        <button @click="createLotto">Get Lucky Numbers</button>
        <p>{{ lottoNum }}</p>
        <br>

    </div>
  </template>
  
  <script>
  // @ is an alias to /src

  
  export default {
    name: 'LottoView',
    data() {
        return {
            lottoNum : [],
        }
    },
    components: {
      
    },
    methods : {
        createLotto() {
            let mixedNum = []
            const candidates = []
            for (let i = 1; i <= 45; i++) {
                candidates.push(i)
            }
            while (candidates.length > 0) {
                let num = Math.floor(Math.random() * candidates.length)
                let leftNum = candidates.splice(num, 1)[0]
                mixedNum.push(leftNum)
            }
            this.lottoNum = mixedNum.slice(0, 6).sort((prev, curr) => prev - curr)
        }
    }
  }
  </script>
  