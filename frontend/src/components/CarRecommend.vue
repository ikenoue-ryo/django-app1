<template>
  <div calss="vertical_height2">
    <div class="car_recommend">
      <div class="car_recommend_article">
        <div class="recommend_back_size">
          <h2 class="font-weight-bold text-left dark-grey-text pb-2">Recommend You</h2>
          <hr class="w-header my-4">
        </div>
        <ul class="horizontal-list">
          <li class="item mx-2">
            <a class="card hoverable mb-4" data-toggle="modal" data-target="#basicExampleModal">
              <v-col class="pa-0">
                <v-hover
                v-slot:default="{ hover }"
                close-delay="200"
                >
                <v-card 
                  class="py-3 { 'on-hover': hover }"
                  :elevation="hover ? 12 : 2"
                >
                  <v-img :src="`https://toyota.jp/pages/contents/corollasport/001_p_001/4.0/image/car-viewer/43_1_5/43_1_5_030_c.jpg`" width=280 height=160></v-img>
                  <div class="card-body">
                    <h3 class="my-3">カローラ</h3>
                    <p class="card-text text-uppercase">低燃費, 5人乗り, 駐無料</p>
                  </div>
                </v-card>
                </v-hover>
              </v-col>
            </a>
          </li>
          <li class="item mx-2">
            <a class="card hoverable mb-4" data-toggle="modal" data-target="#basicExampleModal">
              <v-col class="pa-0">
                <v-hover
                v-slot:default="{ hover }"
                close-delay="200"
              >
                <v-card 
                  class="py-3 { 'on-hover': hover }"
                  :elevation="hover ? 12 : 2"
                >
                    <v-img :src="`https://toyota.jp/pages/contents/sienta/002_p_003/4.0/image/car-viewer/15_24_2/15_24_2_030_c.jpg`" width=280 height=160></v-img>
                    <div class="card-body">
                      <h3 class="my-3">シエンタ</h3>
                      <p class="card-text text-uppercase">低燃費, 7人乗り</p>
                    </div>
                  </v-card>
                </v-hover>
              </v-col>
            </a>
          </li>
          <li class="item mx-2">
            <a class="card hoverable mb-4" data-toggle="modal" data-target="#basicExampleModal">
              <v-col class="pa-0">
                <v-hover
                v-slot:default="{ hover }"
                close-delay="200"
                >
                  <v-card 
                    class="py-3 { 'on-hover': hover }"
                    :elevation="hover ? 12 : 2"
                  >
                    <v-img :src="`https://toyota.jp/pages/contents/aqua/001_p_011/4.0/image/car-viewer/1_6_9/1_6_9_030_c.jpg`" width=280 height=160></v-img>
                    <div class="card-body">
                      <h3 class="my-3">アクア</h3>
                      <p class="card-text text-uppercase">5人乗り, 駐無料</p>
                    </div>
                  </v-card>
                </v-hover>
              </v-col>
            </a>
          </li>
          <li class="item mx-2">
            <a class="card hoverable mb-4" data-toggle="modal" data-target="#basicExampleModal">
              <v-col class="pa-0">
                <v-hover
                  v-slot:default="{ hover }"
                  close-delay="200"
                >
                  <v-card 
                    class="py-3 { 'on-hover': hover }"
                    :elevation="hover ? 12 : 2"
                  >
                    <v-img :src="`https://toyota.jp/pages/contents/voxy/003_p_007/4.0/image/car-viewer/11_1_1/11_1_1_030_c.jpg`" width=280 height=160></v-img>
                    <div class="card-body">
                      <h3 class="my-3">ヴォクシー</h3>
                      <p class="card-text text-uppercase">低燃費, 5人乗り, 駐無料</p>
                    </div>
                  </v-card>
                </v-hover>
              </v-col>
            </a>
          </li>
          <li class="item mx-2">
            <a class="card hoverable mb-4" data-toggle="modal" data-target="#basicExampleModal">
              <v-col class="pa-0">
                <v-hover
                  v-slot:default="{ hover }"
                  close-delay="200"
                >
                  <v-card 
                    class="py-3 { 'on-hover': hover }"
                    :elevation="hover ? 12 : 2"
                  >
                    <v-img :src="`https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/car-viewer/24_5_7/24_5_7_030_c.jpg`" width=280 height=160></v-img>
                    <div class="card-body">
                      <h3 class="my-3">プリウス</h3>
                      <p class="card-text text-uppercase">低燃費, 5人乗り</p>
                    </div>
                  </v-card>
                </v-hover>
              </v-col>
            </a>
          </li>
          <li class="item mx-2">
            <a class="card hoverable mb-4" data-toggle="modal" data-target="#basicExampleModal">
              <v-col class="pa-0">
                <v-hover
                  v-slot:default="{ hover }"
                  close-delay="200"
                >
                  <v-card 
                    class="py-3 { 'on-hover': hover }"
                    :elevation="hover ? 12 : 2"
                  >
                    <v-img :src="`https://toyota.jp/pages/contents/alphard/003_p_009/image/car-viewer/9_20_6/9_20_6_030_c.jpg`" width=280 height=160></v-img>
                    <div class="card-body">
                      <h3 class="my-3">アルファード</h3>
                      <p class="card-text text-uppercase">低燃費, 5人乗り, 駐無料</p>
                    </div>
                  </v-card>
                </v-hover>
              </v-col>
            </a>
          </li>
          <li class="item mx-2">
            <a class="card hoverable mb-4" data-toggle="modal" data-target="#basicExampleModal">
              <v-col class="pa-0">
                <v-hover
                  v-slot:default="{ hover }"
                  close-delay="200"
                >
                  <v-card 
                    class="py-3 { 'on-hover': hover }"
                    :elevation="hover ? 12 : 2"
                  >
                    <v-img :src="`https://toyota.jp/pages/contents/sienta/002_p_003/4.0/image/car-viewer/15_24_2/15_24_2_030_c.jpg`" width=280 height=160></v-img>
                    <div class="card-body">
                      <h3 class="my-3">シエンタ</h3>
                      <p class="card-text text-uppercase">低燃費, 5人乗り, 駐無料</p>
                    </div>
                  </v-card>
                </v-hover>
              </v-col>
            </a>
          </li>
        </ul>
        <div class="back_size">
          <div class="my-2 back-color">
            <v-btn><span class="ml-3">もっと見る</span><v-icon color="white">mdi-chevron-right</v-icon></v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default{

}
</script>


