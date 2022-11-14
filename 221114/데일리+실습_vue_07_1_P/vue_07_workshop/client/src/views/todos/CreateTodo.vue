<template>
  <div>
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
const API_URL ='http://127.0.0.1:8000'
export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      const title = this.title
      axios({
        method: 'post',
        url: `${API_URL}/todos/`,
        data: {
          title,
        }
      })
      .then(response => {
        console.log(response)
        this.$router.push({name: 'TodoList'})
      })
    }
  }
}
</script>
