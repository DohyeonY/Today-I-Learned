<template>

  <v-card class="movie-detail-modal" tile>
    <v-card-title>
      <span class="headline">{{ movie.title }}</span>
      <span v-if="movie.title_en">({{ movie.title_en }})</span>
    </v-card-title>

    
    <v-container fluid>

      <v-divider></v-divider>
      <v-row justify="space-around">
        <v-col cols="5">
          <v-img
            :src="movie.img_url"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
          >
          </v-img>
        </v-col>
      </v-row>

      <v-divider></v-divider>

      <v-card-text>
        <div><b>감독</b> | <span v-for="name in directors" :key=name>{{ name }}, </span></div>
        <div><b>배우</b> | <span v-for="name in actors" :key=name>{{ name }}, </span></div>
        <div><b>평점</b> | <span>{{ movie.rate }}</span></div>
      </v-card-text>

      <v-divider></v-divider>

      <v-expansion-panels accordion>
        <v-expansion-panel accordion>
          <v-expansion-panel-header>줄거리</v-expansion-panel-header>
          <v-expansion-panel-content>
            {{ movie.description }}
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
      
      <v-card-text>
        <div><b>평가</b></div>
        <ul style="list-style: none;">
          <li v-for="review in reviews" :key=review.id>
            <v-row>
              <v-rating
                :value="review.score"
                background-color="white"
                color="yellow accent-4"
                dense
                size="8"
                readonly
              ></v-rating>
              <div>
                | {{ review.content }}
                <i style="font-size:12px;"> by {{ review.username }}</i>
              </div>
              <div v-if="user_pk==review.user" >
                <v-btn small v-on:click="reviewDelete($event, review)">
                  삭제
                </v-btn>
              </div>

             </v-row>
          </li>
        </ul>

      </v-card-text>

    </v-container>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="white darken-1" text @click.prevent="closeDialog">닫기</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  data () {
    return {
      directors: [],
      actors: [],
      target_review: null,
      user_pk: ''
    }
  },

  props: {
    movie: {
      type: Object,
      required: false,
    },
    reviews: {
      type: Array,
      required: false,
    }
  },

  methods: {
    closeDialog() {
      this.$emit('closeDialogEvent', true)
    },

    getUserPk(){
      const token = sessionStorage.getItem('jwt')
      this.user_pk = jwtDecode(token).user_id
    },

    directorsNameCall() {
      const token = sessionStorage.getItem('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      this.movie.directors.forEach(code => {
        axios.get(`http://localhost:8000/api/v1/director/${code}/`, options)
        .then(res => {
          this.directors.push(res.data.name)
        })
        .catch(error => {
          console.log(error.response)
        })
      })
    },

    actorsNameCall() {
      const token = sessionStorage.getItem('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      this.movie.actors.forEach(code => {
        axios.get(`http://localhost:8000/api/v1/actor/${code}/`, options)
        .then(res => {
          this.actors.push(res.data.name)
        })
        .catch(error => {
          console.log(error.response)
        })
      })
    },

    reviewDelete(event, review) {
      const token = sessionStorage.getItem('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.get(`http://localhost:8000/api/v1/review/delete/${review.id}/`, options)
      .then(() => {
        this.$emit('reviewUpdateEvent', true)
      })
    },

  }, //end of methods

  mounted() {
    this.directorsNameCall()
    this.actorsNameCall()
    this.getUserPk()
    // this.reviewsCall()
  },

}
</script>

<style>

</style>