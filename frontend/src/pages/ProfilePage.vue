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
          <v-flex xs12 sm6 md3><img src="@/assets/img/superman.png" width="115" class="sticky" style="width:150px;"></v-flex>
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
                    <p class="text-lg-right">編集</p>
                    </v-text>
                    </template>

                    <v-card>
                      <form @submit.prevent="submitPost">
                      <v-flex xs12 sm6 md9>
                        <v-container>
                          <v-row>
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

                  <h1>こんにちは、{{ username }} です</h1>
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
                </v-col>


                <div class="border_line"></div>

                <v-col
                  cols="6"
                  md="12"
                >
                  <h2>レビュー</h2>
                  <v-row>
                  <v-fa :icon="['far', 'comments']" class="parking_icon sns_icons" />
                  <p class="ma-2">120 件</p>
                  </v-row>
                  <v-row v-for="comment in user_comments" :key="comment.id">
                    <v-col
                      cols="2"
                      md="2"
                    >
                    <div class="profile_icons">
                      <img src="https://d20r2glx6euv0l.cloudfront.net/avatar/6ebeed36dc.jpeg">
                    </div>
                    </v-col>
                    <v-col
                      cols="10"
                      md="10"
                      class="pa-0 review"
                    >
                    <h3>{{ comment.author }}</h3>
                    <p>{{ comment.comment }}</p>
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
import PrFooter from '@/components/PrFooter.vue'
import axios from 'axios'
import api from '@/services/api'

export default {
  name: 'Map',
  components: {
    GlobalHeader,
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
        }
      },
      fav: true,
      menu: false,
      message: false,
      hints: true,
      profiles: [],
      comments: [],
      post_form: {
        posts: {
          title: '',
          text: '',
        }
      },
      id : this.$store.getters['auth/id'],
      name : this.$store.getters['auth/username']
    }
  },
  mounted(){
    //profile
    axios.get('http://localhost:8000/api/v1/profile/')
    .then(response => { this.profiles = response.data }),

    //comment
    axios.get('http://localhost:8000/api/v1/comment/')
    .then(response => { this.comments = response.data })
  },
  methods: {
    // ログインボタン押下
    submitLogin: function () {
      // ログイン
      this.$store.dispatch('auth/login', {
        email: this.form.email,
        password: this.form.password
      })
        .then(() => {
          console.log('Login succeeded.')
          this.$store.dispatch('message/setInfoMessage', { message: 'ログインしました。' })
          // クエリ文字列に「next」がなければ、ホーム画面へ
          const next = this.$route.query.next || '/'
          this.$router.replace(next)
        })
    },
    // 編集ボタンでインスタンスを挿入
    editButton(){
      this.form.edit = this.user_profile
    },
    //プロフィール
    submitPost: function(){
      // this.form.edit.introduction = this.user_profile.introduction
      api({
        method: 'put',
        url: '/profile/' + this.id + '/',
        data: {
          'userpro': this.$store.getters['auth/id'],
          'introduction': this.form.edit.introduction,
          'address': this.form.edit.address,
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
    }
  },
  computed: {
    username(){
      return this.$store.getters['auth/username']
    },
    user_profile(){
      console.log(this.profiles)
      console.log(this.profiles.userpro)
      const profiles = this.profiles.find(profiles => profiles.userpro === this.$store.getters['auth/id'])
      if(!profiles){
        return {
          title: '見つかりません',
          text: '見つかりません',
        }
      }
      console.log('profiles', profiles)
      return profiles
    },
    user_comments(){
      const comments = this.comments.filter(comments => comments.username === this.$store.getters['auth/id']);
      return comments
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
  h3{
    font-size: 1rem;
    font-weight: 600;
  }
}

</style>