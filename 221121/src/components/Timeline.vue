<template>
	<v-timeline
		dense
	>
		<v-timeline-item
			v-for="movie in my_movies"
			:key="movie.pk"
			max-height="800"
		>
			<v-card
			class="elevation-2 mx-auto"
			max-width="600"
			>
				<v-img
				:src="movie.img_url"
				height="400"
				>
					<v-card-title class="headline">{{ movie.title }}</v-card-title>
					<v-card-subtitle>개봉일: {{ movie.open_date }}</v-card-subtitle>
				</v-img>

			</v-card>
		</v-timeline-item>
	</v-timeline>
</template>

<script>
export default {
	name: "timeline",
	props: {
		my_movies: {
			type:Array
		}
	},
};
</script>

<style>
</style>