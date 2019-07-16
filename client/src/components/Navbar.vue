<template>
    <div id="navbar">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark rounded">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar1" aria-controls="navbar" aria-expanded="false" aria-label="Togle Navigation">
                <span class="navbar-toggle-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-md-center" id="navbar1">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link class="nav-link" to="/">Home</router-link>
                    </li>
                    <li v-if="auth==''" class="nav-item">
                        <router-link class="nav-link" to="/login">Login</router-link>
                    </li>
                    <li v-if="auth==''" class="nav-item">
                        <router-link class="nav-link" to="/register">Register</router-link>
                    </li>
                    <li v-if="auth=='loggedin'" class="nav-item">
                        <router-link class="nav-link" to="/profile">Profile</router-link>
                    </li>
                    <li v-if="auth=='loggedin'" class="nav-item">
                        <a class="nav-link" href="" @click="logout()">Logout</a>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
// eslint-disable-next-line
/* eslint-disable */
    import EventBus from './EventBus'
    EventBus.$on('logged-in', test=>{
        console.log(test)
    })
    export default {
        data() {
            return {
                auth: '',
                user: ''
            }
        },
        methods: {
            logout() {
                localStorage.removeItem('userToken')
            }
        },
        mounted() {
            EventBus.$on('logged-in', status=>{
                this.auth=status
            }
        )
    }
}
</script>
