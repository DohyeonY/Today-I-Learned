<template>
    <div>
    <h3>Ssafy 여러분을 응원합니다!</h3>
    <p>{{ staticProps }}</p>
    </div>
</template>

<script>
export default {
    name: 'MyComponentItem',
    props: {
        staticProps : String,
    }
}
</script>

<style>

</style>