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
          <v-flex xs12 sm6 md3><img :src="user_profile.icon" width="115" class="sticky" style="width:150px;"></v-flex>
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
                    <p class="text-lg-right">編集</p>
                    </v-text>
                    </template>

                    <v-card
                      class="card_style"
                    >
                      <GlobalMessage class="message_card" />

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
                                required
                              ></v-text-field>
                            </v-col>
<!-- 
                            <v-col
                              cols="12"
                              md="12"
                            >
                              <v-text-field
                                v-model="form.password"
                                type="password"
                                label="パスワード"
                                required
                              ></v-text-field>
                            </v-col> -->

                          </v-row>
                          <div class="back-color">
                              <button type="submit" class="start">保存</button>
                          </div>
                        </v-container>
                      </v-flex>
                      </form>
                    </v-card>
                  </v-dialog>
                </div>
                <!-- モーダル -->

                  <h1>こんにちは、{{ user_profile.userpro.username }} です</h1>
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                  <h2>自己紹介</h2>
                  <p>{{ user_profile.introduction }}</p>
                </v-col>

                <div class="border_line"></div>

                <v-col
                  cols="6"
                  md="12"
                >
                  <h2>貸し出し中の車</h2>
                  <!-- {{ user_posts }} -->
                  <ul v-for="posts in user_posts" :key="posts.id">
                    <router-link :to="`/post_preview/${posts.id}`">
                      <li>{{posts.car_type}}</li>
                    </router-link>
                  </ul>
                  <v-container style="padding:0; margin: 20px 0;">
                    <v-row>
                      <v-col cols="12" md="6" class="pa-3">
                        <v-card
                          class="pa-0"
                          max-width="344"
                          href="#"
                        >
                          <v-img
                            src="https://toyota.jp/pages/contents/corollasport/001_p_001/4.0/image/car-viewer/43_1_5/43_1_5_030_c.jpg"
                            height="150"
                          ></v-img>

                          <v-card-title>
                            カローラ
                          </v-card-title>
                        </v-card>
                      </v-col>
                      <v-col cols="12" md="6" class="pa-3">
                        <v-card
                          class="pa-0"
                          max-width="344"
                          href="#"
                        >
                          <v-img
                            src="https://toyota.jp/pages/contents/voxy/003_p_007/4.0/image/car-viewer/11_1_1/11_1_1_030_c.jpg"
                            height="150"
                          ></v-img>

                          <v-card-title>
                            ヴォクシー
                          </v-card-title>
                        </v-card>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-col>


                <div class="border_line"></div>

                <v-col
                  cols="6"
                  md="12"
                >
                <h2>駐車場</h2>
                  <v-row class="parking_area">
                      <v-fa :icon="['fas', 'parking']" class="parking_icon sns_icons" />
                    <p class="ma-2">{{ user_profile.address }}</p>
                  </v-row>
                  <div class="map" ref="googleMap" />
                </v-col>


                <div class="border_line"></div>

                <v-col
                  cols="6"
                  md="12"
                  class="user_comment"
                >
                  <h2>レビュー</h2>
                  <v-row>
                  <v-fa :icon="['far', 'comments']" class="parking_icon sns_icons" />
                  <p class="ma-2">{{ user_comments.length }} 件</p>
                  </v-row>
                  
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
                      <router-link :to="`/profile/${comment.profile.userpro.username}`">
                        {{ comment.profile.userpro.username }}
                      </router-link>
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
import GlobalMessage from '@/components/GlobalMessage.vue'
import PrFooter from '@/components/PrFooter.vue'
import axios from 'axios'
import api from '@/services/api'
import GoogleMapsApiLoader from 'google-maps-api-loader';


export default {
  name: 'Map',
  components: {
    GlobalHeader,
    GlobalMessage,
    PrFooter,
  },
  data(){
    return {
      dialog: false,
      
      google: null,
      mapConfig: {
        center: {
          lat: 35.68944,
          lng: 139.69167
        },
        zoom: 17
      },
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
    }
  },
  async mounted(){
    //profile
    axios.get('http://localhost:8000/api/v1/profile/')
    .then(response => { this.profiles = response.data }),

    //post
    axios.get('http://localhost:8000/api/v1/posts/')
    .then(response => { this.posts = response.data })

    //comment
    axios.get('http://localhost:8000/api/v1/comment/')
    .then(response => { this.comments = response.data })

    this.google = await GoogleMapsApiLoader({
      apiKey: ''
    });
    this.initializeMap();
  },
  methods: {
    initializeMap() {
      new this.google.maps.Map(this.$refs.googleMap, this.mapConfig);
    },

    // 写真アップロード
    selectedFile(e){
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
      formData.append('form.edit.icon', this.uploadFile);

      api({
        method: 'put',
        url: '/profile/' + this.id + '/',
        data: {
          'userpro': {
            'id': this.$store.getters['auth/id'],
            'username': this.$store.getters['auth/username'],
          },
          'introduction': this.form.edit.introduction,
          'address': this.form.edit.address,
          'icon': this.form.edit.icon,
        },
        headers: {
          'content-type': 'multipart/form-data;'
        }
      })
        .then(response => {
          // const username = this.$store.getters['auth/username']
          this.form.edit = response.data
          this.$store.dispatch('message/setInfoMessage', { message: '保存しました。' })
          // const next = this.$route.query.next || `/profile/${username}`
          const next = this.$route.query.next || '/'
          console.log('path', next)
          this.$router.replace(next)
        })

      // axios.
      //   post('/profile/' + this.id + '/', formData, config)
      //   .then(function(response){
      //     console.log(response)
      //   })
      //   .catch(function(error) {
      //     console.log(error)
      //   })
    }
  },
  computed: {
    username(){
      return this.$store.getters['auth/username']
    },
    user_profile(){
      console.log(this.profiles)
      console.log(this.profiles.userpro)
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
    }
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

  .camera_icon{
    font-size: 3rem;
    position: relative;
    top: 23px;
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

.user_comment{
  p:hover{
    cursor : pointer;
    opacity: 0.8;
    transition-duration: 0.5s;
  }
}
</style>