import Vue from 'vue'
import Router from 'vue-router'

// 导入刚才编写的组件
import AppIndex from './components/home/AppIndex'
import Login from './components/Login'
import signUp from './components/sign-up'
import infer from './components/home/imgTransfer'


Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        { path: '/', redirect: '/login' },
        { path: '/login', name: 'Login', component: Login },
        { path: '/index', name: 'AppIndex', component: AppIndex },
        { path: '/signUp', name: 'sign-up', component: signUp},
        { path: '/infer', name: 'infer', component: infer},
    ]
})