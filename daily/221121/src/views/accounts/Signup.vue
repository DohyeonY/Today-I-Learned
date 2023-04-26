<template>
  <div>
    <h1>Sign Up Page</h1>
    <img src="https://t.ctcdn.com.br/essK16aBUDd_65hp5umT3aMn_i8=/400x400/smart/filters:format(webp)/i606944.png" alt="">

    <form @submit.prevent="signUp">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model="username"><br>

      <label for="nickname">닉네임</label>
      <input type="text" id="nickname" v-model="nickname"><br>

      <label for="password1">비밀번호</label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2">비밀번호 확인</label>
      <input type="password" id="password2" v-model="password2"><br>
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      username : null,
      nickname: null,
      password1 : null,
      password2 : null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const nickname = this.nickname
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username : username,
        nickname : nickname,
        password1 : password1,
        password2 : password2,
      }
      if (password1 === password2) {
        this.$store.dispatch('signUp', payload)
        this.$router.push({name: 'Login'})
      } else {
         alert('패스워드가 일치하지 않습니다.')
         this.$router.push({name: 'Signup'})
      }      
    }
  }
}
</script>
