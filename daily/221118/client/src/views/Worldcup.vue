<template>
  <v-container class="worldcup">

    <div v-if="!finishFlag">
      <h1>더 좋아하는 영화를 선택해 주세요</h1>
      <hr>
      <div v-if="!left">
        <v-btn @click="next">{{ roundNum }}강 시작하기</v-btn>
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

    <div v-if="finishFlag">
      <h1>우승!</h1>
      <hr>
      <v-row
        align="center"
        justify="center"
      >
        <v-col cols="6">
          <WorldcupChoice id="winner" :movie="left"/>
        </v-col>
      </v-row>

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
      roundNum: 8,
      left: null,
      right: null,
      finishFlag: false,
    }
  },

  components: {
    WorldcupChoice,
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
        // console.log(this.current_round)
        res.data.movies.forEach(code => {
          axios.get(`http://localhost:8000/api/v1/movie/${code}/`, options)
          .then(res => {
            // console.log(res.data)
            this.current_round.push(res.data)
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
      this.left = this.current_round.pop()
      this.right = this.current_round.pop()
    },
  },

  watch: {
    //라운드 종료 판별
    left: function() {
      if (this.current_round.length === 0 && !this.left) {
        this.current_round = this.next_round
        this.next_round = []
        this.roundNum = this.current_round.length
      }
    },

    //우승자 판별
    right: function() {
      if (this.next_round.length === 0 && this.current_round.length === 1 && !this.left && !this.right) {
        this.left = this.current_round.pop()
        this.finishFlag = true

        //취향점수 반영을 위한 API 호출
        const token = sessionStorage.getItem('jwt')
        const user_id = jwtDecode(token).user_id
        const preferenceURL = 'http://localhost:8000/api/v1/preference/'
        const options = {
          headers: {
            Authorization: 'JWT ' + token
          }
        }
        console.log(this.left)
        const data= {
          value: 8,
          genres: this.left.genres,
          user: user_id
        }
        axios.post(preferenceURL, data, options)
        // .then(res=>{
        //   console.log(res)
        // })

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