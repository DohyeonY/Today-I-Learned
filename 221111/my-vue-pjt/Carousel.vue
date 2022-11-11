<template>
  <div>
    <Header :class="transparent_nav ? 'transparent-bg' : ''"></Header>
  </div>
  <div class="carousel-container">
    <swiper
      :slide-per-view="1"
      :navigation="true"
      :autoplay="{ delay: 5000, disableOnInteraction: false }"
      class="carousel"
    >
      <swiper-slide v-for="feature in features.value" :key="feature.id">
        <div
          class="hero"
          :style="{
            background: `linear-gradient(rgba(0, 0, 0, 0) 39%, rgba(0, 0, 0, 0) 41%, rgba(0, 0, 0, 0.65) 100%),url('${
              this.featureURL
            }${
              isMobile ? feature.poster_path : feature.backdrop_path
            }'),rgb(28, 28, 28)`,
          }"
        >
          <div class="hero-content">
            <!-- <div class="hero-content-text">
              <h1>
                <router-link :to="'/movie/' + feature.id" class="movie-link">
                  <span>{{ feature.title }}</span>
                </router-link>
              </h1>
              <p>{{ feature.overview }}</p>
            </div> -->
          </div>
        </div>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import { ref } from "vue";
import { Swiper, SwiperSlide } from "swiper/vue";
import Header from "@/components/Header.vue";
// Import Swiper Styles
import "swiper/swiper-bundle.min.css";
import "swiper/swiper.min.css";

import NavSwiper, { Navigation, Autoplay } from "swiper";
NavSwiper.use([Navigation, Autoplay]);
import env from "@/env";
export default {
  props: ["type"],
  components: {
    Swiper,
    SwiperSlide,
    Header,
  },
  data() {
    return {
      featureURL: env.BACKDROP_URL.large,
      features: ref([]),
      page: 1,
      isMobile: false,
      transparent_nav: true,
    };
  },
  methods: {
    getFeatureData() {
      fetch(`https://api.themoviedb.org/3/trending/movie/week?${env.API_KEY}`)
        .then((response) => response.json())
        .then((data) => (this.features.value = data.results));
    },
    onSwiper(swiper) {
      console.log(swiper);
    },
    mobileBreakpoint() {
      this.isMobile = window.innerWidth < 600;
    },
    handleScroll() {
      if (window.pageYOffset > 300) {
        this.transparent_nav = false;
      } else {
        this.transparent_nav = true;
      }
    },
  },
  beforeMount() {
    this.getFeatureData();
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeUnmount() {
    if (typeof window === "undefined") return;

    window.removeEventListener("resize", this.mobileBreakpoint, {
      passive: true,
    });
    window.removeEventListener("scroll", this.handleScroll);
  },
  mounted() {
    this.mobileBreakpoint();
    window.addEventListener("resize", this.mobileBreakpoint, { passive: true });
  },
};
</script>

<style scoped>
.transparent-bg {
  background-color: transparent !important;
}
.hero {
  background-size: 150%, cover !important;
  background-position: 50%, 50% !important;
  height: 100%;
  cursor: move;
}
.carousel {
  margin-top: -6rem !important;
  height: calc(100vh - 5.5rem);
  overflow-x: hidden;
}
.hero-content {
  max-width: 1280px;
  padding: 20px 50px;
  margin: 0 auto;
}
.hero-content-text {
  z-index: 100;
  max-width: 700px;
  position: absolute;
  bottom: 40px;
  margin-right: 20px;
  min-height: 100px;
  background: transparent;
  color: #fff;
}
.hero-content h1 span {
  font-size: 46px;
  font-weight: 500;
  margin-block-start: 0.67em;
  margin-block-end: 0.67em;
  /* text-decoration: none; */
  color: #fff;
  user-select: none;
}
.hero-content h1 span:hover {
  color: #42b883;
}
.hero-content p {
  font-size: 22px;
  font-weight: 200;
  line-height: 26px;
  color: #fff;
  margin-block-start: 1em;
  margin-block-end: 1em;
  user-select: none;
}
</style>
