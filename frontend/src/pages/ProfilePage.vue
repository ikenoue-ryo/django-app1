<template>
  <v-app>
    <div class="back_body">
      <GlobalHeader />

      <h2>Profile</h2>
      <v-card
        class="card_style"
        max-width="800"
      >
        
        <v-layout wrap>
          <v-flex xs12 sm6 md3 text-center>
            <img v-if="user_profile.icon" :src="user_profile.icon" width="115" class="sticky" style="width:150px; margin:10px;">
            <div v-else class="file_input">
              <label class="input-item__label">
                <v-fa :icon="['fas', 'camera']" class="camera_icon sns_icons" :rules="rules"/>
              </label>
            </div>
            <!-- <router-link :to="`/message/${username}`">
              <v-icon color="blue">mdi-email-outline</v-icon>Messageを送る
            </router-link> -->
          </v-flex>
          <v-flex xs12 sm6 md9>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  md="12"
                >
                <!-- モーダル -->
                <div class="text-center">
                  <v-dialog
                    v-model="dialog"
                    width="600"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text
                        color="red lighten-2"
                        dark
                        v-bind="attrs"
                        v-on="on"
                        @click="editButton"
                      >
                    <p class="text-lg-right" v-if="username === $route.params.username">編集</p>
                    </v-text>
                    </template>

                    <v-card
                      class="card_style"
                    >
                      <!-- <GlobalMessage class="message_card" /> -->

                      <form @submit.prevent="submitPost">
                      <v-flex xs12 sm6 md9 class="inner_card">
                        <v-container>
                          <v-row>
                            <div xs12 sm6 md3 class="photo_area">
                              <div class="file_input">
                                <label class="input-item__label">
                                  <v-fa :icon="['fas', 'camera']" class="camera_icon sns_icons" />
                                  <input type="file" name="file" ref="preview" @change="selectedFile" v-show="show">
                                </label>
                              </div>

                              <div class="image_area" v-if="url" style="position:relative">
                                <div style="position:absolute" @click="deletePreview"><v-icon color="white">mdi-close</v-icon></div>
                                <img :src="url">
                              </div>
                            </div>

                            <v-col
                              cols="12"
                              md="12"
                            >
                              <v-text-field
                                v-model="form.edit.introduction"
                                label="自己紹介"
                                autocomplete="off"
                                required
                              ></v-text-field>
                            </v-col>

                            <v-col
                              cols="12"
                              md="12"
                            >
                              <v-text-field
                                v-model="form.edit.address"
                                label="駐車場"
                                autocomplete="off"
                                required
                              ></v-text-field>
                            </v-col>
                          </v-row>
                          <div class="back-color">
                              <v-btn type="submit" class="start">保存</v-btn>
                          </div>
                        </v-container>
                      </v-flex>
                      </form>
                    </v-card>
                  </v-dialog>
                </div>
                <!-- モーダル -->

                  <h1 v-if="user_profile.userpro">こんにちは、{{ user_profile.userpro.username }} です</h1>
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                  <h2>自己紹介</h2>
                  <p v-if="user_profile.introduction">{{ user_profile.introduction }}</p>
                  <p v-else class="non_post" style="padding-left:10px;">入力してください</p>
                </v-col>

                <div class="border_line"></div>

                <v-col
                  md="12"
                >
                  <h2>投稿した車</h2>
                  <v-container style="padding:0;" v-if="user_posts && user_posts.length > 0">
                    <v-row>
                      <v-col cols="12" md="6" class="pa-3" v-for="posts in user_posts" :key="posts.id">
                        <router-link :to="`/post_preview/${posts.id}`" class="font_color">
                          <v-card
                            class="pa-0"
                            max-width="344"
                          >
                            <v-img
                              :src="posts.photo"
                              height="150"
                            ></v-img>

                            <v-card-title>
                              {{posts.car_type}}
                            </v-card-title>
                          </v-card>
                        </router-link>
                      </v-col>
                    </v-row>
                  </v-container>
                  <div v-else class="non_post">
                    <router-link :to="`/post/`">
                        <v-fa :icon="['fas', 'pencil-alt']" class="parking_icon sns_icons" />
                        <p class="ma-2">投稿がまだありません</p>
                    </router-link>
                  </div>
                </v-col>


                <div class="border_line"></div>

                <v-col
                  md="12"
                >
                <h2>駐車場</h2>
                  <v-row>
                    <div class="parking_area" v-if="user_profile.address && user_profile.address.length > 0">
                        <v-fa :icon="['fas', 'parking']" class="parking_icon sns_icons" />
                      <p class="ma-2">{{ user_profile.address }}</p>
                    </div>
                    <div v-else class="non_post" style="padding-left:10px;">
                      <p>駐車場が入力されていません</p>
                    </div>
                  </v-row>

                  <!-- マップ -->
                  <!-- <input type="text" v-model="address" style="border:1px solid;">
                  <button type="button" @click="mapSearch">検索</button>
                  <div id="map"></div> -->
                  <!-- マップ -->
                </v-col>


                <div class="border_line"></div>

                <v-col
                  md="12"
                  class="user_comment"
                >
                  <h2>レビュー</h2>
                  <v-row>
                  <v-fa :icon="['far', 'comments']" class="parking_icon sns_icons" />
                  <p class="ma-2">{{ user_comments.length }} 件</p>
                  </v-row>
                  
                  <div class="mb-5">
                    <form @submit.prevent="submitComment" class="form_class">
                      <v-rating
                        v-model="form.comment.point"
                        background-color="orange lighten-3"
                        color="orange"
                        size="20"
                        dense
                      ></v-rating>
                      <v-text-field
                        v-model="form.comment.comment"
                        label="コメントを書く"
                        :rules="rules"
                        hide-details="auto"
                        class="comment_form"
                      ></v-text-field>
                      <div class="back-color text-lg-right pa-3 submit_comment">
                        <v-btn type="submit" class="comment_post">送信</v-btn>
                      </div>
                    </form>
                  </div>

                  <v-row v-for="comment in user_comments" :key="comment.id">
                    <v-col
                      cols="2"
                      md="2"
                    >
                    <div class="profile_icons">
                      <router-link :to="`/profile/${comment.profile.userpro.username}`"><img :src="comment.profile.icon"></router-link>
                    </div>
                    </v-col>
                    <v-col
                      cols="10"
                      md="10"
                      class="review"
                    >
                    <h3>
                      <v-row class="ml-0">
                        <router-link :to="`/profile/${comment.profile.userpro.username}`" class="mr-3">
                          {{ comment.profile.userpro.username }}
                        </router-link>
                        <v-rating
                          v-model="comment.point"
                          background-color="orange lighten-3"
                          color="orange"
                          size="20"
                          dense
                        ></v-rating>
                      </v-row>
                    </h3>
                    <p @click="isActive = !isActive" :class="comment_all">{{ comment.comment }}</p>
                    </v-col>
                    <div class="border_line mb-5"></div>
                  </v-row>
                </v-col>

              </v-row>
            </v-container>
          </v-flex>
        </v-layout>
      </v-card>
      <PrFooter />
    </div>
  </v-app>
