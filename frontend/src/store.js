import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from './axios-api'

Vue.use(Vuex)
export default new Vuex.Store({
	state: {
		accessToken: null,
		refreshToken: null,
		APIdata: ''
	},
	mutations: {
		updateStorage (state, { access, refresh }) {
			state.accessToken = access
			state.refreshToken = refresh
		},
		destroyToken (state) {
			state.accessToken = null
			state.refreshToken = null
		},
	},
	actions : {
		userLogin (context, identifiants) {
			return new Promise((resolve, reject) => {
				getAPI.post('/token/', {
					username: identifiants.username,
					password: identifiants.password
				}).then(response => {
					context.commit('updateStorage', {access: response.data.access, refresh: response.data.refresh})
					resolve()
				}).catch(err => {
					reject(err)
				})
			})
		},
		userLogout(context) {
			if (context.getters.loggedIn) {
				context.commit('destroyToken')
			}
		},
	},
	getters: {
		loggedIn (state) {
			return state.accessToken != null
		}
	}
})