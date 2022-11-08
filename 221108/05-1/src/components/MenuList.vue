<template>
  <div class="menu-list">
    <h1>1. 음료를 고르세요.</h1>
    <menuList/>
  </div>
</template>

<script>

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