<template>
  <div>
    <img src="https://t.ctcdn.com.br/essK16aBUDd_65hp5umT3aMn_i8=/400x400/smart/filters:format(webp)/i606944.png" alt="">
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password">비밀번호</label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
      <button @click="goSignup">Signup</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username : null,
      password : null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,

      }
      this.$store.dispatch('logIn', payload)
    },
    goSignup() {
      this.$router.push({name: 'Signup'})
    }
  }
}
</script>