<template>
  <div @submit.prevent="createTodo">
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      console.log(1123)
      const title = this.title
      const API_URL ='http://127.0.0.1:8000'
      if(!title) {
        alert('제목을 입력하세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/todos/`,
        data: {
          title: title,
        },
        headers : {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(response => {
        console.log(response)
        this.$router.push({name: 'TodoList'})
      })
      .catch(error => {
        console.log(error)
        alert('로그인 하세요')
        this.$router.push({ name: 'Login'})
      })
    }
  }
}
</script>
