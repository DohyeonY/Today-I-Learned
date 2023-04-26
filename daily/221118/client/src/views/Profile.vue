<template>
  <div class="mx-auto" id="profile">
    
    <v-container>
      <h2>{{ username }}'s</h2>
      <v-row
        justify="center"
      >
        <v-col cols="3">
          <h3>Movie List</h3>
          <Timeline :my_movies="my_movies"/>
        </v-col>
        <v-col cols="8">
          <h3>Review List</h3>
          <ReviewList :my_reviews="my_reviews"/>
          <br>
          <RecommandList :movies="reccomands"/>
        </v-col>
      </v-row>
    </v-container>
    
    
  </div>
</template>

<script>
import Timeline from '../components/Timeline'
import ReviewList from '../components/ReviewList'
import RecommandList from '../components/RecommandList'
import jwtDecode from 'jwt-decode'
import { mapGetters } from 'vuex';
import router from '../router';
import axios from 'axios'

const HOST = process.env.VUE_APP_SERVER_HOST;

export default {
  name: "profile",
  
  data () {
    return {
      username: null,
      my_reviews: [],
      my_movies: [],
      reviews_info: [],
      reccomands: [],
    }
  },

  components: {
    Timeline,
    ReviewList,
    RecommandList,
  },

  methods: {
    getInfo() {
      this.username = sessionStorage.getItem('username')
      const token = sessionStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const options = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      axios.get(HOST+'/api/v1/my_movies/', options)
      .then(res => {
        this.reviews_info = res.data.review_set
        this.reviews_info.forEach(review => {
          axios.get(`http://localhost:8000/api/v1/movie/${review.movie}/`, options)
          .then(result => {
            this.my_movies.push(result.data)
            const new_info = {
              movie: result.data.title,
              score: review.score,
              content: review.content
            }
            this.my_reviews.push(new_info)
          })
        })
      })
      .catch(err => console.log(err))

      axios.get(`http://localhost:8000/api/v1/preference/${user_id}/`, options)
      .then(res => {
        this.reccomands = res.data
      })
    }
  }, 

  computed: {
    ...mapGetters(['isLoggedIn']),
  },

  created () {
    if (this.isLoggedIn) {
      this.getInfo()
    } else{
      router.push('/login')
    }
  }
};
</script>

<style>
</style>