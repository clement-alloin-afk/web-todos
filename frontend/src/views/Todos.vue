<template>
	<div class="todos">
		<Navbar></Navbar>
		<div class="container py-5 bg-light">
			<div class="newTodo">
				<h1>New Todo</h1>
				<form action="" method="post" @submit.prevent="submitForm">
					<p v-if="error">
						<b>Champs vide</b>
					</p>
					<input placeholder="Test" id="todoValue" type="text" name="newTodoValue">
                    <input class="button" type="submit" value="Ajouter">
				</form>
			</div>
			<div class="todoList">
				<div v-for="todos in APIData" :key="todos.uuid" class="col-md-4">
					<p class="todos-value">{{todos.value}}</p>
				</div>
				
			</div>
		</div>
	</div>
</template>

<script>
	import { getAPI } from '../axios-api'
	import Navbar from '../components/Navbar'
	import { mapState } from 'vuex'
	export default {
		name: 'Todos',
		data() {
			return {
				error: false
			}
		},
		components: {
			Navbar
		},
		computed: mapState(['APIData']),
		created () {
			getAPI.get('/todos/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
				.then(response => {
					console.log('Receiving data')
					this.$store.state.APIData = response.data
					console.log(response.data)
				})
				.catch(err => {
					console.log(err) 
				})
		},
		methods: {
			submitForm(){
                console.log("owner : "+this.$)
                if(! this.newTodoValue){
                    this.error = true
                    return
                }
			}
		},
	}
</script>

<style scoped>
	

</style>