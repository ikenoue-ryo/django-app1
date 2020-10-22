<template>
  <v-container fluid class="header_class">
    <v-layout wrap class="header_inner">
      <a href="/">CarShare</a>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <div class="back-color">
          <v-row>
            <div class="search_form">
              <div class="search_icon">
                <v-fa :icon="['fas', 'search']" class="search_icon" />
              </div>
              <v-text-field
                label="検索..."
                v-model="keyword"
                @input="onInput"
                @focus="focus"
              >
              </v-text-field>
              
              <v-card
                class="car_search"
                max-width="300"
                tile
                v-show="show"
              >
                <v-list flat>
                  <v-subheader>CarType</v-subheader>
                  <v-list-item-group
                    color="primary"
                  >
                    <v-list-item
                      v-for="(car_type, index) in filterdCarTypes"
                      :key="index"
                      :href="car_type.en_name"
                    >
                      <v-list-item-icon style="margin-right:20px;">
                        <img :src="car_type.images" width="100">
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title v-text="car_type.jp_name"></v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>
              </v-card>

            </div>
            <div class="icon">
              <div class="text-center">
                <v-menu
                  width="100px!important"
                  v-model="menu"
                  :close-on-content-click="false"
                  :nudge-width="200"
                  left
                  offset-y
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      icon
                      v-bind="attrs"
                      v-on="on"
                    >
                      <img src="https://d20r2glx6euv0l.cloudfront.net/avatar/6ebeed36dc.jpeg">
                    </v-btn>
                  </template>

                  <v-card>
                    <v-list>
                      <v-list-item>
                        <v-list-item-avatar>
                          <img
                            src="https://d20r2glx6euv0l.cloudfront.net/avatar/6ebeed36dc.jpeg"
                            alt="Username"
                          >
                        </v-list-item-avatar>

                        <v-list-item-content>
                          <v-list-item-title>{{ username }}</v-list-item-title>
                        </v-list-item-content>

                        <v-list-item-action>
                          <v-btn
                            :class="fav ? 'red--text' : ''"
                            icon
                            @click="fav = !fav"
                          >
                            <v-icon>mdi-heart</v-icon>
                          </v-btn>
                        </v-list-item-action>
                      </v-list-item>
                    </v-list>

                    <v-divider class="ma-0"></v-divider>

                    <v-list>
                      <router-link :to="`/profile/${username}`">
                        <v-list-item v-ripple>
                        <v-list-item-action class="mr-2">
                          <div class="sns_icons">
                            <v-fa :icon="['far', 'user']" class="search_icon" />
                          </div>
                          </v-list-item-action>
                          <v-list-item-title>プロフィール設定</v-list-item-title>
                        </v-list-item>
                      </router-link>

                      <v-list-item 
                        href="/"
                        @click="logout"
                      >
                      <v-list-item-action class="mr-2">
                        <div class="sns_icons">
                          <v-fa :icon="['fas', 'sign-out-alt']" class="search_icon" />
                        </div>
                        </v-list-item-action>
                        <v-list-item-title>ログアウト</v-list-item-title>
                      </v-list-item>
                    </v-list>
                  </v-card>
                </v-menu>
              </div>
            
            </div>
          <v-btn v-if="isLoggedIn" href="post" class="start">投稿する</v-btn>
          <v-btn v-else href="signup" class="start">はじめる</v-btn>
          </v-row>
        </div>
      </v-toolbar-items>
    </v-layout>
  </v-container>
</template>



<script>
import car_types from '../pages/carTypes';
export default {
  data(){
    return{
      keyword: '',
      show: false,
      fav: true,
      menu: false,
      message: false,
      hints: true,
    }
  },
  computed: {
    username(){
      return this.$store.getters['auth/username']
    },
    isLoggedIn(){
      return this.$store.getters['auth/isLoggedIn']
    },
    car_types(){
      return car_types
    },
    filterdCarTypes(){
      const car_types = [];
      for(const i in this.car_types){
          const car = this.car_types[i];
          if(car.jp_name.indexOf(this.keyword) !== -1 ||
          car.jp_hira.indexOf(this.keyword) !== -1) {
            car_types.push(car);
          }
      }
      return car_types;
    }
  },
  methods:{
    onInput(){
      this.show = true
    },
    // フォーカスされた時の処理
    focus(){
      this.keyword = ''
      this.show = false
    },
    // カーソールが外れた時の処理
    outblur(){
      this.keyword = ''
      // this.show = false
    },
    logout(){
      this.$store.dispatch('auth/logout')
    }
  }
}
</script>



<style lang="scss">
.header_class{
  background-color: #fff;
  .header_inner{
    width: 900px;
    margin: 0 auto;
    padding: 0 20px;
    a{
      font-size: 1.2rem;
      font-weight: 600;
      padding: 10px;
      margin:0;
      color: #000;
      text-decoration: none;
    }
    a.start{
      background-color: #329eff!important;
      font-size: 0.9rem;
      color: #fff;
      font-weight: bold;
      margin-top: 8px;
    }
  }
  .icon {
    display: inline-block;
    float: right;
    margin: 10px;
  }
  .icon img {
    width: 35px;
    border-radius: 50%;
    border: 1px solid grey;
  }
  .v-btn{
    outline: none;
  }
}
.back-color{
  .search_form{
    position: relative;
    bottom: 5px;
    .v-input{
      display: inline-block;
      float: left;
      margin-right: 10px;
      padding-top: 10px;
      height: 43px;
    }
    .search_icon{
      font-size: 27px !important;
      width: 33px;
      display: inline-block;
      float: left;
      padding: 12px 6px 0 5px;
    }
  }
}
#app{
  font-family: Rubik, "Noto Sans JP", sans-serif;
  .container {
    max-width: 100%;
  }
}
.search_form{
  .v-card{
    position: absolute;
    top: 60px;
    z-index: 10;
    right: 10px;
  }
  .v-list{
    width: 226px;
  }
}
.sns_icons {
  font-size: 1.5rem;
  width: 50px;
  display: inline-block;
  float: left;
  margin-left: 10px;
  .logout_icon{
    color: grey;
  }
  .user_icon{
    color: grey;
  }
}
.v-list{
  a{
    text-decoration: none;
  }
}
</style>