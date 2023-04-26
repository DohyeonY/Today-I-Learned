<template>
  <div>
    <OrderListItem v-for="order in orderList" :key="order.title" :order="order"/>
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'
export default {
  name: 'OrderList',
  components : {
    OrderListItem
  },  
  computed: {
    orderList () {
      return this.$store.state.orderList
    },
    // totalOrderCount () {
    //   return
    // },
    // totalOrderPrice () {
    //   return
    // },
  },
}
</script>

<style>
</style>