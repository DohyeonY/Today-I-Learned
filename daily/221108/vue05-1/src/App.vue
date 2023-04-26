<template>
  <div id="app">
    <h1 style="text-align: center;">Coffee Order App</h1>
    <hr>
    <div class="container text-center">
      <div class="row">
        <div class="col"><MenuList /></div>
        <div class="col"><SizeList /></div>
      </div>
    </div>
    <hr>
    <b-button style="width:700px;" @click="addOrder" variant="primary">Order</b-button>

    <hr>
    <br>
    
    <!-- {{ orderList }} -->
    <h1 style="text-align: center;">장바구니</h1>
    <hr>
    <ul>
      <li>총 갯수 : {{ totalOrderCount }}</li>
      <li>총 가격 : {{ totalOrderPrice }}</li>
    </ul>
    <hr>
    <OrderList/>

  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'

export default {
  name: 'App',
  components : {
    MenuList,
    SizeList,
    OrderList,
  },
  computed: {
    orderList () {
      return this.$store.state.orderList
    },
    totalOrderCount () {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice () {
      return this.$store.getters.totalOrderPrice
    }
  },
  methods : {
    addOrder () {
      this.$store.dispatch('addOrder')
    }
  },
}

  

</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}
.flex-container{
  display: flex;
}

.flex-item{
  margin: 10px;
  text-align: center;
}
/* ul {
  list-style: none;
} */
</style>
