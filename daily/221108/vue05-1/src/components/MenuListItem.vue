<template>
  <div>
    <div class="box" @click="updateMenuList"
    :class="{ 'change-back' : MenuList.selected }"
    >
      {{ MenuList.title }} {{ MenuList.price }}
      <br>
      <img :src="MenuList.image" alt="42141" style="width:50px; height:50px;">
      <!-- <p style="smallbox">{{ MenuList.price }}</p> -->
      <!-- <p style="smallbox">{{ MenuList.selected }}</p> -->
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    MenuList: Object,
  },
  methods : {
    updateMenuList() {
      this.$store.dispatch('updateMenuList', this.MenuList)
    }
  },
}
</script>

<style>
.box{
  box-sizing: content-box;
  border:solid black 1px;
  padding: 0px;
  display: grid;
  height: 130px;
 }
 .change-back {
  background-color: aqua;
}

</style>