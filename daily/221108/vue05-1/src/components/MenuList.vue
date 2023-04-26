<template>
  <div class="menu-list">
    <h1>1. 음료를 고르세요.</h1>
    <MenuListItem v-for="menu in menuList" :key="menu.title" :menu-list="menu"/>
    <!-- <MenuListItem/> -->
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem'

export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList () {
      return this.$store.state.menuList
    },
  },
  methods: {
    selectMenu: function () {},
  },
}
</script>

<style>

</style>