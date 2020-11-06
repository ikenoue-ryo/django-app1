<template>
  <v-app>
    <!-- <Spinner v-show="!loading" /> -->
    <div id="app" class="back_body">
      <GlobalHeader />

      <h2>Ride</h2>
      
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
      >
      <notFound v-if="notFound" />
      <template v-else>

        <div class="clearfix text-right edit_delete">
        <!-- モーダル -->
        <div class="inline_block" style="margin-right:15px;">
          <v-dialog
            v-model="dialog"
            class="inner_card edit_form"
          >
            <template v-slot:activator="{ on, attrs }">
              <div
                color="red lighten-2"
                dark
                v-bind="attrs"
                v-on="on"
                @click="editButton"
              >
              <p class="">編集</p>
              </div>
            </template>
              <v-card
                class="card_style card_edit"
              >
                <form @submit.prevent="submitPost" class="form_class">

                  <!-- カーセレクト -->
                  <v-col
                    class="d-flex pa-0"
                    cols="12"
                    sm="6"
                  >
                    <v-select
                      v-model="form.posts.car_type"
                      :items="car_types"
                      label="Car Select"
                      outlined
                      style="font-size:16px;"
                      item-value="types"
                      item-text="name"
                    ></v-select>
                  </v-col>

                  <!-- サムネイル画像 -->
                  <v-flex xs12 sm6 md12 class="inner_card">
                    <v-container>
                      <v-row>
                        <div xs12 sm6 md3 xs3 class="photo_area">
                          <div class="file_input" v-show="show">
                            <label class="input-item__label">
                              <v-fa :icon="['fas', 'camera']" class="camera_icon sns_icons" />
                              <input type="file" name="file" ref="preview" @change="selectedFile">
                            </label>
                          </div>

                          <div class="image_area" v-if="url">
                            <div @click="deletePreview"><v-icon color="white">mdi-close</v-icon></div>
                            <img :src="url">
                          </div>
                        </div>

                      </v-row>
                    </v-container>
                  </v-flex>


                  <quillEditor v-model="form.posts.text" style="border: 1px solid;"/>
                  <div class="back-color">
                    <button type="submit" class="start">保存</button>
                  </div>
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
              <div
                color="red lighten-2"
                dark
                v-bind="attrs"
                v-on="on"
              >
              <p class="">削除</p>
              </div>
            </template>
              <v-card
                class="card_style delete_area"
              >
                <v-row>
                  <div class="delete_question">
                    この投稿を削除しますか？
                  </div>
                </v-row>
                <v-row justify="center" style="padding-bottom:30px;">
                  <v-btn @click="dialog2 = false" class="mr-5" text color="black" elevation="2" outlined raised>
                    キャンセル
                  </v-btn>
                  <v-btn @click="deleteButton" width="110" text color="black" elevation="2" outlined raised>
                    削除
                  </v-btn>
                </v-row>
              </v-card>

          </v-dialog>
        </div>
        <!-- モーダル -->
        </div>

        <div class="post_contents">
          <p>{{ post.car_type }}</p>
          <div v-html="post.text" class="post_text"></div>
          <ul>
            <v-row>
              <router-link :to="`/profile/${username}`">
                <li v-for="tags in post.tag" :key="tags" class="float-left">
                  #{{ tags.name }}
                </li>
              </router-link>
            </v-row>
          </ul>
        </div>

        <v-layout wrap class="profile">
          <v-flex sm6 md2 xs3>
            <div class="icon">
              <router-link :to="`/profile/${username}`">
                <img :src="user_profile.icon">
              </router-link>
            </div>
          </v-flex>
          <v-flex sm6 md10 xs9 class="text_left">
            <div class="pr_profile">
              <p class="prof_name" v-if="user_profile">{{ user_profile.userpro.username }}</p>
              <p>{{ user_profile.introduction }}</p>
            </div>
          </v-flex>
        </v-layout>

        <div class="share_price">
          <div class="card">
            <div class="card-body">
              <div v-if="post.price" class="price">
                {{ post.price.toLocaleString() }}
                <span class="yen"> 円/(月額)</span>
              </div>
              <p class="card-text">指定の場所に返却してください。</p>
              <!-- モーダル -->
                <div class="text-center">
                  <v-dialog
                    v-model="dialog3"
                    width="600"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <div
                        color="red lighten-2"
                        dark
                        v-bind="attrs"
                        v-on="on"
                        @click="editButton"
                      >

                      <v-btn color="#2bbbad">予約する</v-btn>
                      </div>
                    </template>

                  <v-card
                    class="card_style card_preview"
                  >
                    <!-- <GlobalMessage class="message_card" /> -->

                    <form @submit.prevent="submitBooking">
                      <v-flex xs12 sm6 md9 xs9 class="inner_card">
                        <v-container>
                          <v-row>

                            <!-- 日付 -->
                            <v-row>
                              <v-col
                                cols="12"
                                sm="12"
                              >
                                <v-date-picker
                                  width=100%
                                  no-title
                                  v-model="dates"
                                  range
                                ></v-date-picker>
                              </v-col>
                            </v-row>
                            <v-row class="px-3">
                              <v-col
                                cols="12"
                                sm="12"
                              >
                                <div-field
                                  v-model="dateRangeText"
                                  label="Date range"
                                  prepend-icon="mdi-calendar"
                                  readonly
                                ></div-field>
                                model: {{ dates }}
                              </v-col>
                            </v-row>
                            <!-- 日付 -->

                          </v-row>
                          <div class="back-color">
                              <button type="submit" color="#2bbbad">予約する</button>
                          </div>
                        </v-container>
                      </v-flex>
                    </form>
                  </v-card>
                </v-dialog>
              </div>
              <!-- モーダル -->

            </div>
          </div>
        </div>
        </template>
      </v-card>
    </div>
    <PrFooter/>

  </v-app>
