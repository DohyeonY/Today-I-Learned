import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [
      
    ],
    menuList: [
      {
        title : '아메리카노',
        price : 3000,
        selected : false, //초기값
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        title : '에스프레소',
        price : 3500,
        selected : false,
        image : 'https://source.unsplash.com/featured/?espresso'
      },
      {
        title : '라떼',
        price : 4000,
        selected : false,
        image : 'https://source.unsplash.com/featured/?latte'
      }
    ],
    sizeList: [
      {
        name : 'tall',
        price : 0,
        selected : false,
      },
      {
        name : 'grande',
        price : 500,
        selected : false,
      },
      {
        name : 'venti',
        price : 1000,
        selected : false,
      }
    ],
  },

  getters: {
    totalOrderCount (state) {
      return state.orderList.length
    },
    totalOrderPrice (state) {
      let result = 0
      state.orderList.forEach((order) => {
        result += order.size.price + order.menu.price
      })
      return result
    }
  },

  mutations: {
    ADD_ORDER (state) {
      console.log(11213)
      const newOrder = { menu : {}, size : {}}
      state.menuList.forEach((menu) => {
        if (menu.selected === true) {
          newOrder.menu = menu
          // state.orderList.menuPrice = menu.price
      }})
      state.sizeList.forEach((size) => {
        if (size.selected === true) {
          newOrder.size = size
          // state.orderList.size = size.name
          // state.orderList.sizePrice = size.price
          }
      })
      console.log(newOrder)
      state.orderList.push(newOrder)
      state.menuList.forEach((menu) => {
        menu.selected = false
      })
      state.sizeList.forEach((size) => {
        size.selected = false
      })
    },

    UPDATE_MENU_LIST (state, menuListItem) {
      state.menuList.forEach((menu) => {
        menu.selected = false
      })
      const index = state.menuList.indexOf(menuListItem)
      state.menuList[index].selected = !state.menuList[index].selected
      // console.log('dd')
    },

    UPDATE_SIZE_LIST (state, sizeListItem) {
      state.sizeList.forEach((size) => {
        size.selected = false
      })
      const index = state.sizeList.indexOf(sizeListItem)
      state.sizeList[index].selected = !state.sizeList[index].selected

    },

  },
  actions: {
    updateMenuList(context, menuListItem) {
      context.commit('UPDATE_MENU_LIST', menuListItem)
    },
    updateSizeList(context, sizeListItem) {
      context.commit('UPDATE_SIZE_LIST', sizeListItem)
    },
    addOrder(context, orderListItem) {
      context.commit('ADD_ORDER', orderListItem)
    }

  },
  modules: {
  }
})