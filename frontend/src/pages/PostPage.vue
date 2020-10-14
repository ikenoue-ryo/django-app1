<template>
  <div id="app" class="back_body">
    <GlobalHeader />

    <h2>Let's Post</h2>
    <v-card
      class="card_style"
      max-width="800"
    >

    <form @submit.prevent="submitSave" class="form_class">
      <quillEditor v-model="form.posts.text" style="border: 1px solid;"/>
      <button type="submit">送信</button>
    </form>

    </v-card>
    <PrFooter/>
  </div>
</template>

<script>
import api from '@/services/api'
import GlobalHeader from '../components/GlobalHeader'
import PrFooter from '../components/PrFooter'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

import { quillEditor } from 'vue-quill-editor'
// import axios from 'axios'

export default {
  components: {
    GlobalHeader,
    PrFooter,
    quillEditor
  },
  data(){
    return{
      form: {
        posts: {
          title: '',
          text: '',
        }
      }
    }
  },
  // mounted(){
  //   axios.get('http://127.0.0.1:8000/api/v1/posts/')
  //   .then(response => {this.results = response.data})
  // },
  methods: {
    submitSave: function(){
      api({
        method: 'post',
        url: '/posts/',
        data: {
          'id': this.form.posts.id,
          'title': this.form.posts.title,
          'text': this.form.posts.text,
        }
      })
        .then(response => {
          this.form.posts = response.data
        })
    }
  }
};
</script>


<style>
/* エディタ専用のCSS(SCSSが効かない) */
.ql-editor p{
  font-size: 20px;
}

.ql-editor ::placeholder{
  color: orange;
}

.ql-container{
  border: none!important;
}
</style>



<style lang="scss" scoped>
p{
  font-size: 1.2rem;
  font-family: Rubik, -apple-system, "Hiragino Sans", "Hiragino Kaku Gothic ProN", BlinkMacSystemFont, YuGothic, "Yu Gothic", sans-serif;
}

.back_body{
  background-color: #eee;
  overflow: hidden;
  

  h2{
    text-align: center;
    font-size: 45px;
    font-weight: 600;
    text-align: center;
    margin: 30px;
  }

  .card_style{
    margin: 30px auto;
    padding: 50px;
    border-top: 5px solid #33b5e5;
    min-height: 100vh;

    .back-color{
      a.start{
        background-color: #329eff!important;
        font-size: 0.9rem;
        color: #fff;
        font-weight: bold;
        margin-top: 20px;
        padding: 20px;
      }
    }
  }

  .image_area{
    margin-bottom: 20px;

    img{
      width: 700px;
      height: 400px;
      object-fit: contain;
    }
  }
}


.v-input{
  font-size: 3rem;
}
</style>