<template>
<v-app>
  <div id="app" class="back_body">
    <GlobalHeader />

    <h2>Let's Post</h2>
    <v-card
      class="card_style"
    >

      <form @submit.prevent="submitPost" class="form_class ma-0">

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
              <div xs12 sm6 md3 class="photo_area">
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

        <!-- おすすめ -->
        <v-text-field
          style="margin-bottom: 30px; width: 350px;"
          class="pa-3"
          v-model="form.posts.pr1"
          :counter="20"
          label="おすすめポイント１"
        ></v-text-field>
        <v-text-field
          style="margin-bottom: 30px; width: 350px;"
          class="pa-3"
          v-model="form.posts.pr2"
          :counter="20"
          label="おすすめポイント２"
        ></v-text-field>
        <v-text-field
          style="margin-bottom: 30px; width: 350px;"
          class="pa-3"
          v-model="form.posts.pr3"
          :counter="20"
          label="おすすめポイント３"
        ></v-text-field>
        <v-text-field
          style="margin-bottom: 30px; width: 350px;"
          class="pa-3"
          v-model="form.posts.pr4"
          :counter="20"
          label="おすすめポイント４"
        ></v-text-field>

        <!-- タグ -->
        <div class="tag">
          <h3>Tag</h3>
          <v-checkbox
              class="ma-0"
              v-model="form.posts.tag"
              label="低燃費"
              color="info"
              value="低燃費"
              hide-details
            ></v-checkbox>
          <v-checkbox
              class="ma-0"
              v-model="form.posts.tag"
              label="駐車場無料"
              color="info"
              value="駐車場無料"
              hide-details
            ></v-checkbox>
          <v-checkbox
              class="ma-0"
              v-model="form.posts.tag"
              label="	1ヶ月間貸し出し可"
              color="info"
              value="1ヶ月間貸し出し可"
              hide-details
            ></v-checkbox>
        </div>

        <v-text-field
          style="margin-bottom: 30px;"
          class="pa-3 price_area"
          v-model="form.posts.price"
          :counter="5"
          :rules="nameRules"
          label="金額"
          required
        ></v-text-field>円

        <quillEditor v-model="form.posts.text" style="border: 1px solid;"/>
        <div class="back-color">
          <button type="submit" class="start">送信</button>
        </div>
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
      car_types: [
        {name: 'カローラ', types: 'corolla'},
        {name: 'プリウス', types: 'prius'},
        {name: 'ヴォクシー',types: 'voxy'},
        {name: 'シエンタ', types: 'sienta'},
        {name: 'アクア', types: 'aqua'},
        {name: 'アルファード', types: 'alphard'},
      ],

      results: [],

      form: {
        posts: {
          author: '',
          photo: '',
          title: '',
          text: '',
          pr1: '',
          pr2: '',
          pr3: '',
          pr4: '',
          tag: [],
          car_type: '',
          price: '',
          profile: {
            introduction: '',
            address: '',
            userpro: '',
          },
        }
      },

      profiles: [],

      ex4: ['info'],

      //写真アップロード
      uploadFile: null,
      icon: '',
      url: '',
      show: true,
    }
  },
  mounted(){
    //post
    axios.get('http://127.0.0.1:8000/api/v1/posts/')
    .then(response => {this.results = response.data})

    //profile
    axios.get('http://localhost:8000/api/v1/profile/')
    .then(response => { this.profiles = response.data })
    
  },
  methods: {
    submitPost: function(){
      let formData = new FormData();
      formData.append('author.id', this.$store.getters['auth/id'])
      formData.append('author.username', this.$store.getters['auth/username'])
      formData.append('photo', this.uploadFile)
      formData.append('title', this.form.posts.title)
      formData.append('text', this.form.posts.text)
      formData.append('pr1', this.form.posts.pr1)
      formData.append('pr2', this.form.posts.pr2)
      formData.append('pr3', this.form.posts.pr3)
      formData.append('pr4', this.form.posts.pr4)
      for (let i = 0; i < this.form.posts.tag.length; i++) {
        formData.append('tag[' + i + ']', JSON.stringify({'name': this.form.posts.tag[i]}))
      }
      formData.append('car_type', this.form.posts.car_type)
      formData.append('price', this.form.posts.price)
      formData.append('profile.introduction', this.user_profile.introduction);
      formData.append('profile.address', this.user_profile.address);
      formData.append('profile.userpro.id', this.$store.getters['auth/id']);
      formData.append('profile.userpro.username', this.$store.getters['auth/username']);

      api({
        method: 'post',
        url: '/posts/',
        data: formData,
        headers: {
          'content-type': 'multipart/form-data'
        },
      })
        .then(response => {
          this.form.posts = response.data
          console.log(this.form.posts)
          console.log('Post succeeded.')
          this.$store.dispatch('message/setInfoMessage', { message: '投稿しました。' })
          const next = this.$route.query.next || 'post_preview/' + this.form.posts.id
          this.$router.replace(next)
        })
        .catch(error => {
          console.log('ここ1', this.form.posts);
          console.log('ここ2', this.form.posts.profile.introduction);
          console.log('ここ3', error);
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
  },
  computed:{
    user_profile(){
      console.log(this.profiles)
      console.log(this.profiles.userpro)
      const profiles = this.profiles.find(profiles => profiles.userpro.username === this.$store.getters['auth/username'])
      if(!profiles){
        return {
          title: '見つかりません',
          text: '見つかりません',
        }
      }
      console.log('profiles', profiles)
      return profiles
    },
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

  .image_area{
    img{
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
  transition: 0.25s;
  padding: 6px 18px;
  cursor: pointer;
  margin: 3px;
}

.back-color{
  text-align: center;

  button.start{
    background-color: #329eff!important;
    font-size: 0.9rem;
    color: #fff;
    font-weight: bold;
    margin-top: 40px;
    padding: 10px;
    text-decoration: none;
    outline: none;
    border-radius: 5px;
    width: 80px;
  }
}

.v-input{
  width: 33.33%;
  display: inline-block;
}

.tag{
  border: 1px solid #999;
  border-radius: 5px;
  padding: 20px 15px;
  margin-bottom: 30px;

  h3{
    font-size: 1rem;
    font-weight: normal;
  }
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

.v-input{
  font-size: 1.1rem;
}

</style>