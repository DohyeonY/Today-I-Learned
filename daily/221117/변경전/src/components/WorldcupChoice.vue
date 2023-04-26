<template>

  <div v-if="!!movie">
    <h2>{{movie.title}}</h2>
    <v-hover
      v-slot:default="{ hover }"
      :open-delay="openDelay"
      :close-delay="closeDelay"
      :disabled="disabled"
      :value="value"
      max-height="600px"
    >
      <v-img
        @click="select"
        :src="movie.img_url"
        alt=""
        width="400px"
        height="600px"
        :elevation="hover ? 12 : 2"
      ></v-img>
    </v-hover>
  </div>

</template>

<script>
// import axios from 'axios'

export default {
  data () {
    return {
      movieObject: null,
      disabled: false,
      openDelay: '0',
      closeDelay: '0',
      value: false,
    }
  },
  
  props: {
    movie:{
      type: Object,
      required: false,
    }
  },

  methods: {
    select() {
      this.$emit('choiceEvent', true)
    }
  }

}
</script>

<style>

</style>