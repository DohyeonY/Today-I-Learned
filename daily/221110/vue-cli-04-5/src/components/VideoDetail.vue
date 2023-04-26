<template>
    <div>
        <div v-if="video.id" class="embed-responsive embed-responsive-16by9">
            <iframe
            class="embed-responsive-item"
            frameborder="0"
            allowfullscreen="1"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            :src="`https://www.youtube.com/embed/${video.id.videoId}`"
            ></iframe>
            <h3>{{ video.snippet.title }}</h3>
            <h5>{{ video.snippet.description }}</h5>
        </div>
        <img v-else style="width:200px; height: 200px;" src="../assets/noResult.png" alt="11">
    </div>
  </template>
  
  <script>

  
  export default {
    name: "VideoDetail",
    props: {
        video : Object
    },  
    computed: {

    }
  };
  </script>
  
  <style>
  </style>