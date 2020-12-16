<template>
	<div class="todos">
		<Navbar></Navbar>
		<div class="container py-3 bg-light">
			<section>
				<div class="row justify-content-center mt-4">
					<form action="" method="post" v-on:submit.prevent="addNewTodo">
						<input v-model="newTodo" class="input-value mr-1" placeholder="Description" />
						<input class="button" type="submit" value="Ajouter">
						<p v-if="champsVide">Champs vide !</p>
					</form>
				</div>
			</section>
			<ul class="todo-list">
				<li v-for="todo in APIData" class="todo" :key="todo.uuid">
					<div class="row align-items-center">
						<del v-if="todo.checked" class="col-sm-8">
							<input class="checkbox m-4" type="checkbox" v-on:click.prevent="check(todo)" checked>
							{{ todo.value }}
						</del>
						<span v-else class="col-sm-8">
							<input class="checkbox m-4" type="checkbox" v-on:click.prevent="check(todo)" >
							{{ todo.value }}
						</span>
						<button v-on:click.prevent="deleteTodo(todo)" type="button" class="btn-delete btn-secondary btn-sm">X</button>
					</div>
				</li>
			</ul>
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
				champsVide: false,
				newTodo: null
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
			addNewTodo(){
				if(this.newTodo){
					getAPI.post('/todos/',
						{ value: this.newTodo,checked: false },
						{ headers: {Authorization: 'Bearer ' + this.$store.state.accessToken } },
					)
					.then(response => {
						let newTodo = response.data
						this.APIData.push(newTodo)
						this.newTodo = null
					})
					this.champsVide = false
				}
				else {
					this.champsVide = true
				}
			},
			deleteTodo (todo) {
				getAPI.delete('/todo/'+todo.uuid+'/',
					{ headers: {Authorization: 'Bearer ' + this.$store.state.accessToken}},
				);
				this.APIData.splice(this.APIData.indexOf(todo), 1)
			},
			check(todo) {
				console.log("allooo")
				todo.checked = !todo.checked;
				console.log(todo.checked)
				getAPI.patch('/todo/'+todo.uuid+'/',
					{ value: todo.value , checked: todo.checked },
					{ headers: {Authorization: 'Bearer ' + this.$store.state.accessToken}},
				);
			}
		},
	}
</script>

<style scoped>
	
	.todo-list {
		margin: 20px 30px ;
		margin-left: 200px ;
		justify-content: center ;
		list-style: none;
	}
	.todo-list li {
		font-size: 28px;
	}
</style>


