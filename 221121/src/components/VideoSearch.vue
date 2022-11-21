<template>
  <div>
    <button @click="SearchVideo">{{ movie.title }} 관련 영상 찾기</button>
    <VideoList
      :videos="videos"
      @goApp="goApp"
    />
    <VideoDetail
      :videos="videos[0]"
    />
  </div>
</template>

<script>
import VideoList from './VideoList.vue'
import VideoDetail from './VideoDetail.vue'
import axios from 'axios'
export default {
  props: {
    movie : Object
  },
  components: {
    VideoList,
    VideoDetail
  },
  data() {
    return {
      videos: [],
      video: null,
    }
  },
  methods: {
    SearchVideo() {
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params: {
          key: 'AIzaSyBTX2_gE9Dd3AHnmkn56wMTRdkkNx8XFnY',
          q: this.movie.title + 'trailer',
          part: 'snippet',
          type: 'video'
        }
      })
        .then((res) => {
          this.videos = res.data.items
        })
        .catch((error) => {console.log(error)})
    },
    goApp(video) {
      this.$emit('goApp', video)
    }
  }
}
</script>

<style>
</style>