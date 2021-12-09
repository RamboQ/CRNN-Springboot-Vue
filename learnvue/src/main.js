import Vue from 'vue'
import App from './App.vue'
import router from './router'
//import axs from 'axios'

//let axs = require('axios')
//axios.defaults.baseUrl = '/api'
//axios.defaults.headers.post['Content-Type']='application/json'
//Vue.prototype.$axios = axs

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
