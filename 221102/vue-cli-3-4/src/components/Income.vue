<template>
  <div>
    <p>연봉 입력 (만원) : <input v-model="income" type="number"></p>

    <p>세액감면액 (만원) : <input v-model="discount" type="number"></p>
    <hr>
    <h2>종합소득금액 : {{ income }} 만원 </h2>
    <h2>종합소득공제 : (-) 150 만원</h2>
    <h2 v-if="income - 150 >= 0">과세표준 : {{ income - 150 }} 만원</h2>
    <h2 v-else>과세표준 : 0 만원</h2>
    <Taxrate :income-cal='income-150' :tax-discount="discount"/>
    
  </div>
</template>

<script>
import Taxrate from './Taxrate.vue'
export default {
    name: "Income",
    components: {
      Taxrate,

    },
    data: function () {
        return {
          income : '',
          discount : '',

        }
    },
    // methods: {
    //   inputNum : function (event) {
    //     this.income = event.target.value
    //   }
    // },
}
</script>

<style>

</style>