</template>

<script>
import api from '@/services/api'
import GlobalHeader from '../components/GlobalHeader'
import PrFooter from '../components/PrFooter'
import notFound from '../pages/notFound'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

import { quillEditor } from 'vue-quill-editor'
import axios from 'axios'
import store from '../store'

// import Spinner from 'vue-simple-spinner'

export default {
  components: {
    GlobalHeader,
    PrFooter,
    quillEditor,
    notFound,
    // Spinner,
  },
  beforeRouteEnter(to, from, next) {
    axios.get(`http://127.0.0.1:8000/api/v1/posts/${to.params.id}/`)
      .then(res => {
        store.commit('window/setNotFound', false)
        console.log('レスポンス1', res)
        next()
      })
      .catch(err => {
        if (err.response.status === 404) {
          store.commit('window/setNotFound', true)
          console.log('エラー1', err)
          next()
        } else {
          next()
        }
      })
    },
  beforeRouteUpdate(to, from, next) {
    axios.get(`http://127.0.0.1:8000/api/v1/posts/${to.params.id}/`)
      .then(res => {
        store.commit('window/setNotFound', true)
        console.log('レスポンス2', res)
        next()
      })
      .catch(err => {
        if (err.response.status === 404) {
            store.commit('window/setNotFound', true)
            console.log('エラー2', err)
            next()
        } else {
            next()
        }
      })
  },

  data(){
    return{
      // loading: true,

      car_types: [
        {name: 'カローラ', types: 'corolla'},
        {name: 'プリウス', types: 'prius'},
        {name: 'ヴォクシー',types: 'voxy'},
        {name: 'シエンタ', types: 'sienta'},
        {name: 'アクア', types: 'aqua'},
        {name: 'アルファード', types: 'alphard'},
      ],

      dialog: false,
      dialog2: false,
      dialog3: false,
      results: [],
      profiles: [],
      form: {
        posts: {
          text: '',
          car_type: '',
          price: ''
        },
      },

      //写真アップロード
      uploadFile: null,
      icon: '',
      url: '',
      show: true,

      //日付フォーマット
      dates: [],
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
          'author': {
            'id': this.$store.getters['auth/id'],
            'username': this.$store.getters['auth/username'],
          },
          'car_type': this.form.posts.car_type,
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

    // 予約
    submitBooking(){
      api({
        credentials: "include",
        method: 'post',
        url: 'http://127.0.0.1:8000/app/booking/',
        headers: {
          'X-CSRFToken': this.$csrfToken,
        },
      })
      .then(() => {
        console.log('予約送信！')
      })
    },

    // 写真アップロード
    selectedFile: function(e){
      e.preventDefault();
      let files = e.target.files;
      this.uploadFile = files[0];
      console.log('uploadFile', this.uploadFile)

      const file = this.$refs.preview.files[0];
      this.url = URL.createObjectURL(file);
      this.$refs.preview.value = '';
      // 画像のアップ時にfileinputを消す
      this.show = !this.show
    },
    deletePreview(){
      this.url = '';
      // ファイルアップロードの復活
      this.show = !this.show
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
    },
  },
  computed: {
    notFound() {
      return this.$store.getters['window/isNotFound']
    },

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
      if(!post){
        return {
          text: '見つかりません',
        }
      }
      return post
    },
    user_profile(){
      const profiles = this.profiles.find(profiles => profiles.userpro.id === this.$store.getters['auth/id'])
      if(!profiles){
        return {
          text: '見つかりません',
        }
      }
      return profiles
    },
    user_posts(){
      const posts = this.posts.filter(posts => posts.author === this.$store.getters['auth/id']);
      return posts
    },
    dateRangeText(){
      return this.dates.join(' ~ ')
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

label > input {
  display: none;
}

label {
  padding: 0 1rem;
} 

label::after {
  font-size: 1rem;
  color: #888;
  padding-left: 1rem;
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

.div-field input {
    font-size: 1.2em;
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
  height: 0;

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

.share_price {
  background-color: #f5f5f5;
  margin: 36px;

  p.card-text{
    font-size: 1rem;
  }

  .card {
    // width: 230px;
    border-radius: 15px;
    position: fixed;
    // bottom: 30px;
    // right: 110px;
    // z-index: 10;
    padding: 5px;
    border: 1px solid #eee;
    background: #fff;
    box-shadow: 0 2px 5px 0 rgba(0,0,0,0.16), 0 2px 10px 0 rgba(0,0,0,0.12);
  }

  .card-body{
    .price{
      font-size: 1.4rem;      
    }

    .v-btn{
      background: #2bbbad;
      color: #fff;
      font-size: 1rem;
      padding: 10px;
      width: 100%;
      outline: none;
    }

    a{
      text-decoration: none;
    }
  }

  .price {
    font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto, "Helvetica Neue", sans-serif !important;
    font-size: 1.2rem;
    font-weight: 500;
    margin-bottom: 10px;
  }

  .price span.yen {
    font-size: 0.9rem;
  }
}

.form_class{
  padding: 25px 50px;
}

form{
  border-radius: 5px;
  margin-bottom: 30px;
}

.file_input{
  .camera_icon{
    font-size: 3rem;
  }
}

.image_area{
  img{
    background-color: #fff;
  }
}

.inner_card{
  max-width: 100%;
  padding: 25px 50px;

  .back-color{
    text-align: center;

    button.start{
      background-color: #329eff!important;
      font-size: 0.9rem;
      color: #fff;
      font-weight: bold;
      margin-top: 20px;
      padding: 10px;
      text-decoration: none;
      outline: none;
      border-radius: 5px;
      width: 80px;
    }

    button.comment_post{
      background-color: #329eff!important;
    }
  }

.v-input{
  font-size: 1.1rem;
}

  .photo_area{
    margin: 0 auto;
  }

  .file_input{
    margin: 0 auto;
  }

  .camera_icon{
    top: 13px;
    right: 2px;
  }

  .v-icon{
    color: grey!important;
  }
}

.back-color{
  text-align: center;

  button.start{
    background-color: #329eff!important;
    font-size: 0.9rem;
    color: #fff;
    font-weight: bold;
    margin-top: 20px;
    padding: 10px;
    text-decoration: none;
    outline: none;
    border-radius: 5px;
    width: 80px;
  }
}

.delete_area{
  padding: 25px 50px;

  .delete_question{
    text-align: center;
    width: 100%;
    padding: 30px;
    font-weight: 600;
  }
}

button.v-btn{
  color: #fff;
}


.v-date-picker{
  width: 100%!important;
}

.v-date-picker-header {
  display: none!important;
}

.post_contents{
  ul{
    padding: 0;
    margin:0 10px;

    li{
      list-style: none;
      margin-right: 10px;
      font-size: 1.2rem;;
    }
  }
}

</style>