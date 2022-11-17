import Vue from 'vue'
import App from './App.vue'

import router from './router'
import store from './store'

import VueSession from 'vue-session'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;

Vue.use(VueSession);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
