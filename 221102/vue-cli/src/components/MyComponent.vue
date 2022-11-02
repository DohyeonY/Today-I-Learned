<template>
  <div>
    <h1>이곳은 HelloWorld.vue 입니다</h1>
    <MyComponentItem v-bind:static-props="MyComponent에서 보낸 데이터"/>
    <!-- <MyComponentItem/>
    <MyComponentItem/> -->
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'
// import MyComponentitem from './MyComponentitem.vue'
export default {
    name : 'MyComponent',
    components : {
        // 2. 등록하기
        MyComponentItem,

    }
}
</script>

<style>
    .border {
            border : solid 1px black;
    }
</style>
