<template>
  <div id="login-form" class="mx-auto">
    <h1>로그인 페이지</h1>
    <div v-if="isLoading" class="spinner-border" role="status">
      <span class="sr-only">Loading</span>
    </div>

    <form 
      v-else class="login-input" 
      @submit.prevent="login(credentials)"
      @keyup.enter="login(credentials)"
      >
      <div v-if="getErrors.length" class="error-list alert alert-danger">
        <ul>
          <li v-for="(error, idx) in getErrors" :key="idx">
            {{ error }}
          </li>
        </ul>
      </div>

      <div class="form-group">
        <v-text-field v-model="credentials.username" label="아이디" name="Username"></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field
          v-model="credentials.password"
          label="비밀번호"
          name="Password"
          type="password"
        ></v-text-field>
      </div>
      <div>
        <button>로그인</button>
      </div>
    </form>
  </div>
</template>

<script>
// import router from '../router';  // '../router/index.js'
import { mapGetters, mapActions} from "vuex";

export default {
  name: "LoginForm",
  data() {
    return {
      credentials: {
        // id,password 에 해당하는 data
        username: "",
        password: ""
        // loading: 0,
      }
    };
  },
  methods: {
    ...mapActions(['login'])
  },
  computed: {
    ...mapGetters(['getErrors', 'isLoading'])
  }
};
</script>

<style>
</style>