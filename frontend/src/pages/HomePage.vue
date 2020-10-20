<template>
  <v-app>
    <GlobalHeader />
    <!-- <GlobalMessage/> -->
    <MainSlider />
    <CarType />
    <CarRecommend />
    <UserRecommend />
    <GlobalFooter />
  </v-app>
</template>


<script>
import GlobalHeader from '../components/GlobalHeader'
// import GlobalMessage from '../components/GlobalMessage'
import MainSlider from '../components/MainSlider'
import CarType from '../components/CarType'
import CarRecommend from '../components/CarRecommend'
import UserRecommend from '../components/UserRecommend'
import GlobalFooter from '../components/GlobalFooter'

export default{
  components: {
    GlobalHeader,
    // GlobalMessage,
    MainSlider,
    CarType,
    CarRecommend,
    UserRecommend,
    GlobalFooter,
  }
}
</script>


<style lang="scss" scoped>
#app{
    font-family: Rubik, "Noto Sans JP", sans-serif; 
    // Arial, "ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro", Osaka, メイリオ, Meiryo, "ＭＳ Ｐゴシック", "MS PGothic", sans-serif;
    background-color: #eee;
}

.container {
  max-width: 900px;
}

.fullheight {
    height: 100%;
}
</style>