<style lang="scss" scoped>
p {
  color: grey;
}

.w-header{
  width: 50px;
}

.back-color{
  padding: 0 30px;
  
  button{
    background-color: #333!important;
    width: 150px;
    padding: 20px;
    font-size: 0.9rem;
    color: #fff;
    font-weight: bold;
    border-radius: 50px;
    padding: 25px!important;
  }
}

.car_recommend_article {
  background: #e2ebf3;
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
  padding-left: calc(50% - 445px);
  margin: 0;
}

.car_recommend_article li.item {
  display: inline-block;
  margin: 14px;
}

.car_recommend_article a.card {
  margin: 0 !important;
  text-decoration: none;
}

.car_recommend_article .tab-pane {
  width: 900px;
  margin: 20px auto;
}

.car_recommend_article .back_size {
  margin: 30px auto 0;
}

.car_recommend_article .back_size .more_button {
  margin: 0 20px;
}

.car_recommend_article .back_size .more_button button {
  background: #333;
  color: #fff;
  border-radius: 50px;
  font-size: 1rem;
  padding: 13px;
  width: 150px;
}

.v-icon{
  color: #fff;
}

img.card-img-top {
  width: 280;
  height: 160px;
  object-fit: cover;
}

.card-body{
    padding: 10px 20px;

    h3{
      color: #000;
      font-size: 1.2rem;
      font-weight: bold;
    }

    p{
      font-size: 0.9rem;
      color: grey;
      margin: 0;
    }
}

.v-card:not(.on-hover) {
  transition: .2s ease-in-out;
}
</style>