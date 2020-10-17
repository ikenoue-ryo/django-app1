<template>
  <v-app>
    <div id="app" class="back_body">
      <GlobalHeader />

      <h2>Post Preview</h2>

      <div class="sns_photo">
        <!-- SNSアイコン -->
        <div class="sns_back clearfix">
          <div class="sns_icons">
            <v-fa :icon="['fab', 'facebook']" class="fb_icon" />
            <v-fa :icon="['fab', 'twitter']"  class="tw_icon" />
            <v-fa :icon="['fab', 'instagram']" class="ig_icon" />
            <v-fa :icon="['fab', 'linkedin']" class="li_icon" />
            <v-fa :icon="['fab', 'pinterest']" class="pi_icon" />
          </div>
        </div>
        <!-- SNSアイコン -->
      </div>

      <v-card
        class="card_style"
        max-width="800"
      >
        <div>
          <div v-html="post.text" class="post_text"></div>
        </div>

        <v-layout wrap class="profile">
          <v-flex xs12 sm6 md2>
            <div class="icon">
              <img src="">
            </div>
          </v-flex>
          <v-flex xs12 sm6 md10>
            <div class="pr_profile">
              <p class="prof_name">{{ username }}</p>
              <p></p>
            </div>
          </v-flex>
        </v-layout>

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
  },
  computed: {
    user_id() {
      console.log('ログインユーザーID', this.$store.getters['auth/id'])
      return this.$store.getters['auth/id']
    },
    username(){
      return this.$store.getters['auth/username']
    },
    id(){
      console.log('投稿ID', this.$route.params.id)
      return Number(this.$route.params.id);
    },
    post(){
      const post = this.results.find(results => results.id === this.id);
      return post
    }

  }
};
</script>


<style>
/* エディタ専用のCSS(SCSSが効かない) */
p{
    font-size: 1.2rem;
    font-family: Rubik, -apple-system, "Hiragino Sans", "Hiragino Kaku Gothic ProN", BlinkMacSystemFont, YuGothic, "Yu Gothic", sans-serif;
    line-height: 2.0;
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
  line-height: 2.5;
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

.sns_back {
  display: inline-block;
  float: left;
}


.sns_photo{
  width: 780px;
  margin: 0 auto;

  .blog_text{
    font-size: 1.2rem;
    padding: 20px;

    h2{
      font-size: 1.4rem;
      font-weight: 600;
      text-align: left;
      margin: 20px 0;
    }

    img{
      width: 100%;
      margin-bottom: 20px;
      border-radius: 10px;
    }

    ul{
      line-height: 2.5;
    }

    p{
      line-height: 2;
    }
  }
}



.sns_back .sns_icons {
  font-size: 2.5rem;
  width: 50px;
  display: inline-block;
  float: left;
  position: relative;
  right: 90px;

  .fb_icon{
    color: #3b5998;
  }
  .tw_icon{
    color: #2196f3;
  }
  .ig_icon{
    color: #e91e63;
  }
  .li_icon{
    color: #2867B2;
  }
  .pi_icon{
    color: #f44336;
  }
}

</style>