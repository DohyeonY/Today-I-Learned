<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import { constants } from 'buffer';

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content : null
    }
  },
  methods: {
    createArtcicle() {
      const title = this.title
      const content = this.content
      if(!title) [{
        alert('제목을 입력하세요')
      }]
      else if (!comment) {
        
      }
    }
  }
}
</script>

<style>

</style>
