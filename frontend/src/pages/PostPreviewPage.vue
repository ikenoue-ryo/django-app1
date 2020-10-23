<template>
  <v-app>
    <!-- <Spinner v-show="!loading" /> -->

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
        <div class="clearfix text-right edit_delete">
        <!-- モーダル -->
        <div class="inline_block" style="margin-right:15px;">
          <v-dialog
            v-model="dialog"
            width="500"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text
                color="red lighten-2"
                dark
                v-bind="attrs"
                v-on="on"
                @click="editButton"
              >
              <p class="">編集</p>
              </v-text>
            </template>
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

          </v-dialog>
        </div>
        <!-- モーダル -->

        <!-- モーダル -->
        <div class="inline_block">
          <v-dialog
            v-model="dialog2"
            width="500"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text
                color="red lighten-2"
                dark
                v-bind="attrs"
                v-on="on"
              >
              <p class="">削除</p>
              </v-text>
            </template>
              <v-card
                class="card_style"
                max-width="800"
              >
              <v-btn @click="deleteButton">
                削除
              </v-btn>
              </v-card>

          </v-dialog>
        </div>
        <!-- モーダル -->
        </div>



        <div style="width:700px;">
          <p>{{ post.title }}</p>
          <p>{{ post.car_type }}</p>
          <p>{{ post.price }}円</p>
          <div v-html="post.text" class="post_text"></div>
        </div>

        <v-layout wrap class="profile">
          <v-flex xs12 sm6 md2>
            <div class="icon">
              <router-link :to="`/profile/${username}`">
                <img :src="user_profile.icon">
              </router-link>
            </div>
          </v-flex>
          <v-flex xs12 sm6 md10>
            <div class="pr_profile">
              <p class="prof_name">{{ user_profile.userpro.username }}</p>
              <p>{{ user_profile.introduction }}</p>
            </div>
          </v-flex>
        </v-layout>



      </v-card>

    </div>
    <PrFooter/>

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

// import Spinner from 'vue-simple-spinner'

export default {
  components: {
    GlobalHeader,
    PrFooter,
    quillEditor,
    // Spinner,
  },
  data(){
    return{
      // loading: true,

      dialog: false,
      dialog2: false,
      results: [],
      profiles: [],
      form: {
        posts: {
          title: '',
          text: '',
          car_type: '',
          price: ''
        },
      }
    }
  },
  mounted(){
    axios.get('http://127.0.0.1:8000/api/v1/posts/')
    .then(response => {
      this.results = response.data;
    })

    axios.get('http://localhost:8000/api/v1/profile/')
    .then(response => {
      this.profiles = response.data;
    })
  },
  methods: {
    submitPost: function(){
      api({
        method: 'put',
        url: '/posts/' + this.id + '/',
        data: {
          'id': this.form.posts.id,
          'author': this.$store.getters['auth/id'],
          'car_type': this.form.posts.car_type,
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
    },
    // 編集ボタンでインスタンスを挿入
    editButton(){
      this.form.posts = this.post
    },
    // 削除ボタン
    deleteButton(){
      api({
        method: 'delete',
        url: `/posts/${this.post.id}`,
      })
      .then(response => {
        console.log(response);
        const next = this.$route.query.next || `/profile/${this.username}`
        this.$router.replace(next)
      })
      .catch(error => {
        console.log(error);
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
    },
    user_profile(){
      const profiles = this.profiles.find(profiles => profiles.userpro.id === this.post.author.id)
      if(!profiles){
        return {
          title: '見つかりません',
          text: '見つかりません',
        }
      }
      return profiles
    },
    user_posts(){
      const posts = this.posts.filter(posts => posts.author === this.$store.getters['auth/id']);
      return posts
    },

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

.clearfix::after {
   content: "";
   display: block;
   clear: both;
}
</style>



<style lang="scss" scoped>
.clearfix::after {
   content: "";
   display: block;
   clear: both;
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
    display: inline-block;
    float: left;
    position: relative;
    right: 70px;

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
  top: 50px;
  right: 80px;

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


.profile{
  border: solid 2px #dce4ec;
  padding: 40px;
  border-radius: 10px;
  background: #eee;
  margin: 50px 0;
  
  .icon{
    width: 80px;
    display: inline-block;
    float: left;
    height: 130px;
  }

  img{
    width: 70px;
    border-radius: 50%;
    border: 1px solid grey;
  }

  .pr_profile{
    p.prof_name {
      font-size: 1.2rem;
      font-weight: 600;
    }

    p{
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
      overflow: hidden;
    }
  }

  p{
    margin-bottom: 5px;
    line-height: 1.6;
    font-size: 1.1rem;
  }
}

.edit_delete{
  width: 100%;
  display: inline-block;

  .inline_block{
    display: inline-block;
  }
}
</style>