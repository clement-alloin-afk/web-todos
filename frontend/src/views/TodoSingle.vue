<template >
	<div class="todos">
		<Navbar></Navbar>
		<div class="container py-3 bg-light">
			<section>
				<div class="row justify-content-center mt-4">
					<form action="" method="post" v-on:submit.prevent="addDescr">
						<input v-model="newDescri" class="input-value mr-1" placeholder="Description" />
						<input class="button" type="submit" value="Ajouter">
						<p v-if="champsVide">Champs vide !</p>
					</form>
				</div>
			</section>
			<ul class="todo-list">
				<li class="todo" >
					<div class="row align-items-center">
						<del v-if="todo.checked" class="col-sm-8">
							<input class="checkbox m-4" type="checkbox" v-on:click.prevent="check()" checked>
							{{ todo.value }}
						</del>
						<span v-else class="col-sm-8">
							<input class="checkbox m-4" type="checkbox" v-on:click.prevent="check()" >
							{{ todo.value }}
						</span>
						<button v-on:click.prevent="deleteTodo()" type="button" class="btn-delete btn-secondary btn-sm">X</button>
					</div>
				</li>
				<li v-for="(descr,index) in todo.descriptions" :key="index" class="descriptionListe m-2">
					<div class="description">{{ descr.description }}</div>
					<div class="date ">{{ format_date(descr.update_date) }}</div>
				</li>
			</ul>
			<button v-on:click.prevent="back" type="button" class="btn-back btn-info btn-sm">Go Back</button>
		</div>
	</div>
</template>

<script >
	import { getAPI } from '../axios-api'
	import Navbar from '../components/Navbar'
	import moment from 'moment'
	export default {
		data() {
			return {
				todo: null,
				newDescri: null,
				champsVide: false
			}
		},
		components: {
			Navbar
		},
		created() {
			this.todo = ('Params: ', this.$route.params).todo ;
			this.todo.descriptions.reverse() ;
		},
		methods: {
			format_date(value){
				if (value) {
					return moment(String(value)).format('DD/MM/YYYY hh:mm')
					}
				},
			addDescr(){
					if(this.newDescri){
						getAPI.patch('/todo/'+this.todo.uuid+'/',
							{ value: this.todo.value , descriptions : [{description : this.newDescri}]},
							{ headers: {Authorization: 'Bearer ' + this.$store.state.accessToken } },
						)
						.then(response => {
							this.todo = response.data
							this.newDescri = null
							this.todo.descriptions.reverse() ;
						})
						
						this.champsVide = false
					}
					else {
						this.champsVide = true
					}
				},
			deleteTodo () {
				getAPI.delete('/todo/'+this.todo.uuid+'/',
					{ headers: {Authorization: 'Bearer ' + this.$store.state.accessToken}},
				);
				this.$router.push({ name: 'todos' })
			},
			check() {
				this.todo.checked = !this.todo.checked;
				getAPI.patch('/todo/'+this.todo.uuid+'/',
					{ value: this.todo.value , checked: this.todo.checked },
					{ headers: {Authorization: 'Bearer ' + this.$store.state.accessToken}},
				);
			},
			back(){
				this.$router.push({ name: 'todos' })
			}
		}
	}
</script>



Vue.filter('formatDate', function(value) {
    if (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
    }
});

<style scoped>
	
	.todo-list {
		margin: 20px 30px ;	
		justify-content: center ;
		list-style: none;
		font-size: 32px;
	}
	.todo {
		margin-left: 200px ;
	}

	.description {
		font-size: 24px;
		margin-left: 10px ;
	}

	.date {
		font-size: 16px;
		margin-right: 15px ;
		display: flex ;
		justify-content: flex-end;
	}

	.descriptionListe {
		border-radius: 5px;
		border-style: solid;
		border-width: 1px ;
		background-color: #E8FEFD; 
	}

	.container{
		border-style: solid;
		border-width: 1px ;
		border-radius: 80px ;
		background-image: linear-gradient(to bottom right, #A6EAE6,#C1F9B5);
	}
	.btn-back {
		margin-left: 30px ;
	}
</style>