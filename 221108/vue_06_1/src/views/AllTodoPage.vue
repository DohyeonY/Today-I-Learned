<template>
  <div>
    <h1 stlye="text-align:center;">모든 할일</h1>
    <div class="input-group mb-3">
      <button @click="createTodo" class="btn" type="button" id="button-addon1">+</button>
      <input type="text" class="form-control" placeholder="할 일을 자겅해주세요!" aria-label="Example text with button addon" aria-describedby="button-addon1" v-model="todoTitle">
    </div>
    <hr>
    <div v-for="list in allList" 
      :key="list.id"
      class="input-group mb-3">
      <div class="input-group-text">
        <input class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input">
      </div>
      <div class="form-control">
        {{ list.content }}

        <div @click="changeImportant(list)" style="text-align: right;" v-if="list.isImportant" >★</div>
        <div @click="changeImportant(list)" style="text-align: right;" v-else>☆</div>
      </div>
      
    </div>
    
  </div>
</template>

<script>
export default {
  data () {
    return {
      todoTitle: ''
    }
  },
  computed: {
    allList () {
      return this.$store.state.list
    }
  },
  methods : {
    changeImportant(list) {
      
      this.$store.dispatch('changeImportant', list)
    },
    createTodo() {
      if (this.todoTitle) {
        this.$store.dispatch("createTodo", this.todoTitle)
      }
      this.todoTitle = null
    }
  },

}
</script>

<style>

</style>