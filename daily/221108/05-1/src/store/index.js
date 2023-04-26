import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title : '아메리카노',
        price : 3000,
        selected : true, //초기값
        image: '<https://source.unsplash.com/featured/?americano>'
      },
      {
        title : '에스프레소',
        price : 3500,
        selected : true,
        image : '<https://source.unsplash.com/featured/?espresso>'
      },
      {
        title : '라떼',
        price : 4000,
        selected : true,
        image : '<https://source.unsplash.com/featured/?latte>'
      }
    ],
    sizeList: [],
  },
  getters: {
  },
  mutations: {
    addOrder: function () {},
    updateMenuList: function () {},
    updateSizeList: function () {},
  },
  actions: {
  },
  modules: {
  }
})