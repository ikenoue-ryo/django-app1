<template>
  <div>
    <GlobalHeader />

    <div class="back_body">
      <h2>Let's Ride</h2>

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

        <v-app>
          <v-container fluid class="back_color">
            <v-layout wrap class="main_img">
                <div>
                  <v-carousel cycle interval="4000" class="rounded-lg">
                    <v-carousel-item v-for="(image, index) in post.main_images" :key="index">
                      <v-row>
                        <v-col class="mt-3">
                          <v-img :src="image.photo" class="rounded-lg main_image"></v-img>
                        </v-col>
                      </v-row>
                    </v-carousel-item>
                  </v-carousel>
                </div>
            </v-layout>

            <v-row>
              <v-col class="blog_text">
              <h2>{{ post.car_type }}の基本情報！</h2>
                <ul v-for="(car, index) in post.car_info" :key="index">
                  <li>{{ car.infomation }}</li>
                </ul>
              </v-col>
            </v-row>

            <v-row>
              <v-col class="blog_text">
                <h2>お気に入りポイント①</h2>
                <img :src="post.main_images[0].photo">
                <ul v-for="(car, index) in post.car_recommend1" :key="index">
                  <li>{{ car.point }}</li>
                </ul>
              </v-col>
            </v-row>

            <v-row>
              <v-col class="blog_text">
                <h2>お気に入りポイント②</h2>
                <img :src="post.main_images[1].photo">
                <div v-for="(car, index) in post.car_recommend2" :key="index">
                  <p>{{ car.point }}</p>
                </div>
              </v-col>
            </v-row>

            <v-row>
              <v-col class="blog_text">
                <h2>お気に入りポイント③</h2>
                <img :src="post.main_images[2].photo">
                <div v-for="(car, index) in post.car_recommend3" :key="index">
                  <p>{{ car.point }}</p>
                </div>
              </v-col>
            </v-row>

          <v-layout wrap class="profile" v-for="(user, index) in post.user_info" :key="index">
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
          </v-layout>

          <div class="share_price">
            <div class="card">
              <div class="card-body">
                <div class="price">{{ post.price }}<span class="yen"> 円/(月額)</span></div>
                <p class="card-text">24h以内に指定の場所に返却してください。</p>
                <a href="#"><v-btn color="#2bbbad">予約する</v-btn></a>
              </div>
            </div>
          </div>

          </v-container>
        </v-app>
      </div>


    </div>

    
  <GlobalFooter />
  </div>
</template>


<script>
import GlobalHeader from '../components/GlobalHeader'
import GlobalFooter from '../components/GlobalFooter'
import posts from '../pages/postLists';


