<template>
  <v-container class="worldcup">

    <div v-if="!finishFlag">
      <h1>취향에 맞는 영화를 추천해 드리기 위해 </h1> 
      <h1>영화 이상형 월드컵을 진행해 주세요!</h1>
      <hr>
      <br>
      <div v-if="!left">
        <v-btn v-if="roundNum < 3" @click="next">결승 시작하기</v-btn>
        <v-btn v-else @click="next">{{ roundNum }}강 시작하기</v-btn>
      </div>
      <v-row
        align="center"
        justify="center"
      >
        <v-col cols="6" align="center">
          <WorldcupChoice id="left" :movie="left" @choiceEvent="leftChoice" />
        </v-col>
        <v-col cols="6" align="center">
          <WorldcupChoice id="right" :movie="right" @choiceEvent="rightChoice" />
        </v-col>
      </v-row>
    </div>

    <div style="text-align: center;" v-if="finishFlag">
      <h1>우승!</h1>
      <br>
      <div style="display: inline-block;">
        <v-btn style=" margin: 20px;" @click="toHome">무비 리스트</v-btn>
        <v-btn style=" margin: 20px;" @click="toProfile">프로필</v-btn>
      </div>
      <br>
      <hr>
      <v-row
        align="center"
        justify="center"
      >
        <v-col cols="6">
          <WorldcupChoice id="winner" :movie="left"/>
        </v-col>
      </v-row>
      <br>
      <div v-for="movie in getRecommendedMovies" :key="movie.id">
        <!-- {{ movie }} -->
        <div class="col">
          <div class="card h-100">
            <img :src= "`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="poster" style="height:80%">
            <div class="card-body">
              <h5 class="card-title text-center fw-bold"> 제목 : {{ movie.title }}</h5>
              <p class="card-text">⭐ 평점 : {{ movie.vote_average }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </v-container>
</template>

<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'
import WorldcupChoice from '@/components/WorldcupChoice.vue'

export default {
  data () {
    return {
      current_round: [],
      next_round: [],
      roundNum: 16,
      left: null,
      right: null,
      finishFlag: false,
      lastTwoGenre: [],
    }
  },

  components: {
    WorldcupChoice,
  },
  computed : {
    getRecommendedMovies () {
      console.log(this.$store.state.recommendedMovies)
      return this.$store.state.recommendedMovies
    },
  },
  
  methods: {
    randomMovieCall() {
      const token = sessionStorage.getItem('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.get('http://localhost:8000/api/v1/worldcup/', options)
      .then(res => {
        // console.log(res)
        res.data.movies.forEach(code => {
          axios.get(`http://localhost:8000/api/v1/movie/${code}/`, options)
          .then(res => {
            // console.log(res.data)
            this.current_round.push(res.data)
          })
          // 첫 리스트 랜덤하게 셔플
          .then(() => {
            let count = this.current_round.length
            for (let i = 0; i < this.current_round.length ; i++) {
            const j = Math.floor(Math.random() * count)
            const k = Math.floor(Math.random() * count)
            const temp = this.current_round[j]
            this.current_round[j] = this.current_round[k]
            this.current_round[k] = temp
            // console.log(this.current_round)
        }
          })
        })
      })
    },

    leftChoice() {
      this.next_round.push(this.left)
      this.left = null
      this.right = null
      this.next()
    },

    rightChoice() {
      this.next_round.push(this.right)
      this.left = null
      this.right = null
      this.next()
    },

    next() {
      // console.log(this.current_round)
      this.left = this.current_round.pop()
      this.right = this.current_round.pop()
      // console.log(this.left)
      // console.log(this.current_round)
      // console.log(__.suffle(this.current_round))
      // console.log(this.right)

    },
    toHome() {
      this.$router.push({ name: 'home'})
    },
    toProfile() {
      this.$router.push({ name: 'profile'})
    },
    
  },

  watch: {
    //라운드 종료 판별
    left: function() {
      if (this.current_round.length === 0 && !this.left) {
        // 첫 라운드 이후 매 라운드마다 랜덤하게 셔플
        let count = this.next_round.length
        for (let i = 0; i < this.next_round.length ; i++) {
          
          const j = Math.floor(Math.random() * count)
          const k = Math.floor(Math.random() * count)
          const temp = this.next_round[j]
          this.next_round[j] = this.next_round[k]
          this.next_round[k] = temp
        }
        // console.log(this.next_round)
        this.current_round = this.next_round
        this.next_round = []
        this.roundNum = this.current_round.length
        if (this.current_round.length === 2) {
          this.current_round.forEach(ele => {
            // console.log(ele)
            this.$store.dispatch('recommendedMovies', ele.tmdb)
            // console.log(this.$store.state.recommendedMovies)
             //취향점수 반영을 위한 API 호출
            const token = sessionStorage.getItem('jwt')
            const user_id = jwtDecode(token).user_id
            const options = {
              headers: {
                Authorization: 'JWT ' + token
              }
            }
            // console.log(this.left)
            const data= {
              value: 8,
              genres: ele.genres,
              user: user_id
            }
            // console.log(data)
            axios.post('http://localhost:8000/api/v1/preference/', data, options)
            // .then(res=>{
            //   console.log(res)
            //   // this.$router.push({name : 'home'})
            // })
            // this.lastTwoGenre.value.push(ele.genres)
          })
        // console.log(this.lastTwoGenre)
        }
      }
    },

    //우승자 판별
    right: function() {
      if (this.next_round.length === 0 && this.current_round.length === 1 && !this.left && !this.right) {
        this.left = this.current_round.pop()
        // this.right = this.current_round.pop()
        // this.left.push(this.right)
        // console.log(this.left)
        // console.log(this.right)
        // console.log(this.)
        this.finishFlag = true
      }
    }
  },


  created() {
    this.randomMovieCall()
  },
}
</script>

<style>

</style>