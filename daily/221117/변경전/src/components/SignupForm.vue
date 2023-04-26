<template>
  <div class="signup-form mx-auto">
    <h1>회원가입 페이지</h1>

    <form class="signup-input" @submit.prevent="signup(userInput)">
      <div v-if="getErrors.length" class="error-list alert alert-danger">
        <p></p>
        <ul>
          <li v-for="(error, idx) in getErrors" :key="idx">{{ error }}</li>
        </ul>
      </div>
      <br>
      <div class="form-group">
        <v-text-field v-model="userInput.username" label="아이디" name="username"></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field v-model="userInput.email" label="닉네임" name="nickname"></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field
          v-model="userInput.password"
          label="비밀번호"
          name="Password"
          type="password"
        ></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field
          v-model="userInput.passwordConfirmation"
          label="비밀번호 확인"
          name="passwordConfirmation"
          type="password"
        ></v-text-field>
      </div>

      <button>회원가입</button>
    </form>
  </div>
</template>

<script>
// import { mapGetters, mapActions } from "vuex";
import axios from 'axios'
export default {
  name: "SignupForm",
  data() {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
        email: null,
      }
      // userInput: {
      //   username: null,
      //   nickname:null,
      //   password: null,
      //   passwordConfirmation: null,
      // }
    };
  },
  methods: {
    // ...mapActions(["signup"])
    signup() {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
      .then(
        this.$router.push({ name:'login' })
      )
      .catch(
        err => console.log(err)
      )
    }
  },
  // computed: {
  //   ...mapGetters(["getErrors"])
  // },
};
</script>

<style>
</style>