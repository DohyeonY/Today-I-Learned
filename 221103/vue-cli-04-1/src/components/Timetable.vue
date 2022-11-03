<template>
  <div>
    <div class="col">
        <h1>예약 페이지</h1>
        <br>
        <h2>선생님 선택</h2>
        <button @click="clickTeacher">Eric</button>
        <button @click="clickTeacher">Tony</button>
        <br>
        <hr>
        <h2>시간 선택</h2>

        <div v-for="(time, index) in times" :key='index'>
        <button @click="clickBtn">{{ time }}</button>

        </div>
        <br>
        <button @click="clickSubmit">예약 확정</button>
        <br>
        <hr>
    </div>


  </div>
</template>

<script>
export default {
  name: 'Timetable',
  components: {


  },
   data: function() {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30",
        "15:00","15:30","16:00","16:30","17:00","17:30",
      ],
      selected: [],
      selectedTeacher : [],
      choiceTime: [],
      choiceTeacher: [],
    }
    
  },
  methods : {
    clickBtn : function(event) {
      if (!event.target.style.textDecoration) {
        event.target.style.textDecoration = 'line-through'

        if (this.selected.length == 5) {
          window.alert('5개 넘음')
          event.target.style.textDecoration = ''

        } else {
          this.selected.push(event.target.innerText)
        }

      } else {
        event.target.style.textDecoration = ''
        this.selected.splice(event.target.innerText, 1)

    }
  },
  clickTeacher : function(event) {
      if (!event.target.style.textDecoration) {
        event.target.style.textDecoration = 'line-through'
        this.selectedTeacher.push(event.target.innerText)
      } else {
        event.target.style.textDecoration = ''
        this.selectedTeacher.splice(event.target.innerText, 1)
    }
  },
  clickSubmit : function() {
    if (this.selected.length == 0) {
        window.alert("시간을 선택해")
    } else if(this.selectedTeacher == 0) {
        window.alert("선생님을 선택해")
    // } 
    // else if(!this.selected && this.selectedTeacher) {
    //     window.alert("선택해")
    } else {
        this.choiceTime.push(this.selected)
        this.choiceTeacher.push(this.selectedTeacher)
        const btnTag = document.querySelectorAll('button')
        btnTag.forEach((el) => {
            el.style.textDecoration = ''
        })
        const objectData = { 'time' : this.choiceTime, 'teacher' : this.choiceTeacher }
        this.$emit('click-submit', objectData)
        // this.$emit('click-submit', this.choiceTime)
        // this.$emit('click-submit', this.choiceTeacher)


        this.selected.splice(this.selected)
        this.selectedTeacher.splice(this.selectedTeacher)
        this.choiceTeacher.splice(this.choiceTeacher)
        this.choiceTime.splice(this.choiceTime)
    }
    }
  },

}
</script>

<style>

</style>