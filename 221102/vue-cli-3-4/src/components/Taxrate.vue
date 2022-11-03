<template>
  <div>
    <hr>
    <h2 v-if="incomeCal < 0">산출세액 : 0 만원</h2>
    <h2 v-else-if="0 <= incomeCal < 1200">산출세액 : {{ incomeCal * 6 / 100 }} 만원</h2>
    <h2 v-else-if="1200 <= incomeCal < 4600">산출세액 : {{ round((incomeCal * 15 / 100) - 108)}} 만원</h2>
    <h2 v-else-if="4600 <= incomeCal < 8800">산출세액 : {{ round((incomeCal * 24 / 100) - 522)}} 만원</h2>
    <h2 v-else-if="8800 <= incomeCal < 15000">산출세액 : {{ math.round((incomeCal * 35 / 100) - 1490)}} 만원</h2>
    <h2 v-else-if="15000 <= incomeCal < 30000">산출세액 : {{ math.round((incomeCal * 38 / 100) - 1940)}} 만원</h2>
    <h2 v-else-if="30000 <= incomeCal < 50000">산출세액 : {{ math.round((incomeCal * 40 / 100) - 2540)}} 만원</h2>
    <h2 v-else-if="50000 <= incomeCal < 100000">산출세액 : {{ math.round((incomeCal * 42 / 100) - 3540)}} 만원</h2>
    <h2 v-else-if="100000 <= incomeCal">산출세액 : {{ math.round((incomeCal * 45 / 100) - 6540)}} 만원</h2>

    <h2>세액감면 : {{ taxDiscount }} 만원</h2>
    <hr>
    <Finaltax :income-cal="incomeCal" :tax-discount="taxDiscount"/>

  </div>
</template>

<script>
import Finaltax from './Finaltax.vue'
export default {
  components: { Finaltax },
    name: "TaxRate",
    props : {
      incomeCal: String,
      taxDiscount: String,
    },
    data: function () {
        return {
          sanculTax : '',
          income : '',
          discount : '',

        }
    },
    // methods : {
    //  SanCulTax : function () {
    //   const san = incomeCal
    //   if (san <= 1200) {
    //     this.sanculTax = san * 6 / 100
    //   } else if (1200 < san <= 4600) {
    //     this.sanculTax = (san * 15 / 100) -108
    //   } else if (4600 < san <= 8800) {
    //     this.sanculTax = (san * 24 / 100) - 522
    //   } else if (8800 < san <= 15000) {
    //     this.sanculTax = (san * 35 / 100) - 1490
    //   } else if (15000 < san <= 30000) {
    //     this.sanculTax = (san * 38 / 100) - 1940
    //   } else if (30000 < san <= 50000) {
    //     this.sanculTax = (san * 40 / 100) - 2540
    //   } else if (50000 < san <= 100000) {
    //     this.sanculTax = (san * 42 / 100) - 3540
    //   } else {
    //     this.sanculTax = (san * 45 / 100) - 6540
    //   }
    //   } 
    // }
}
</script>

<style>

</style>