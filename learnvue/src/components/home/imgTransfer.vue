<template>
  <div id="back-block">
    <div id="log-out-bgd">
      <button id="log-out" v-on:click="logOut">Logout</button>
    </div>
    <div id="pst">
    <p id="logo">OCR Online!</p>
      <div id="select">
        <input v-on:change="fileChange" id="file" ref="fileElem"  type="file" accept="image/png, image/jpg">
        <span id="info">{{path}}</span><input v-on:click="upload" id="btn" type="button"><button v-on:click="infer" id="certain">识别</button>
      </div>
    </div>
    <div id="result-show" v-if="isResult">
      <div id="img-show">
        <img v-if="isShowImg" id="img" v-bind:src="src">
      </div>
      <div id="img-result-show">
        <p id="result-value" v-for="(text, index) in result" :key="index">{{index + 1}}.&#12288;{{text}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = 'api'

export default {
  name: "imgTransfer",
  data () {
    return {
        isResult: false,
        path: '',
        src: '',
        file: null,
        result: [],
        isShowImg: false,
    }
  },
  methods: {
    logOut(){
      this.$router.replace("/login")
    },
    infer(){
        let param = new FormData()
        param.append('img', this.file)
        let config = {
          headers: {'Content-Type': 'multipart/form-data'}
        }
        axios.post('/infer',param, config)
        .then(response => {
            if(response.data.code == 200){
              this.result = [];
              let tmp = response.data.value
              let tmp_array = tmp.split("\n")
              for(let t_value in tmp_array){
                  this.result.push(tmp_array[t_value])
              }
              this.result.pop()
            }else{
              this.result = "error! fail to infer!"
            }
        })
    },
    upload(){
      this.$refs.fileElem.click()
    },
    fileChange(){
      this.path = this.$refs.fileElem.files[0].name
      let newSrc = this.getObjectURL(this.$refs.fileElem.files[0])
      this.src = newSrc
      this.file = this.$refs.fileElem.files[0]
      this.isShowImg = true;
      this.isResult = true;
    },
    getObjectURL(file) {
      let url = null ;
      // 下面函数执行的效果是一样的，只是需要针对不同的浏览器执行不同的 js 函数而已
      if (window.createObjectURL!=undefined) { // basic
        url = window.createObjectURL(file) ;
      } else if (window.URL!=undefined) { // mozilla(firefox)
        url = window.URL.createObjectURL(file) ;
      } else if (window.webkitURL!=undefined) { // webkit or chrome
        url = window.webkitURL.createObjectURL(file) ;
      }
      return url ;
    },
  },
}
</script>

<style scoped>
  #log-out-bgd{
    padding-top: 1%;
  }
  #log-out{
    display: block;
    position: relative;
    left: 92%;
  }
  #result-value{
  }
  #certain{
    display: block;
    border: 1px solid;
    border-radius: 3px;
    background: rgba(245, 153, 119, 0.99);
  }
  #img{
    max-width: 100%;
    max-height: 100%;
  }
  #img-show{
    border: 1px solid;
  }
  #img-result-show{
    border: 1px solid;
    /*white-space: pre-wrap;*/
  }
  #result-show{
    position: relative;
    display: grid;
    grid-template-columns: 1fr 1fr;
    top: 12%;
    width: 100%;
    height: 40%;
  }
  #back-block{
    height: 100%;
    weight: 100%;
    background: rgb(255, 242, 226);
  }
  #img-result-show p{
    text-align: left;
    margin-left: 5%;
    margin-bottom: 0.7%;
    margin-top: 0;
  }
  #info{
    display: block;
    border: 1px solid;
    border-radius: 2px;
  }
  #btn{
    display: block;
    width: 28px;
    background: url("../../assets/file-icon4.jpg");
    border-radius: 2px;
  }
  #logo{
    border-radius: 2px;
    position: relative;
    left: 39%;
    width: 25%;
    display: block;
    background: #5c5c5c;
    font-size: 65px;
    color: rgb(255, 255, 255);
    text-shadow: 0 0 0.5em #0ae642, 0 0 0.2em #5c5c5c;
  }
  #pst{
    top: 10%;
    position: relative;
    border: 2px rgb(255, 242, 226) solid;
  }
  #file{
    display: none;
  }
  #select{
    height: 28px;
    width: 22%;
    display: grid;
    grid-template-columns: 8fr 1fr 2fr;
    position: relative;
    left: 40%;
  }
</style>