<template>
  <v-app>
  <div class="back_body">
    <GlobalHeader />

    <h2>Message {{ messages }}</h2>
    <v-card
      class="card_style"
      max-width="800"
    >
      
        <v-layout wrap>
          <v-flex xs12 sm6 md12 text-center>

            <v-card>
              <v-toolbar
                flat
                color="primary"
                dark
              >
                <v-toolbar-title>User Profile</v-toolbar-title>
              </v-toolbar>
              <v-tabs vertical>
                <v-tab v-for="message in messages" :key="message">
                  {{ message.sender }}
                </v-tab>
                <!-- <v-tab>
                  <v-icon left>
                    mdi-lock
                  </v-icon>
                  Option 2
                </v-tab>
                <v-tab>
                  <v-icon left>
                    mdi-access-point
                  </v-icon>
                  Option 3
                </v-tab> -->

                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <p v-for="message in messages" :key="message">
                        <span>{{ message.message }}</span>
                      </p>

                      <p>
                        Nam ipsum risus, rutrum vitae, vestibulum eu, molestie vel, lacus. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Aliquam lobortis. Aliquam lobortis. Suspendisse non nisl sit amet velit hendrerit rutrum.
                      </p>

                      <p class="mb-0">
                        Phasellus dolor. Fusce neque. Fusce fermentum odio nec arcu. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Phasellus blandit leo ut odio.
                      </p>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <p>
                        Morbi nec metus. Suspendisse faucibus, nunc et pellentesque egestas, lacus ante convallis tellus, vitae iaculis lacus elit id tortor. Sed mollis, eros et ultrices tempus, mauris ipsum aliquam libero, non adipiscing dolor urna a orci. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Nunc sed turpis.
                      </p>

                      <p>
                        Suspendisse feugiat. Suspendisse faucibus, nunc et pellentesque egestas, lacus ante convallis tellus, vitae iaculis lacus elit id tortor. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In hac habitasse platea dictumst. Fusce ac felis sit amet ligula pharetra condimentum.
                      </p>

                      <p>
                        Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Nam commodo suscipit quam. In consectetuer turpis ut velit. Sed cursus turpis vitae tortor. Aliquam eu nunc.
                      </p>

                      <p>
                        Etiam ut purus mattis mauris sodales aliquam. Ut varius tincidunt libero. Aenean viverra rhoncus pede. Duis leo. Fusce fermentum odio nec arcu.
                      </p>

                      <p class="mb-0">
                        Donec venenatis vulputate lorem. Aenean viverra rhoncus pede. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. Fusce commodo aliquam arcu. Suspendisse enim turpis, dictum sed, iaculis a, condimentum nec, nisi.
                      </p>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <p>
                        Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna, posuere eget, vestibulum et, tempor auctor, justo.
                      </p>

                      <p class="mb-0">
                        Cras sagittis. Phasellus nec sem in justo pellentesque facilisis. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at tortor in tellus interdum sagittis.
                      </p>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
              </v-tabs>
            </v-card>      

          </v-flex>
        </v-layout>

        <div class="message_area">
          <v-text-field
            label="Message"
            hide-details="auto"
          ></v-text-field>
        </div>
    </v-card>
  </div>
  </v-app>
</template>


<script>
import GlobalHeader from '@/components/GlobalHeader.vue'
// import GlobalMessage from '@/components/GlobalMessage.vue'
import axios from 'axios'
// import api from '@/services/api'


export default {
  name: 'Map',
  components: {
    GlobalHeader,
    // GlobalMessage,
  },
  data(){
    return {
      profiles: [],
      message: [],
      id : this.$store.getters['auth/id'],
      name : this.$store.getters['auth/username'],
      //メッセージ
      selectedItem: 1,
      items: [
        { text: 'Real-Time', icon: 'mdi-clock' },
        { text: 'Audience', icon: 'mdi-account' },
        { text: 'Conversions', icon: 'mdi-flag' },
      ],
    }
  },
  async mounted(){
    //profile
    axios.get('http://localhost:1337/api/v1/profile/')
    .then(response => { this.profiles = response.data })

    //message
    axios.get('http://localhost:1337/api/v1/inbox/')
    .then(response => { this.message = response.data })

  },
  computed: {
    user_id(){
      return this.$store.getters['auth/id']
    },
    username(){
      return this.$store.getters['auth/username']
    },
    user_profile(){
      const profiles = this.profiles.find(profiles => profiles.userpro.username === this.$route.params.username)
      if(!profiles){
        return {
          title: '見つかりません',
          text: '見つかりません',
        }
      }
      console.log('profiles', profiles)
      return profiles
    },
    messages(){
      console.log('あああ', this.user_id)
      const my_message = this.message.filter(message => message.receiver.username === this.$route.params.username)
      return my_message
    },
    one_messages(){
      const my_message = this.message.filter(message => message.receiver.username === this.$route.params.username)
      return my_message
    },
    // message_list(){
    //   const message_lists = this.message.filter(message => message.receiver === 1)
    //   return message_lists
    // }
  }
}
</script>


<style lang="scss" scoped>
.back_body{
  background-color: #eee;
  overflow: hidden;
  min-height: 100vh;

  h2{
    text-align: center;
    font-size: 45px;
    font-weight: 600;
    text-align: center;
    margin: 30px;
  }

  .card_style{
    min-height: 500px;
    margin: 30px auto;
    padding: 0;
    border-top: 5px solid #33b5e5;

    h1{
      font-size: 2.0rem;
      text-align: left;
      margin: 0;
    }

    h2{
      font-size: 1.4rem;
      text-align: left;
      margin: 20px 0;
    }

    p{
      font-size: 1rem;
      text-align: justify;
    }

    .back-color{
      button.start{
        background-color: #329eff!important;
        font-size: 0.9rem;
        color: #fff;
        font-weight: bold;
        margin-top: 20px;
        padding: 20px;
        text-decoration: none;
        outline: none;
      }
    }
  }
}

.border_line{
  border: 1px solid #EBEBEB;
  width: 100%;
}

.profile_icons{
  img{
    width: 50px;
    border-radius: 50%;
    border: 1px solid grey;
  }
}

.message_area{
  width: 500px;
  float: right;
  margin: 25px 20px;
  width: 78%;
}
</style>