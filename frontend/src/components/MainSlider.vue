<template>
  <v-container fluid>
    <v-layout wrap class="main_img">
        <div>
          <v-carousel cycle interval="4000" class="rounded-lg">
            <v-carousel-item
              v-for="(photo, index) in photos"
              :key="index"
            >
              <v-row>
                <v-col class="mt-3">
                  <v-img 
                  :src="photo.image"
                  max-width=860 class="rounded-lg"
                  ></v-img>
                </v-col>
              </v-row>
            </v-carousel-item>
          </v-carousel>
        </div>
    </v-layout>
    <div class="post-car">
      <a href="/post" class="btn btn--circle user-post"><v-icon color="white">mdi-camera</v-icon></a>
    </div>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        photos: [
          {
            image: 'https://www.honda.co.jp/top-page/common/img/visual/FIT_200213.jpg'
          },
          {
            image: 'https://tk.ismcdn.jp/mwimgs/2/8/1140/img_285d39a114000a05feb109d7fb224bde302851.jpg'
          },
          {
            image: 'https://media.safarilounge.jp/online/thegear/content/theme/img/org/article/947/slider_5b0d3ad0b6c83_2.jpg?t=1577411173'
          },
          {
            image: 'https://www.honda.co.jp/top-page/common/img/visual/FIT_200213.jpg'
          },
          {
            image: 'https://tk.ismcdn.jp/mwimgs/2/8/1140/img_285d39a114000a05feb109d7fb224bde302851.jpg'
          },
        ],
      }
    },
  }
</script>

<style lang="scss" scoped>
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

</style>
