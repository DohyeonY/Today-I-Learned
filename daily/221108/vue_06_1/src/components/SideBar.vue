<template>
  <div id="nav">
    <router-link to="/" exact>모든</router-link>
    <router-link to="/today">오늘</router-link>
    <router-link to="/important">중요</router-link>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
#nav {
  border-radius: .5rem;
  border: 2px solid #2c3e50;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
}

#nav a {
  text-decoration: none;
  color: #2c3e50;
  font-size: 2rem;
}

#nav a.router-link-active {
  color: #42b983;
}
</style>