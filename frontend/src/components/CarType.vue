<template>
  <div class="car_type">
    <h2>CAR SELECT</h2>

    <v-tabs
      background-color="#eee"
      color="#329eff"
      centered
    >
      <v-tab class="font_style">TOYOTA</v-tab>
      <v-tab class="font_style">HONDA</v-tab>
      <v-tab class="font_style">MAZDA</v-tab>

      <v-tab-item
        v-for="n in 3"
        :key="n"
      >
        <v-container fluid pa-0 pt-5>
          <v-row>
            <v-col cols="12" md="4" class="pa-2" v-for="car_type in car_types" :key="car_type.id">
              <v-hover
                v-slot:default="{ hover }"
                close-delay="200"
              >
                <v-card 
                  class="py-3 { 'on-hover': hover }"
                  :elevation="hover ? 12 : 2"
                  :href="car_type.en_name"
                >
                  <v-img :src="car_type.images" width=280 height=160></v-img>
                  <div class="card-body">
                    <h3 class="my-3">{{ car_type.jp_name }}</h3>
                    <p class="card-text text-uppercase">低燃費, 5人乗り, 駐無料</p>
                  </div>
                </v-card>
              </v-hover>
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>
    </v-tabs>
  </div>
</template>


<script>
import car_types from '../pages/carTypes';

export default{
  computed:{
    car_types(){
      return car_types;
    }
  },
}
</script>


<style lang="scss" scoped>
.car_type{
  width: 900px;
  margin: 0 auto;
  padding: 0 20px;
  margin-bottom: 80px;

  h2{
    font-size: 2.0rem;
    font-weight: 600;
    text-align: center;
    margin: 30px;
  }

  h3{
    font-size: 1.2rem;
    font-weight: bold;
  }

  .card-body{
    padding: 10px 20px;

    h3{
      color: #000;
    }

    p{
      font-size: 0.9rem;
      color: grey;
      margin: 0;
    }
  }

  .font_style{
    font-size: 1.0rem;
    font-weight: 600;
  }
}

.container {
  background-color: #eee;
}

.v-card:not(.on-hover) {
  transition: .2s ease-in-out;
  color: white;
}

</style>