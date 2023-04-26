<template>
  <div id="app">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-12">
          <h1 class="text-center">My First Youtube Project</h1>
            <SearchBar 
            @videos-emit="videosEmit"
            />
        </div>
      </div>

      <div class="row">

        <div class="col-7">
          <h1>영상</h1>
          <VideoDetail
          :video="video"
          />
        </div>

        <div class="col-5">
          <h1>영상 리스트</h1>
          <VideoList 
          :videos="videos"
          @get-video="getVideo"
          />
        </div>

      </div>

    </div>
  </div>
</template>


<script>
import SearchBar from '@/components/SearchBar'
import VideoDetail from '@/components/VideoDetail'
import VideoList from '@/components/VideoList'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },

  data: function () {
    return {
      selectedVideo : null,
      inputData: null,
      videos: [],
      video: {},
      
    }
  },
  methods: {
    videosEmit (videos) {
      this.videos = videos
    },
    getVideo (video) {
      this.video = video
      console.log(video)
    }

  },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
