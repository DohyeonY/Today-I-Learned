<template>
  <div>
    <div class="card padding" style="width:700px; height:800px; margin:auto; border:none; ">

      <div class="card-title" style="margin-bottom:0px; border-radius:20px 20px 0 0;">
        <h5 class="card-title" style="margin-bottom:0px; background-color: #E3F2FD;"><WatchListForm/></h5>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item nopadding" ><WatchListItem/></li>
      </ul>
    </div>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm'
import WatchListItem from '@/components/WatchListItem'


export default {
  name: "WatchListView",
  data() {
    return {

    }
  },
  components: {
    WatchListForm,
    WatchListItem,
  },
  methods: {
    add() {

    }
  }
}
</script>

<style>
 .nopadding{
  padding-top :0px;
  
 }
</style>