<template>
  <div style="text-align:center;">
    <h1 style="text-align:center;">SSAFY TUBE</h1>
      <hr>
      <iframe
      style="width:800px; height:600px;"
        class="embed-responsive-item"
        frameborder="0"
        allowfullscreen="1"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        :src="`https://www.youtube.com/embed/${video[0].id.videoId}`"
      ></iframe>
      <br>
      <h2>{{ video[0].snippet.title }}</h2>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "App",
  data () {
      return {
          videos: [],
          video: {},
      }
  },

  methods: {
    getVideos () {
      this.videos = []
      this.video = {}
      const baseURL = "https://www.googleapis.com/youtube/v3/search"
      const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
      // Youtube API에 요청을 보내어
      axios
          .get(baseURL, {
          params: {
              // key, part, q
              key: API_KEY,
              part: "snippet",
              type: "video",
              q: '코딩노래',
              maxResults: 1
          }
          })
          .then(response => {
              this.video = response.data.items
              console.log(response.data)
              console.log(this.video)
          })
          .catch((error) => {
              console.log(error)
          })
      },
    },

    created () {
      this.getVideos()
    }
  }
</script>

<style>
</style>