/*
 * @Author: your name
 * @Date: 2021-03-07 22:17:04
 * @LastEditTime: 2021-03-09 19:13:47
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /t_fronted/src/router/index.js
 */
// import { from } from 'core-js/core/array'
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Buf from '../views/Buf.vue'
import Update from '../views/Update.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    redirect:"/info"
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path:'/info',
    name:'教师信息',
    component:Buf
  },
  {
    path:"/update",
    name:"Update",
    component: Update
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
