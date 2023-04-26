<template>
    <div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Logout',
    data() {
      return {
        username : null,
        password : null,
  
      }
    },
    created() {
        console.log('삭제')
        if (!this.$store.getters.isLogin) {
            alert('로그인 먼저 하세요')
            this.$router.push({ name: 'Login'})
        } else {
            this.$store.commit('DELETE_TOKKEN')
        }
    }

  }
  </script>
  