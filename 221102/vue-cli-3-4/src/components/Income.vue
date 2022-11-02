<template>
  <div>
    <p>연봉 입력 (만원) : <input @input="inputNum" v-model="income" type="number"></p>

    <p>세액감면액 (만원) : <input v-model.number="age" type="number"></p>
    <hr>
    <h2>종합소득금액 : {{ income }} 만원 </h2>
    <h2>종합소득공제 : (-) 150 만원</h2>
    <h2>과세표준 : {{ income - 150 }} 만원</h2>
    
  </div>
</template>

<script>
export default {
    name: "Income",
    data: function () {
        return {
          income : ''
        }
    },
    methods: {
      inputNum : function (event) {
        this.income = event.target.value
      }
    },
}
</script>

<style>

</style>