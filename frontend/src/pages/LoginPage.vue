<template>
  <div class="back_body">
    <GlobalHeader />

    <h2>Let's Login</h2>
    <v-card
      class="card_style"
      max-width="800"
    >
      <v-form v-model="form.valid" @submit.prevent="submitLogin">
        <v-layout wrap>
          <v-flex xs12 sm6 md3><img src="@/assets/img/superman.png" width="115"></v-flex>
          <v-flex xs12 sm6 md9>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    type="email"
                    v-model="form.email"
                    :rules="form.emailRules"
                    label="メールアドレス"
                    required
                  ></v-text-field>
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    v-model="form.password"
                    type="password"
                    label="パスワード"
                    required
                  ></v-text-field>
                </v-col>

              </v-row>
              <div class="back-color">
                  <v-btn type="submit" class="start">ログイン</v-btn>
              </div>
            </v-container>
          </v-flex>

        </v-layout>
      </v-form>
    </v-card>
  </div>

</template>



<script>
import GlobalHeader from '@/components/GlobalHeader.vue'

export default {
  components: {
    GlobalHeader,
  },
  data (){
    return {
      form: {
        valid: false,
        password: '',
        nameRules: [
          v => !!v || 'Name is required',
          v => v.length <= 10 || 'Name must be less than 10 characters',
        ],
        email: '',
        emailRules: [
          v => !!v || 'E-mail is required',
          v => /.+@.+/.test(v) || 'E-mail must be valid',
        ],
      }
    }
  },
  methods: {
      // ログインボタン押下
      submitLogin: function () {
        // ログイン
        this.$store.dispatch('auth/login', {
          email: this.form.email,
          password: this.form.password
        })
          .then(() => {
            console.log('Login succeeded.')
            this.$store.dispatch('message/setInfoMessage', { message: 'ログインしました。' })
            // クエリ文字列に「next」がなければ、ホーム画面へ
            const next = this.$route.query.next || '/'
            this.$router.replace(next)
          })
      }
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
    margin: 30px auto;
    padding: 50px;
    border-top: 5px solid #33b5e5;

    img {
      width: 120px;
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
</style>