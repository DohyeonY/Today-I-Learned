<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <span 
          @click="updateTodoStatus(todo)" 
          :class="{ 'is-completed': todo.is_completed }"
        >
        {{ todo.title }}
        </span>
        
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  methods: {
    getTodos: function () {
      this.$store.dispatch('getArticles')
      this.todos = this.$store.state.articles
    },
    //   axios({
    //     method: 'get',
    //     url: 'http://127.0.0.1:8000/todos/',
    //     headers : {
    //       Authorization: `Token ${this.$store.token}`
    //     }
    //   })
    //     .then(res => {
    //       console.log(res)
    //       this.todos = res.data
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // },
    deleteTodo: function (todo) {
      // 3번 문제
      const index = this.todos.indexOf(todo)
      this.todos.splice(index, 1)
      
      },

    updateTodoStatus: function (todo) {
      // 4번 문제
      console.log(todo)
      todo.is_completed = !todo.is_completed
    },
  },
  }

</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
