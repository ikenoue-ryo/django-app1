<template>
  <v-app class="app">
    <GlobalHeader />
    <div class="app_flex">
      <div style="width: 100%;">

        <div class="back_body">
          <h2>{{ car_name.toUpperCase()}}</h2>
          <v-list v-if="car_info && car_info.length > 0">
            <v-list-item v-for="info in car_info" :key="info.index">
                <v-container fluid class="back_color">
                  <v-content>
                    <v-list-item :to="`/post_preview/${info.id}`" style="background-color: #fff; border-radius:10px;">
                      <v-container>
                        <v-layout wrap>
                          <v-flex xs12 sm6 md5>
                            <div class="back_size">
                              <img :src="info.photo">
                            </div>
                          </v-flex>
                          <v-flex xs12 sm6 md7 class="pad_class">
                            <div class="card_detail">
                                <div class="card_info clearfix">
                                  <h3>{{ info.place }}</h3>
                                  <v-btn
                                    large
                                    icon
                                    color="pink"
                                  >
                                    <v-icon>mdi-heart</v-icon>
                                  </v-btn>
                                  <ul>
                                    <li v-if="info.pr1">{{ info.pr1 }}</li>
                                    <li v-if="info.pr2">{{ info.pr2 }}</li>
                                    <li v-if="info.pr3">{{ info.pr3 }}</li>
                                    <li v-if="info.pr4">{{ info.pr4 }}</li>
                                  </ul>
                                  <ul class="tag" v-if="info.tag">
                                      <li v-for="tag in info.tag" :key="tag"># {{ tag.name }}</li>
                                  </ul>
                                  <div class="price">{{ info.price.toLocaleString() }}
                                    <span class="yen"> 円/(月額)</span>
                                  </div>
                                </div>
                            </div>
                          </v-flex>

                        </v-layout>
                      </v-container>
                    </v-list-item>
                  </v-content>
                </v-container>
            </v-list-item>
          </v-list>
          <div v-else class="non_contents">
            <p>投稿がありません</p>
          </div>
        </div>
      </div>
    </div>
    <GlobalFooter />
  </v-app>
</template>

<script>
import GlobalHeader from '../components/GlobalHeader';
import GlobalFooter from '../components/GlobalFooter';
import axios from 'axios'

export default {
  components:{
    GlobalHeader,
    GlobalFooter,
  },
  data () {
    return {
    post_list: [],

    // カルーセル
    model: 0,
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
    car_name(){
      const name = this.$route.params.en_name
      return name
    },
    car_info(){
      const post_list = this.post_list.filter(post_list => post_list.car_type === this.car_name)
      return post_list
    },
  },
  methods: {
    pageChange: function(pageNumber){
      this.displayLists = this.lists.slice(this.pageSize*(pageNumber -1), this.pageSize*(pageNumber));
    },
  },
  mounted: function(){
    //post
    axios.get('http://localhost:1337/api/v1/posts/')
    .then(response => { this.post_list = response.data })
  }
}
</script>


<style lang="scss" scoped>
.app{
  display: flex;
  flex-direction: column;

  .app_flex{
    display: flex;
    flex-grow: 1;
    background-color: #eee;
  }
}

.container{
  background: #fff;
  a{
    padding: 10px;
    text-decoration: none;
  }
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

  .back_color {
    background-color: #eee;
    overflow: hidden;
    width: 900px;
    
    .v-content{
      border: 1px solid #ddd;
      border-radius:10px;
    }
  }

  .v-list{
    background-color: #eee;
    padding: 0;
    margin-bottom: 40px;
  }
}

.header_class {
  font-family: Rubik, "Noto Sans JP", sans-serif;
}



.price {
  font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto, "Helvetica Neue", sans-serif !important;
  font-size: 1.2rem;
  font-weight: 500;
  margin: 10px 0;
  text-align: right;
  position: absolute;
  bottom: 33px;
  right: 20px;

  span.yen {
    font-size: 0.9rem;
  }
}

.card_info{
  width: 100%;
  height: 185px;

  h3{
    font-size: 1.2rem;
    margin: 10px 0;
  }
  
  ul{
    font-size: 1.1rem;

    li{
      font-size: 1rem;
      line-height: 1.8;
    }
  }

  ul.tag {
    margin: 0;
    padding: 0;
    position: absolute;
    bottom: 40px;
    width: 40%;

    li {
        display: inline-block;
        font-size: 0.9rem;
        margin: 0 5px;
        padding: 3px 10px;
        border-radius: 6px;
        font-weight: 500;
        border: solid 2px #dce4ec;
        font-weight: 600;
    }
  }
}

.pagenation{
  margin: 50px;
}

.back_size{
  width: 100%;

  img{
    width: 100%;
    margin: 10px 0;
  }
}

.v-image{
    z-index: 10;
}

.v-btn{
  display: inline;
  float: right;
  bottom: 42px;
  left: 20px;
}

.clearfix::after {
   content: "";
   display: block;
   clear: both;
}

.non_contents{
  margin: 0 auto;
  text-align: center;
  padding: 50px;
}

</style>