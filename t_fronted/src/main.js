/*
 * @Author: your name
 * @Date: 2021-03-07 22:17:04
 * @LastEditTime: 2021-03-08 15:48:11
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /t_fronted/src/main.js
 */
import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'
import VueResource from 'vue-resource'
Vue.use(VueResource );

Vue.config.productionTip = false;
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
