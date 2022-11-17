<template>

  <v-hover v-slot:default="{ hover }">
    <v-card class="movie-card">

      <v-img
        :src="movie.img_url"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        height="200px"
      >
      </v-img>


      <v-expand-transition>
        <div 
          v-if="hover || rating !== 0"
          class="d-flex transition-fast-in-fast-out black darken-2 text-center display-1 v-card--reveal"
          @click.stop="review_dialog_show=true"
        >
          <v-rating
            v-model="rating"
            color="orange"
            background-color="orange lighten-3"
            size="21.6"
          ></v-rating>
        </div>
      </v-expand-transition>

      <v-dialog
        v-model="review_dialog_show"
        max-width="500"
      >
        <MovieReviewModal :rating="rating" :movie="movie" @reviewUpdateEvent="ratingCheck" @closeDialogEvent="closeReviewDialog"/>
      </v-dialog>


      <v-card-actions>

        <v-spacer></v-spacer>

        <!-- <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-bookmark</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-share-variant</v-icon>
        </v-btn> -->

        <!-- detail modal -->
        <v-dialog v-model=detail_dialog_show width="600px">
          <template v-slot:activator="{ on }">
            <v-btn small v-on="on">
              <v-icon>mdi-file-document-box-search-outline</v-icon>Detail
            </v-btn>
          </template>
          <MovieDetailModal :movie="movie" :reviews="reviews" @reviewUpdateEvent="ratingCheck" @closeDialogEvent="closeDetailDialog"/>
        </v-dialog>


      </v-card-actions>
    </v-card>
  </v-hover>

</template>

<script>
  import axios from 'axios'
  import jwtDecode from 'jwt-decode'
  import MovieDetailModal from '@/components/MovieDetailModal.vue'
  import MovieReviewModal from '@/components/MovieReviewModal.vue'

  export default {
    data: () => ({
      reviews: [],
      rating: 0,
      detail_dialog_show: false,
      review_dialog_show: false,
    }),

    components: {
      MovieDetailModal,
      MovieReviewModal,
    },

    props: {
      movie: {
        type: Object,
        required: false,
      }
    },

    methods: {

      closeDetailDialog() {
        this.detail_dialog_show = false
      },

      closeReviewDialog() {
        this.review_dialog_show = false
      },
      
      // rating한 적이 있는 영화는 별점 표시 (mount되는 시점에서 실행되는 함수)
      ratingCheck() {
        // 현재 영화의 리뷰 목록에서 현재 로그인한 사람의 id를 찾아본다.
        const token = sessionStorage.getItem('jwt')
        const user_id = jwtDecode(token).user_id
        const options = {
          headers: {
            Authorization: 'JWT ' + token
          }
        }

        axios.get(`http://localhost:8000/api/v1/review/movie/${this.movie.id}/`, options)
        .then(res => {
          this.reviews = res.data
          this.reviews.forEach(review => {
            if (review.user === user_id) {
              this.rating = review.score
            }
            axios.get(`http://localhost:8000/api/v1/user/${review.user}/`, options)
            .then(res => {
              review.username = res.data.username
            })
          })
        })
      } // end of ratingCheck()

    },

    watch: {

    }, // watch end
    
    mounted() {
      this.ratingCheck()
    }

  }
</script>

<style>
.v-card--reveal {
  align-items: center;
  bottom: 18%;
  justify-content: center;
  opacity: 0.8;
  position: absolute;
}

</style>