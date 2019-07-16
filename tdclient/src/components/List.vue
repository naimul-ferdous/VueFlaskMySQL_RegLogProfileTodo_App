<template>
    <div class="container" id="todo-list">
        <div class="row">
            <div class="col-md-6 mx-auto">
                <h1 class="text-center">TODO List</h1>
                <form @submit.prevent="addNewTask">
                    <label for="taskNameInput">Task Name</label>
                    <input v-model="taskname" type="text" class="form-control" id="taskNameInput" placeholder="Add New Task">
                    <button v-if="this.isEdit==false" type="submit" class="btn btn-success btn-block mt-3">Submit</button>
                    <button v-else @click="updateTask()" type="button" class="btn btn-primary btn-block mt-3">Update</button>
                </form>
                <table class="table">
                    <tr v-for="(todo) in todos" v-bind:key="todo.id" v-bind:title="todo.title">
                        <td class="text-left">{{todo.title}}</td>
                        <td class="text-right">
                            <button @click="editTask(todo.title,todo.id)" class="btn btn-info">Edit</button>
                            <button @click="deleteTask(todo.id)" class="btn btn-danger">Delete</button>
                        </td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            todos: [],
            id: '',
            taskname: '',
            isEdit: false
        }
    },
    mounted() {
        this.getTasks()
    },
    methods: {
        getTasks() {
            axios({method: 'GET', url: '/api/tasks'}).then(
                result=>{
                    console.log(result.data)
                    this.todos= result.data
                },
                eror=>{
                    console.log(error)
                } 
            )
        },
        addNewTask() {
            axios.post('/api/task', {
                title: this.taskname
            }).then(res=>{
                this.taskname=''
                this.getTasks()
                console.log(res)
            }).catch(err=>{
                console.log(err)
            })
        },
        editTask(title,id) {
            this.id=id
            this.taskname=title
            this.isEdit=true
        },
        updateTask() {
            axios.put(`/api/task/${this.id}`,
            {
                title: this.taskname
            }).then(res=>{
                this.taskname=''
                this.isEdit=false
                this.getTasks()
                console.log(res)
            }).catch(err=>{
                console.log(err)
            })
        },
        deleteTask(id) {
            axios.delete(`/api/task/${id}`).then(res=>{
                this.taskname=''
                this.getTasks()
                console.log(res)
            }).catch(err=>{
                console.log(err)
            })
        }
    }
}
</script>

