<template>
  <div id="sign-up-block">
    <div>
    <input v-model="user.username" placeholder="请输入账号">
    </div>
    <div>
    <input type=password v-model="user.password" placeholder="请输入密码">
    </div>
    <div>
      <input type=password v-on:change="chekPasswordChange" v-model="checkPassword" placeholder="请确认密码">
    </div>
    <div>
    <button v-on:click="signUp">注册</button>
    </div>
    <div id="info">
    <p v-if="isOk">注册成功！<span v-on:click="htmlJmp"  id="jump">点击跳转</span></p>
    <p v-if="isRgs">注册失败，请检查用户名和密码是否为空!</p>
    <p v-if="checkFlag">密码不一致!请检查</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.baseURL = '/api';

export default {
  name: "sign-up",
  data (){
    return {
      user: {
        username: '',
        password: '',
      },
      isOk: false,
      isRgs: false,
      checkPassword: '',
      checkFlag: false,
    }
  },
  methods: {
    signUp(){
      if(this.chekPasswordFcn()) {
        this.checkFlag = false;
        axios.post("/signUp", {
          username: this.user.username,
          password: this.user.password,
        })
        .then(response => {
            if (response.data.code === 200) {
              console.log("Register Ok!");
              this.isOk = true;
              this.isRgs = false;
              setTimeout(() => this.htmlJmp(), 5000);
            }else{
              console.log("Register fail!");
              this.failRgs();
            }
          }
        )
        .catch(failResponse => {
          console.log(failResponse.status);
        })
      }else{
        this.checkFlag = true;
      }
    },
    htmlJmp(){
      this.$router.replace("/login");
    },
    failRgs(){
      this.user.password = '';
      this.user.username = '';
      this.isOk = false;
      this.isRgs = true;
      this.checkPassword =  '';
      this.checkFlag = false;
    },
    chekPasswordFcn(){
        console.log(this.checkPassword);
        console.log(this.user.password);
        console.log(this.checkPassword == this.user.password);
        return this.checkPassword == this.user.password;
    },
    chekPasswordChange(){
      if(this.chekPasswordFcn()){
        this.checkFlag = false;
      }else{
        this.checkFlag = true;
        this.isRgs = false;
        this.isOk = false;
      }
    },
  }
}
</script>

<style scoped>
  #info{
    height: 15px;
  }
  #jump{
    color: crimson;
  }
  #sign-up-block{
    display: grid;
    grid-template-rows: 1fr 1fr 1fr;
    grid-gap: 2%;
    position: relative;
    top: 30%;
    left: 35%;
    background: white;
    border: #ffffff 2px solid;
    border-radius: 6px;
    width: 25%;
    height: 23%;
    padding-top: 2%;
    padding-bottom: 2%;
  }
</style>