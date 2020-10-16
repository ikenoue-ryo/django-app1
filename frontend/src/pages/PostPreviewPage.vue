<template>
  <v-app>
    <div id="app" class="back_body">
      <GlobalHeader />

      <h2>Post Preview</h2>
      {{ results }}
      <v-card
        class="card_style"
        max-width="800"
      >
      <div>
        <div v-for="result in results" :key="result">
          <div v-html="result.text" class="post_text"></div>
        </div>
      </div>
      </v-card>

      <!-- <v-layout wrap class="profile" v-for="(user, index) in post.user_info" :key="index">
        <v-flex xs12 sm6 md2>
          <div class="icon">
            <img :src="user.icon">
          </div>
        </v-flex>
        <v-flex xs12 sm6 md10>
          <div class="pr_profile">
            <p class="prof_name">{{ user.name }}</p>
            <p>{{ user.pr }}</p>
          </div>
        </v-flex>
      </v-layout> -->

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

import axios from 'axios'

export default {
  components: {
    GlobalHeader,
    PrFooter,
  },
  data(){
    return{
      results: [],
      form: {
        posts: {
          title: '',
          text: '',
        }
      }
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
          'title': this.form.posts.title,
          'text': this.form.posts.text,
        }
      })
        .then(response => {
          this.form.posts = response.data
          console.log('Post succeeded.')
          this.$store.dispatch('message/setInfoMessage', { message: '投稿しました。' })
          const next = this.$route.query.next || '/'
          this.$router.replace(next)
        })
    }
  }
};
</script>


<style>
/* エディタ専用のCSS(SCSSが効かない) */
p{
    font-size: 1.2rem;
    font-family: Rubik, -apple-system, "Hiragino Sans", "Hiragino Kaku Gothic ProN", BlinkMacSystemFont, YuGothic, "Yu Gothic", sans-serif;
  }

img{
    width: 100%;
    border-radius: 10px;
  }

ul{
  font-size: 1.2rem;
}

li{
  font-size: 1.2rem;
  font-family: Rubik, -apple-system, "Hiragino Sans", "Hiragino Kaku Gothic ProN", BlinkMacSystemFont, YuGothic, "Yu Gothic", sans-serif;
  line-height: 1.5;
}

h1{
  font-size: 1.7rem;
  font-weight: 600;
}

h2{
  font-size: 1.5rem;
  font-weight: 600;
}

h3{
  font-size: 1.3rem;
  font-weight: 600;
}
</style>



<style lang="scss" scoped>


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
}


.v-input{
  font-size: 3rem;
}
</style>