<template>
	<div class="nav-bar">
		<nav class="navbar navbar-expand-lg navbar-light bg-white nav-1">
			<div class="container mw-0 px-3">
				<a href="#" class="navbar-brand">
					<img src="../assets/logo.png" width="" height="27" class="d-inline-block align-top">
				</a>
				<div class="collapse navbar-collapse" id="navbarContent">
					<ul class="navbar-nav mr-auto">
						<li class="logout-btn nav-item" v-if="accessToken!=null"><router-link :to = "{ name:'logout' }">Logout</router-link></li>
					</ul>
				</div>
			</div>
		</nav>
	</div>
</template>

<script >
	import { mapState } from 'vuex'
	export default {
		name: 'Navbar',
		computed: mapState(['accessToken'])
	}
</script>

<style scoped>
	a {
		color:#000;
	}
</style>