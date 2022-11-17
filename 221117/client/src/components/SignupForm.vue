<template>
  <div class="signup-form mx-auto">
    <h1>Signup</h1>

    <form class="signup-input" @submit.prevent="signup(userInput)">
      <div v-if="getErrors.length" class="error-list alert alert-danger">
        <p></p>
        <ul>
          <li v-for="(error, idx) in getErrors" :key="idx">{{ error }}</li>
        </ul>
      </div>
      <br>
      <div class="form-group">
        <v-text-field v-model="userInput.username" label="username" name="username"></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field v-model="userInput.nickname" label="Nickname" name="nickname"></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field
          v-model="userInput.password"
          label="Password"
          name="Password"
          type="password"
        ></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field
          v-model="userInput.passwordConfirmation"
          label="Password Confirmation"
          name="passwordConfirmation"
          type="password"
        ></v-text-field>
      </div>

      <button>Register</button>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "SignupForm",
  data() {
    return {
      userInput: {
        username: "",
        nickname:"",
        password: "",
        passwordConfirmation: ""
      }
    };
  },
  methods: {
    ...mapActions(["signup"])
  },
  computed: {
    ...mapGetters(["getErrors"])
  },
};
</script>

<style>
</style>