</template>


<script>
import GlobalHeader from '@/components/GlobalHeader.vue'
// import GlobalMessage from '@/components/GlobalMessage.vue'
import PrFooter from '@/components/PrFooter.vue'
import axios from 'axios'
import api from '@/services/api'

export default {
  name: 'Map',
  metaInfo: {
    script: [
      { src: `https://maps.googleapis.com/maps/api/js?key=${process.env.VUE_APP_GOOGLE_MAP_API}&callback=initMap`, async: true, defer: true }
    ],
  },
  components: {
    GlobalHeader,
    // GlobalMessage,
    PrFooter,
  },
  data(){
    return {
      dialog: false,
      
      form: {
        valid: false,
        password: '',
        nameRules: [
          v => !!v || 'Name is required',
          v => v.length <= 10 || 'Name must be less than 10 characters',
        ],
        email: '',
        emailRules: [
          v => !!v || 'E-mail is required',
          v => /.+@.+/.test(v) || 'E-mail must be valid',
        ],
        edit: {
          introduction: '',
          address: '',
          icon: '',
        },
        comment:{
          username: '',
          point: '',
          comment: '',
          profile: '',
        }
      },
      fav: true,
      menu: false,
      message: false,
      hints: true,
      profiles: [],
      posts: [],
      comments: [],
      post_form: {
        posts: {
          title: '',
          text: '',
        }
      },
      id : this.$store.getters['auth/id'],
      name : this.$store.getters['auth/username'],
      //写真アップロード
      uploadFile: null,
      icon: '',
      url: '',
      show: true,

      isActive: true,

      // コメント
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],

      // マップ
      map: {},
      marker: null,
      geocoder: {},
      address: ''
    }
  },
  mounted(){
    //profile
    axios.get('/api/v1/profile/')
    .then(response => { this.profiles = response.data }),

    //post
    axios.get('/api/v1/posts/')
    .then(response => { this.posts = response.data })

    //comment
    axios.get('/api/v1/comment/')
    .then(response => { this.comments = response.data })

    this.map = new window.google.maps.Map(document.getElementById('map'));
    this.geocoder = new window.google.maps.Geocoder();

  },
  methods: {
    mapSearch() {
      console.log('mapSearch')
      this.geocoder.geocode({
        'address': this.address
      }, (results, status) => {
        console.log('results', results)
        if (status === window.google.maps.GeocoderStatus.OK) {
          this.map.setCenter(results[0].geometry.location);
          // 緯度経度の取得
          // results[0].geometry.location.lat();
          // results[0].geometry.location.lng();
          this.marker = new window.google.maps.Marker({
            map: this.map,
            position: results[0].geometry.location
          });
          console.log(this.marker)
        }
      });
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
      this.form.edit = this.user_profile
    },
    //プロフィール
    submitPost: function(){
      let formData = new FormData();
      formData.append('userpro.id', this.id);
      formData.append('userpro.username', this.name);
      formData.append('introduction', this.form.edit.introduction);
      formData.append('address', this.form.edit.address);
      formData.append('icon', this.uploadFile);

      api({
        method: 'put',
        url: '/profile/' + this.id + '/',
        data: formData,
        headers: {
          'content-type': 'multipart/form-data'
        },
      })
        .then(response => {
          this.form.edit = response.data
          this.$store.dispatch('message/setInfoMessage', { message: '保存しました。' })
          const next = this.$route.query.next || `/profile/${this.name}`
          console.log('path', next)
          // goでリロード処理
          this.$router.go(next)
        })
    },
    // コメント
    submitComment: function(){
      let formData = new FormData();
      formData.append('username', this.user_profile.id);
      formData.append('point', this.form.comment.point);
      formData.append('profile.id', this.user_profile.id);
      formData.append('comment', this.form.comment.comment);

      api({
        method: 'put',
        url: '/comment/' + this.id + '/',
        data: formData,
        headers: {
          'content-type': 'multipart/form-data'
        },
      })
      .then(response => {
        this.form.comment = response.data
        console.log('Comment succeded.')
        const next = this.$route.query.next || `/profile/${this.name}`
        this.$router.go(next)
      })
    },
  },
  computed: {
    username(){
      return this.$store.getters['auth/username']
    },
    user_profile(){
      console.log(this.profiles)
      const profiles = this.profiles.find(profiles => profiles.userpro.username === this.$route.params.username)
      if(!profiles){
        return {
          title: '見つかりません',
          text: '見つかりません',
        }
      }
      console.log('profiles', profiles)
      return profiles
    },
    user_posts(){
      const posts = this.posts.filter(posts => posts.author.username === this.$route.params.username);
      return posts
    },

    user_comments(){
      const comments = this.comments.filter(comments => comments.username === this.user_profile.id);
      return comments
    },
    comment_all(){
      return{
        all:this.isActive,
        part:!this.isActive,
      }
    },
    // id(){
    //   console.log('投稿ID', this.$route.params.id)
    //   return Number(this.$route.params.id);
    // },
  },
}
</script>


