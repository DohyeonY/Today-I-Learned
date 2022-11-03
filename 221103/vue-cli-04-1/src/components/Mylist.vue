<template>
  <div>
    <h1>상담 신청 현황</h1>
        <h2>상담 선생님</h2>
        <p>성함 : {{ getTeacher.join(' ') }}</p>
        <br>
        <hr>
        <p>선택 시간 : {{ getTime.join(' ') }}</p>
        <hr>
        <img alt="Vue logo" src="../assets/ssafy-logo.png">
    </div>
</template>

<script>
export default {
 name: 'Mylist',
 props : {
    getTeacher : Array,
    getTime : Array,
 }
}
</script>

<style>

</style>