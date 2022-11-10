<template>
<div class="card mb-3" style="max-width: 540px;">
    <div class="row g-0">

        <div class="col-md-4">
            <img class="img-fluid rounded-start" :src="video?.snippet.thumbnails.high.url" />
        </div>

        <div class="col-md-8">
            <div class="card-body">
                <h5 class="card-title">{{ video?.snippet.title }}</h5>
                <p class="card-text">{{ video?.snippet.title }}</p>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
name: "VideoListItem",
props: {
    video: Object
}
};
</script>

<style>
</style>