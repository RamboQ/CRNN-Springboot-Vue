<template>
  <div id="log-in">
    用户名: <input type="text" v-model="loginForm.username" placeholder="请输入用户名">
    <br><br>
    <span>密　码: </span><input type="password" v-model="loginForm.password" placeholder="请输入密码">
    <br><br>
    <div id="sign">
    <button v-on:click="login" id="sign-in-btn">登录</button>
    <button v-on:click="signUp" id="sign-up-btn">注册</button>
    </div>
  </div>
</template>

<script>
import axios from "axios"
axios.defaults.baseURL='/api'

export default {
  name: "Login",
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      responseResult: []
    }
  },
  methods: {
    login() {
      axios.post('/login', {
          password: this.loginForm.password,
          username: this.loginForm.username,
      })
      .then(successResponse => {
        console.log(this.loginForm.password)
        if(successResponse.data.code === 200){
          this.$router.replace({path: '/infer'})
        }
      })
      .catch(failResponse => {
          console.log(failResponse.status);
      })
    },
    signUp(){
      console.log('sign-up');
      this.$router.replace({path: '/signUp'})
    }
  }
}
//console.log($axios);
</script>

<style scoped>
  #sign-up-btn{
    width: 80px;
  }
  #sign-in-btn{
    margin-right: 22%;
    width: 80px;
  }
  #sign{
    position: relative;
    width: 80%;
    left: 9.8%;
  }
  #log-in{
    position: relative;
    top: 30%;
    left: 35%;
    background: white;
    border: #ffffff 2px solid;
    border-radius: 6px;
    width: 25%;
    height: 20%;
    padding-top: 4%;
  }
</style>