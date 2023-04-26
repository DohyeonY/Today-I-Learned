<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'Singup',
  data: function () {
    return {
      username : null,
      password1 : null,
      password2 : null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username : username,
        password1 : password1,
        password2 : password2,
      }
      if (password1 === password2) {
        this.$store.dispatch('signUp', payload)
        } else {
         alert('패스워드가 일치하지 않습니다.')
        }


      // this.$router.push({name: 'Login'})
    }
  }
}
</script>
