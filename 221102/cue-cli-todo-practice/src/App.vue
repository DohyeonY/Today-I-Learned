<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">

    <TodoList :todos='todos' @delete-todo="deleteTodo"/>
    <TodoForm @create-todo="createTodo"/>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      todos : []
    }
  },
  methods: {
    createTodo: function (todoTitle) {
      const todo = {
        title : todoTitle
      }
      this.todos.push(todo)
    },
    deleteTodo: function (todo) {
      const index = this.todos.indexOf(todo)
      this.todos.splice(index, 1)
    },
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
