<template>
  <div>
    <h2 v-if="incomeCal < 0">결정세액 : 0 만원</h2>
    <h2 v-else-if="0 <= incomeCal < 1200">결정세액 : {{ incomeCal * 6 / 100 - taxDiscount}} 만원</h2>
    <h2 v-else-if="1200 <= incomeCal < 4600">결정세액 : {{ (incomeCal * 15 / 100) - 108 - taxDiscount}} 만원</h2>
    <h2 v-else-if="4600 <= incomeCal < 8800">결정세액 : {{ (incomeCal * 24 / 100) - 522 - taxDiscount}} 만원</h2>
    <h2 v-else-if="8800 <= incomeCal < 15000">결정세액 : {{ (incomeCal * 35 / 100) - 1490 - taxDiscount}} 만원</h2>
    <h2 v-else-if="15000 <= incomeCal < 30000">결정세액 : {{ (incomeCal * 38 / 100) - 1940 - taxDiscount}} 만원</h2>
    <h2 v-else-if="30000 <= incomeCal < 50000">결정세액 : {{ (incomeCal * 40 / 100) - 2540 - taxDiscount}} 만원</h2>
    <h2 v-else-if="50000 <= incomeCal < 100000">결정세액 : {{ (incomeCal * 42 / 100) - 3540 - taxDiscount}} 만원</h2>
    <h2 v-else-if="100000 <= incomeCal">결정세액 : {{ (incomeCal * 45 / 100) - 6540 - taxDiscount}} 만원</h2>
    <!-- <h1>{{ taxDiscount }}</h1> -->
  </div>
</template>

<script>
export default {
    name: 'Finaltax',
    props : {
      incomeCal: String,
      taxDiscount: String,
    },
}
</script>

<style>

</style>