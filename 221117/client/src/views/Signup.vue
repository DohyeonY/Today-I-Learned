<template>
  <v-row
  align="center"
  justify="center"
  >
    <v-col cols="6">
      <SignupForm />
    </v-col>
  </v-row>
</template>

<script>
import SignupForm from '../components/SignupForm'

export default {
  name: 'signup',
  components: {
    SignupForm,
  },
}
</script>

<style>

</style>