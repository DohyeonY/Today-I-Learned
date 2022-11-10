<template>
    <div>
      <div v-for="video in videos[0]" :key="video.id.videoId" @click="setVideo(video)">
        <VideoListItem :video="video"/>
      </div>
    </div>
  </template>
  
  <script>
  import VideoListItem from "@/components/VideoListItem";

  export default {
    name: "VideoList",
    props: {

        videos : Array,
    },
    data () {
        return {
            video: [],
        }
    },
    components: {
        VideoListItem
    },
    computed: {

    },
    methods: {
        setVideo(video) {
            this.video = video
            console.log(this.video)
            this.$emit('get-video', this.video)
        },

    }
  };
  </script>
  
  <style>
  </style>