export default{
  components:{
    GlobalHeader,
    GlobalFooter,
  },
  data () {
      return {
        photos: [
          {
            image: 'https://lh3.googleusercontent.com/pw/ACtC-3fYdGWASYQcPttnU6cGD7OJeQdCnuEIZciUb69jMDYucp4WAq9G8Lcph2Iybng0DapIWhI3GN4LLKcRe_qOuWZ21e88v0aZMCba71WmCcEIZdleUWFozU23JI8rTv3aG9v8Ujxhmgw0qZmiKWSptupq=w1880-h1410-no?authuser=0'
          },
          {
            image: 'https://lh3.googleusercontent.com/pw/ACtC-3fTv4VZI0rjLUvkqhvgNV9IYHAHdLPXuwnBmNSuk1hY9DqdGWwL0sh-fcTjhn8m9Vte1R35Z9yvE1CX0FTt9ancMw3NWJwgMJHpyzBYkhPmw_2l-67WI9ihdQXyBXAgTimz1PpllqcUi4afc4P5SSjM=w1880-h1410-no?authuser=0'
          },
          {
            image: 'https://lh3.googleusercontent.com/pw/ACtC-3fFxuGkyQ4Ptks6YZFZlxa4nFK-p6MiJqzBZw2xKBy5xapGGJ3wVNKpr8EZg9Og1ygvhTbW_fhaLBTck4pb48gAg5I8FLqeoJrIudbkGrWsg1V94ZY2CrbpJ2vs9oHbfNREoecvsk42en5VNVaHbIuV=w1880-h1410-no?authuser=0'
          },
          {
            image: 'https://lh3.googleusercontent.com/pw/ACtC-3c5-mYefFGUMD7SzqHCDAnhRrlGf7HhV7xNHI6WCN1Nm_-VWCXM4xGoLLy6HzaMMnGtxcQ7Ws82jfZVJLPCbDl5fbXRE2xMaPesT40Y3DKGZhGlu7UxYfv3BZHzh_EnwsnMuhRE_8RM_pWqzVWV4fHq=w1880-h1410-no?authuser=0'
          },
          {
            image: 'https://lh3.googleusercontent.com/pw/ACtC-3fcS4fX1FG55xLgw55LvePc5CpqLW1HN5ruL3Awcu8mvRCq-YuJ0E4pnzgTJ5reJ1FOmtYtQ6RaXrcS6LjvOhySGSu-cuipRO5sqrJbnFq_cnbh4ZHb1vXCEFJl71ilcct9oDCe6DjngIY40x5DSsjA=w1880-h1410-no?authuser=0'
          },
        ],
      }
    },
  computed:{
    id(){
      return Number(this.$route.params.id);
    },
    post(){
      const post = posts.find(posts => posts.id === this.id);
      if (!post) {
        return {
          author: '見つかりません',
          car_type: '',
          title: '',
          text: '',
        };
      }
      return post
    },
    author(){
      return this.post.author
    },
    car_type(){
      return this.post.car_type
    },
    title(){
      return this.post.title
    },
    text(){
      return this.post.text
    },
  }

}
</script>


<style lang="scss" scoped>
#app{
  font-family: Rubik, -apple-system, "Hiragino Sans", "Hiragino Kaku Gothic ProN", BlinkMacSystemFont, YuGothic, "Yu Gothic", sans-serif;
  position: relative;
  top: -30px;
  width: 700px;
  margin: 0 auto;
}

.back_color {
  background-color: #eee;
  overflow: hidden;
}

.back_body{
  background-color: #eee;
  overflow: hidden;
  

  h2{
    font-size: 45px;
    font-weight: 600;
    text-align: center;
    margin: 30px;
  }
}

.main_img{
  width: 860px;
  margin: 0 auto;
}

.post-car {
  position: relative;
  top: 0;
  right: 0;

  i{
    font-size: 3.0rem;
    margin-left: 26px;
  }
}

.post-car a.btn--circle {
  border-radius: 50%;
  line-height: 100px;
  width: 100px;
  height: 100px;
  padding: 0;
  -webkit-box-shadow: 0 5px 0 #26a69a;
  box-shadow: 0 5px 0 #26a69a;
  background: #30cfc0;
  color: #fff;
  font-size: 1.2rem;
  text-decoration: none;
}

.post-car a.btn--circle:hover {
  -webkit-transform: translate(0, 3px);
  transform: translate(0, 3px);
  -webkit-box-shadow: 0 2px 0 #26a69a;
  box-shadow: 0 2px 0 #26a69a;
}

.post-car a.user-post {
  position: fixed;
  bottom: 20px;
  right: 110px;
  z-index: 10;
}

.post-car .fa, .post-car .fas {
  font-size: 2.5rem;
  position: relative;
  top: 9px;
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
  background: #fff;
  margin-bottom: 100px;
  
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
  }
}

.clearfix::after {
   content: "";
   display: block;
   clear: both;
}

.share_price {
  background-color: #f5f5f5;
  margin: 36px;

  .card {
    width: 230px;
    border-radius: 15px;
    position: fixed;
    bottom: 30px;
    right: 110px;
    z-index: 10;
    padding: 5px;
    border: 1px solid #eee;
    background: #fff;
    box-shadow: 0 2px 5px 0 rgba(0,0,0,0.16), 0 2px 10px 0 rgba(0,0,0,0.12);
  }

  .card-body{
    .v-btn{
      background: #2bbbad;
      color: #fff;
      font-size: 1rem;
      padding: 10px;
      width: 100%;
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

.main_image{
  max-width: 680px;
  height: 500px;
}



</style>