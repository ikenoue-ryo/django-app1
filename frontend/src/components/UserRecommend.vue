<template>
  <div calss="vertical_height2">
    <!-- <ul v-for="profile in profiles" :key="profile">
      <li><img :src="profile.icon"></li>
    </ul> -->
    <div class="car_recommend">
      <div class="car_recommend_article change_back_color">
        <div class="recommend_back_size">
          <h2 class="font-weight-bold text-left dark-grey-text pb-2">User Nearby</h2>
          <hr class="w-header my-4">
        </div>
        <ul class="horizontal-list">
          <li class="item mx-2" v-for="(profile, index) in profiles" :key="index">
            <!-- Card -->
            <router-link :to="`/profile/${profile.userpro.username}`">
            <a class="card hoverable mb-4" data-toggle="modal" data-target="#basicExampleModal">
              <v-col class="pa-0 card_size">
                <v-hover
                v-slot:default="{ hover }"
                close-delay="200"
                >
                <v-card
                  class="py-3 { 'on-hover': hover }"
                  :elevation="hover ? 12 : 2"
                >
                  <v-img :src="profile.icon" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">{{ profile.userpro.username }}</h3>
                    <v-rating
                      v-model="profile.point"
                      background-color="orange lighten-3"
                      color="orange"
                      size="20"
                      dense
                    ></v-rating>
                  </div>
                </v-card>
                </v-hover>
              </v-col>
            </a>
            </router-link>
            <!-- Card -->
          </li>
         
        </ul>
<!--        <div class="back_size">-->
<!--          <div class="more_button">-->
<!--            <button type="button" class="btn btn-git">もっと見る <i class="fas fa-angle-right"></i></button>-->
<!--          </div>-->
<!--        </div>-->
      </div>
    </div>
  </div>
</template>


<script>
// import profiles from '../pages/profileLists'
import axios from 'axios'

export default {
  data(){
    return {
      rating: 0,
      profiles: [],
    }
  },
  mounted(){
    //profile
    axios.get('http://localhost:8000/api/v1/profile/')
    .then(response => { this.profiles = response.data })
  },
  // computed:{
  //   profiles(){
  //     return profiles;
  //   }
  // },
}
</script>


<style lang="scss" scoped>
.w-header{
  width: 50px;
}

.car_recommend_article {
  background: #bbdefb;
  padding: 60px;
}

.car_recommend_article .recommend_back_size {
  margin: 0 auto;
  text-align: left;
}

.car_recommend_article .recommend_back_size h2 {
  margin-left: 10px;
}

.car_recommend_article .recommend_back_size hr {
  text-align: left;
  display: block;
  margin-left: 10px;
}

.car_recommend_article ul.horizontal-list {
  overflow-x: auto;
  white-space: nowrap;
  padding-left: calc(50% - 451px);
  margin: 0;
}

.car_recommend_article li.item {
  display: inline-block;
  margin: 14px 0;
  vertical-align: top;
}

.change_back_color {
  background: #eee;
}

a.card{
  text-decoration: none;
}

.card-body{
  padding: 10px;

  h3{
    font-size: 0.9rem;
    margin: 0;
  }

  p{
    color: grey;
    font-size: 0.7rem;
    margin: 0;
  }
}

.v-rating{
  button{
   padding: 0!important; 
  }
}

.v-card:not(.on-hover) {
  transition: .2s ease-in-out;
}
</style>