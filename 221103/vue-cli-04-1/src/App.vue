<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
  <h1>버튼 박스 제작</h1>
  
    <div clsaa="container text-center" style="border:1px solid black;">
      <div class="row">


        <div class="col">
         <Timetable @click-submit="parentGetEvent"/>

        </div>
        
        <div class="col">
          <Mylist :get-time="getTime" :get-teacher="getTeacher"/>

        </div>

      </div>
    </div>

  </div>

  
</template>

<script>

import Mylist from '@/components/Mylist'
import Timetable from '@/components/Timetable'


export default {
  name: 'App',
  components: {
    Timetable,
    Mylist,

  },
   data: function() {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30",
        "15:00","15:30","16:00","16:30","17:00","17:30",
      ],
      getTime: [],
      getTeacher: [],
    }
    
  },
  methods : {
    parentGetEvent : function(inputData) {
      console.log(`${inputData}`)
      this.getTime.splice(this.getTime)
      this.getTeacher.splice(this.getTeacher)
      console.log(`${inputData.time}`)
      console.log(`${inputData.teacher}`)
      this.getTime.push(`${inputData.time}`)
      this.getTeacher.push(`${inputData.teacher}`)
      // console.log(this.getTime)
      // console.log(this.getTeacher)

    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>



