<template>
  <div id="app">
    <p >Counter: {{ counter }}</p>
    <p>Counter x2: {{ countDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 

  data () {
    return {
      count: 0,
    }
  },

  computed: {
    counter () {
      return this.$store.state.count
    },
    countDouble () {
      return this.$store.getters.countDouble
    },
    
  },
  methods: {
    increase () {
      return this.$store.commit('INCREASE')
    },
    decrease () {
      return this.$store.commit('DECREASE')
    },

  },
    // changeCount() {
    //   const newCount = this.count
    //   this.$store.dispatch('changeCount', newCount)
    // },
}
</script>

<style>
</style>
