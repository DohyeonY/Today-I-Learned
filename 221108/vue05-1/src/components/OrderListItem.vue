<template>
  <div>
  <ul>
    <li>주문 제품 : {{ order.menu.title }}</li>
    <li>주문 가격 : {{ order.menu.price + order.size.price}}</li>
    <li>사이즈 : {{ order.size.name }}</li>
  </ul>
  <hr>
</div>
</template>

<script>

export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  // computed: {
  //   totalPrice: function () {
  //   },
  // },
}
</script>

<style>
</style>