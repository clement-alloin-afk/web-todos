import Vue from 'vue'
import VueRouter from 'vue-router'
import Todos from './views/Todos'
import Login from './views/Login'
import Logout from './views/Logout'
import TodoSingle from './views/TodoSingle'

Vue.use(VueRouter)

export default new VueRouter({
	mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
		path: '/',
		name: 'todos',
		component: Todos,
		meta: {
			requiresLogin: true
			}
		},
		{
		path: '/login',
		name: 'login',
		component: Login,
		},
		{
		path: '/logout',
		name: 'logout',
		component: Logout,
		},
		{
		path: '/todo',
		name: 'todoSingle',
		component: TodoSingle,
		meta: {
			requiresLogin: true
			}
		}
	]
})