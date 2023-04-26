<template>
  <v-row
  align="center"
  justify="center"
  >
    <v-col cols="4">
      <LoginForm />
    </v-col>
  </v-row>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'

export default {
  name: 'login',
  components: {
    LoginForm,
  },
  
}
</script>

<style>
</style>