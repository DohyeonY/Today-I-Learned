<template>
  <div>
    <VideoListItem
      v-for="video in videos"
      :key="video.id.videoId"
      :video="video"
      :thumbnails="video.snippet.thumbnails.default.url"
      @goApp="goApp"
    />
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'


export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    goApp(video) {
      this.$emit('goApp', video)
    }
  }
}
</script>

<style>

</style>