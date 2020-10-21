<template>
<v-app>
  <div id="app" class="back_body">
    <GlobalHeader />

    <h2>Let's Post</h2>
    <v-card
      class="card_style"
      max-width="800"
    >

    
      <form @submit.prevent="submitPost" class="form_class">

        <v-checkbox v-model="form.posts.car_type" label="カローラ" color="info" value="corolla" hide-details></v-checkbox>
        <v-checkbox v-model="form.posts.car_type" label="プリウス" color="info" value="prius" hide-details></v-checkbox>
        <v-checkbox v-model="form.posts.car_type" label="ヴォクシー" color="info" value="voxy" hide-details></v-checkbox>

        <quillEditor v-model="form.posts.text" style="border: 1px solid;"/>
        <button type="submit">送信</button>
      </form>
    </v-card>

    <PrFooter/>
  </div>

  </v-app>
</template>

<script>
import api from '@/services/api'
import GlobalHeader from '../components/GlobalHeader'
import PrFooter from '../components/PrFooter'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

import { quillEditor } from 'vue-quill-editor'
import axios from 'axios'

export default {
  components: {
    GlobalHeader,
    PrFooter,
    quillEditor
  },
  data(){
    return{
      results: [],
      form: {
        posts: {
          author: '',
          title: '',
          text: '',
          price: '',
        }
      },
      ex4: ['info'],
    }
  },
  mounted(){
    axios.get('http://127.0.0.1:8000/api/v1/posts/')
    .then(response => {this.results = response.data})
  },
  methods: {
    submitPost: function(){
      api({
        method: 'post',
        url: '/posts/',
        data: {
          'id': this.form.posts.id,
          'author': this.$store.getters['auth/id'],
          'title': this.form.posts.title,
          'text': this.form.posts.text,
          'car_type': this.form.posts.car_type,
        }
      })
        .then(response => {
          this.form.posts = response.data
          console.log(this.form.posts)
          console.log('Post succeeded.')
          this.$store.dispatch('message/setInfoMessage', { message: '投稿しました。' })
          const next = this.$route.query.next || 'post_preview/' + this.form.posts.id
          this.$router.replace(next)
        })
    }
  },
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

.ql-snow .ql-editor h2 {
  font-size: 1.6rem;
}

.ql-editor ol, .ql-editor ul {
  padding-left: 0;
  font-size: 1.4rem;
  line-height: 2.5;
}

img{
  margin: 20px 0;
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

input[type="checkbox"] {
        display: none;
    }

    label {
        display: inline-block;
        border-radius: 20px;
        text-align: center;
        text-decoration: none;
        border: solid 1px #ccc;
        transition: 0.25s;
        padding: 6px 18px;
        cursor: pointer;
        font-size: 14px;
        margin: 3px;
    }

    input[type="checkbox"]:checked + label {
        background: #00809d;
        color: #fff;
    }

</style>