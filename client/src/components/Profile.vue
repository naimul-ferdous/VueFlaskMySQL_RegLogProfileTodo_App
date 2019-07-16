<template>
    <div class="container" id="profile">
        <div class="jumbotron mt-5">
            <div class="col-sm-8 mx-auto">
                <h1 class="text-center">Profile</h1>
            </div>
        </div>
        <table class="table col-md-6 mx-auto">
            <tbody>
                <tr>
                    <td>First Name</td>
                    <td>{{first_name}}</td>
                </tr>
                <tr>
                    <td>Last Name</td>
                    <td>{{last_name}}</td>
                </tr>
                <tr>
                    <td>Email</td>
                    <td>{{email}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
// eslint-disable-next-line
/* eslint-disable */
import jwtDecode from 'jwt-decode'
export default {
  data () {
    const token = localStorage.userToken
    const decoded = jwtDecode(token)
    return {
      first_name: decoded.identity.first_name,
      last_name: decoded.identity.last_name,
      email: decoded.identity.email
    }
  }
}
</script>
