<template>

  <div class="box"
  @click="updateSizeList"
  :class="{ 'change-back' : size.selected }"
  >
{{ size.name }}
{{ size.price }}

    <br>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods : {
    updateSizeList () {
      this.$store.dispatch('updateSizeList', this.size)
    }
  }
}
</script>

<style>
.change-back {
  background-color: aqua;
}
</style>