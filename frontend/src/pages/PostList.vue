<template>
  <v-app>
    <GlobalHeader />

    <div class="back_body">
      <h2>Let's Ride {{ car_type.en_name }}</h2>
          <v-list>
            <v-list-item v-for="list in displayLists" :key="list.index">
                <v-container fluid class="back_color">
                  <v-content>
                    <v-list-item :to="`/post/${list.id}`" style="background-color: #fff; border-radius:10px;">
                      <v-container>
                        <v-layout wrap>
                          <v-flex xs12 sm6 md5>
                            <div class="back_size">
                              <img :src="list.main_images[0].photo">
                            </div>
                          </v-flex>
                          <v-flex xs12 sm6 md7 px-5>
                            <div class="card_detail">
                                <div class="card_info clearfix">
                                  <h3>{{ list.address }}</h3>
                                  <v-btn
                                    large
                                    icon
                                    color="pink"
                                  >
                                    <v-icon>mdi-heart</v-icon>
                                  </v-btn>

                                  <ul>
                                    <li v-if="list.pr1">{{ list.pr1 }}</li>
                                    <li v-if="list.pr2">{{ list.pr2 }}</li>
                                    <li v-if="list.pr3">{{ list.pr3 }}</li>
                                    <li v-if="list.pr4">{{ list.pr4 }}</li>
                                  </ul>
                                  <ul class="tag">
                                    <li v-if="list.tag1">{{ list.tag1 }}</li>
                                    <li v-if="list.tag2">{{ list.tag2 }}</li>
                                  </ul>
                                  <div class="price">{{ list.price }}
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

          <!-- ページネーション -->
          <div class="text-center pagenation">
            <v-pagination
              v-model="page"
              :length="length"
              prev-icon="mdi-menu-left"
              next-icon="mdi-menu-right"
              @input="pageChange"
            ></v-pagination>
          </div>
        </div>
    
    <GlobalFooter />
  </v-app>
</template>

<script>
import GlobalHeader from '../components/GlobalHeader';
import GlobalFooter from '../components/GlobalFooter';
import car_types from '../pages/carTypes';
import posts from '../pages/postLists';

export default {
  components:{
    GlobalHeader,
    GlobalFooter,
  },
  data () {
    return {
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
    // ページネーション
    page: 1,
    length: 0,
    lists: [],
    displayLists: [],
    pageSize: 3,
    }
  },
  computed:{
    car_types(){
      return this.$route.params.en_name
    },
    car_type(){
      return car_types.find(car_type => car_type.en_name === this.car_types)
    },
    posts(){
      const post = posts.filter(posts => posts.car_type === this.car_types);
      if (!posts) {
        return {
          author: '見つかりません',
          car_type: '',
          title: '',
          text: '',
        };
      }
      return post
    },
  },
  methods: {
    pageChange: function(pageNumber){
      this.displayLists = this.lists.slice(this.pageSize*(pageNumber -1), this.pageSize*(pageNumber));
    }
  },
  mounted: function(){
    this.lists = this.posts

    this.length = Math.ceil(this.lists.length/this.pageSize);

    this.displayLists = this.lists.slice(this.pageSize*(this.page -1), this.pageSize*(this.page));
  }
}
</script>


<style lang="scss" scoped>
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


</style>