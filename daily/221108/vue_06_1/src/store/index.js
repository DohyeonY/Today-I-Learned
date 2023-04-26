import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    list: [
      {
        id: 1638771553377,
        content: 'Vue',
        dueDateTime: '2021-12-11T16:05',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 1638771553378,
        content: 'Vue Router',
        dueDateTime: '2021-12-11T16:05',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 16387715533779,
        content: 'Vuex',
        dueDateTime: '2021-12-11T16:05',
        isCompleted: true,
        isImportant: false,
      },
    ],
  },
  getters: {
  },
  mutations: {
    CHANGE_IMPORTANT(state, listItem) {
      console.log(12312)
      const index = state.list.indexOf(listItem)
      // console.log(listItem)
      state.list[index].isImportant = !state.list[index].isImportant
    },
    CREATE_TODO(state, todoItem) {
      console.log(341431)
      const newDate = new Date()
      const saveDate = `${newDate.getFullYear()}-${newDate.getMonth()+1}-${newDate.getDate()}T00:00`
      todoItem.dueDateTime = saveDate
      todoItem.id = Date.now()
      state.list.push(todoItem)
    }
  },

  actions: {
    changeImportant(context, listItem) {
      // console.log(listItem)

      context.commit('CHANGE_IMPORTANT', listItem)
    },
    createTodo(context, todoContent) {
      // const lenList = state.list.lenght
      
      const todoItem = {
        id: 0,
        content: todoContent,
        dueDateTime: null,
        isCompleted: false,
        isImportant: false,
      }
      context.commit('CREATE_TODO', todoItem)
    }

  },
  modules: {
  }
})