<style lang="scss" scoped>
.map{
  width: 100%;
  height: 300px;
  border-radius: 20px;
  margin-bottom: 20px;
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
  min-height: 100vh;

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

    h1{
      font-size: 2.0rem;
      text-align: left;
      margin: 0;
    }

    h2{
      font-size: 1.4rem;
      text-align: left;
      margin: 20px 0;
    }

    p{
      font-size: 1rem;
      text-align: justify;
    }

    .back-color{
      button.start{
        background-color: #329eff!important;
        font-size: 0.9rem;
        color: #fff;
        font-weight: bold;
        margin-top: 20px;
        padding: 20px;
        text-decoration: none;
        outline: none;
      }
    }
  }
}

.sns_icons {
  font-size: 1.3rem;
  margin: 12px;
  display: inline-block;

  .parking_icon{
    color: #000;
  }

  p{
    display: inline-block;
    margin-left: 10px;
    font-size: 1.2rem;
  }
}

.border_line{
  border: 1px solid #EBEBEB;
  width: 100%;
}

.profile_icons{
  img{
    width: 50px;
    border-radius: 50%;
    border: 1px solid grey;
  }
}

.review{
  padding: 12px 0;

  p{
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
  }

  h3{
    font-size: 1rem;
    font-weight: 600;
  }
}

.file_input{

  border: 1px solid #999;
  border-radius: 50px;
  width: 100px;
  height: 100px;
  margin: 5px auto;

  .camera_icon{
    font-size: 3rem;
    position: relative;
    top: 14px;
    right: 3px;
  }
}

.image_area{
  position: relative;
  bottom: 100px;
  right: 20px;

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

  .photo_area{
    width: 200px;
    height: 200px;
    padding: 0 20px;
    margin: 0 auto;
  }

  .file_input{
    margin: 0 auto;
    position: relative;
    top: 50px;
  }

  .camera_icon{
    top: 13px;
    right: 2px;
  }

  .v-icon{
    color: grey!important;
  }
}

.all{
  display: revert!important;
}
 
.part{
  display: -webkit-box!important;
}
.parking_area{
  width: 100%;
}

.user_comment{
  p:hover{
    cursor : pointer;
    opacity: 0.8;
    transition-duration: 0.5s;
  }
}

.non_post{
  padding: 30px 0;
}

.post_area {
  color: #329eff;
}

button{
  outline: none;
}
</style>