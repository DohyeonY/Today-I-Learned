<template>
  <div @click="goDetail(article.id)">
    <P>글 번호 : {{ article.id }}</P>
    <P>글 제목 : {{ article.title }}</P>
    <hr>
    <!-- <P>글번호 : {{ article.id }}</P> -->
  </div>
</template>

<script>
export default {
    name: 'ArticleItem',
    props: {
        article: Object
    },
    methods : {
        goDetail(id) {
            this.$router.push({name:'detail', params: {id}})
            // this.$router.push({ namd: 'detail', params : {id: `${this.article.id}`} })
        }
    }

}
</script>

<style>

</style>