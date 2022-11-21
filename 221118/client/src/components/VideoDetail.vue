<template>
  <div>
    <h2>VideoDetail</h2>
    <div>
      <iframe id="player" type="text/html" width="640" height="360" 
      :src="videoSrc" frameborder="0"></iframe>
      {{ videoSrc }}
    </div>
    <div>
      <h4>{{ video.snippet.title }}</h4>
      <p>{{ video.snippet.description}}</p>
    </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: Object
  },
  methods: {
    isSelected: function () {
      return Object.keys(this.video).length
    }
  },
  computed: {
    videoSrc: function () {
      if (this.isSelected()) {
        return "http://www.youtube.com/embed/" + this.video.id.videoId
      }
      return ''
    },
  },
}
</script>

<style>

</style>