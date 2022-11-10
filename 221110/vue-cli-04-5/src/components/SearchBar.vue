<template>
    <div>
      <input
      class="form-control"
      v-model="inputWordData"
      @keyup.enter="getVideos" type="text" 
        />
        <hr>
    </div>
  </template>

  <script>
  import axios from 'axios'
  export default {
    name: "SearchBar",
    data () {
        return {
            inputWordData : 'Ssafy',
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
                q: this.inputWordData,
                maxResults: 5
            }
            })
            .then(response => {
                console.log(response.data.items)
                this.videos.push(response.data.items)
                console.log(this.videos)
                this.$emit('videos-emit', this.videos)
            })
            .catch((error) => {
                console.log(error)
            })
        },

        setVideo(video) {
            this.video = video
            console.log(this.video)
        }
      },
      created () {
        this.getVideos()
      }
    }
  </script>
  
  <style>
  </style>