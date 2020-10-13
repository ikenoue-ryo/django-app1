<template>
  <div calss="vertical_height2">
    <div class="car_recommend">
      <div class="car_recommend_article change_back_color">
        <div class="recommend_back_size">
          <h2 class="font-weight-bold text-left dark-grey-text pb-2">User Nearby</h2>
          <hr class="w-header my-4">
        </div>
        <ul class="horizontal-list">
          <li class="item mx-2">
            <!-- Card -->
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
                  <v-img :src="`https://pbs.twimg.com/media/B1BAtSlCQAAj2xG.jpg`" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">りゅう</h3>
                    <v-rating
                      v-model="rating"
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
            <!-- Card -->
          </li>
          <li class="item mx-2">
            <!-- Card -->
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
                  <v-img :src="`https://i.pinimg.com/originals/30/b2/a4/30b2a44767da51d307d88e12e180333c.jpg`" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">チュンリー</h3>
                    <v-rating
                      v-model="rating"
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
            <!-- Card -->
          </li>
          <li class="item mx-2">
            <!-- Card -->
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
                  <v-img :src="`https://i2.gamebiz.jp/images/original/194904785554389dde833ea0011.jpg`" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">剛拳</h3>
                    <v-rating
                      v-model="rating"
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
            <!-- Card -->
          </li>
          <li class="item mx-2">
            <!-- Card -->
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
                  <v-img :src="`https://www.4gamer.net/games/277/G027772/20141125001/SS/003.jpg`" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">赤髪</h3>
                    <v-rating
                      v-model="rating"
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
            <!-- Card -->
          </li>
          <li class="item mx-2">
            <!-- Card -->
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
                  <v-img :src="`https://i.pinimg.com/originals/83/cf/6d/83cf6dbfe424b4f071b37ae32910f885.jpg`" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">赤髪</h3>
                    <v-rating
                      v-model="rating"
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
            <!-- Card -->
          </li>
          <li class="item mx-2">
            <!-- Card -->
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
                  <v-img :src="`https://i.pinimg.com/originals/4b/98/78/4b9878c987500ab5772e89bcaf44e3d8.jpg`" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">ケン</h3>
                    <v-rating
                      v-model="rating"
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
            <!-- Card -->
          </li>
          <li class="item mx-2">
            <!-- Card -->
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
                  <v-img :src="`https://dengekionline.com/elem/000/000/941/941673/street_14_cs1w1_298x.jpg`" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">隊長</h3>
                    <v-rating
                      v-model="rating"
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
            <!-- Card -->
          </li>
          <li class="item mx-2">
            <!-- Card -->
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
                  <v-img :src="`https://pbs.twimg.com/media/B1BAtSlCQAAj2xG.jpg`" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">りゅう</h3>
                    <v-rating
                      v-model="rating"
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
            <!-- Card -->
          </li>
          <li class="item mx-2">
            <!-- Card -->
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
                  <v-img :src="`https://i.pinimg.com/originals/30/b2/a4/30b2a44767da51d307d88e12e180333c.jpg`" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">チュンリー</h3>
                    <v-rating
                      v-model="rating"
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
            <!-- Card -->
          </li>
          <li class="item mx-2">
            <!-- Card -->
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
                  <v-img :src="`https://i2.gamebiz.jp/images/original/194904785554389dde833ea0011.jpg`" width=144 height=144></v-img>
                  <div class="card-body">
                    <h3 class="my-1">剛拳</h3>
                    <v-rating
                      v-model="rating"
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
export default{

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
  width: 900px;
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