<template>
<div>
<button type=”button” name=”button” @click='getUsers'>get users</button>
<table>
 <th>url</th>
 <th>email</th>
 <th>staff</th>
 <tbody>
 <tr v-for="elem in users" :key="elem.key">
 <td><a :href="elem.url">{{elem.username}}</a></td>
 <td>{{elem.email}}</td>
 <td>{{elem.is_staff}}</td>
 </tr>
 </tbody>
</table>
</div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      users: []
    };
  },
  methods: {
    getUsers() {
      axios
        .get("http://127.0.0.1:8000/users/")
        .then(res => (this.users = res.data))
        .catch(error => console.log(error));
    }
  }
};
</script>
<style lang="scss" >
</style>