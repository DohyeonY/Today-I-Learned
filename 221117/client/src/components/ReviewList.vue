<template>
  <v-simple-table fixed-header max-height="500px">
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Movie</th>
          <th class="text-left">Score</th>
          <th class="text-left">Content</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="review in my_reviews" :key="review.pk">
          <td>{{ review.movie }}</td>
          <td>
            <v-rating
              :value="review.score"
              color="orange"
              readonly
              >
            </v-rating>
          </td>
          <td>{{ review.content }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
export default {
  name: 'ReviewList',
  props: {
    my_reviews: {
			type:Array
		}
  }
}
</script>

<style>

</style>