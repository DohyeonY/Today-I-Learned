<template>
  <header>
    <img src="@/assets/ssafybanner.png" alt="">
    <div class="router-box">
      <router-link :to="'/'"><h3>Movie</h3></router-link>
      <router-link :to="'/random'"><h3>Random</h3></router-link>
      <router-link :to="'/watch'"><h3>WatchList</h3></router-link>
    </div>
  </header>
</template>

<script>
export default {};
</script>

<style scoped>
header img {
  width: 100px;
}

header {
  position: fixed;
  z-index: 200;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 40px;
  background-color: rgb(228, 242, 253);
  height: 5rem;
  top: 0;
  right: 0;
  left: 0;
  transition: all 0.5s;
}
header h3 {
  color: black;
  font-size: 32px;
}

header h3:hover {
  color: #42b983;
}

.router-box {
  width: 30%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

a {
  text-decoration: none;
}

a.router-link-exact-active h3 {
  color: #42b983;
}

</style>