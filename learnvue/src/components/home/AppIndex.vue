<template>
  <div id="index">
    <p>hello world!</p>
    <button v-on:click="logOut">退出</button>
  </div>
</template>

<script>
export default {
  name: "AppIndex",
  methods: {
    logOut(){
      this.$router.replace("/");
    }
  }
}
</script>

<style scoped>
  #index{
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