<template>
  <div class="back_body">
    <GlobalHeader />

    <h2>Let's SignUp</h2>
    <v-card
      class="card_style"
      max-width="800"
    >
      <v-form v-model="form.valid" @submit.prevent="submitSignup">
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
                    v-model="form.email"
                    :rules="form.emailRules"
                    label="メールアドレス"
                    required
                  ></v-text-field>
                </v-col>

                <!-- <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    v-model="form.profname"
                    :rules="form.nameRules"
                    :counter="10"
                    label="ユーザーネーム"
                    required
                  ></v-text-field>
                </v-col> -->

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

                <!-- <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    v-model="form.password2"
                    :rules="form.nameRules"
                    :counter="10"
                    label="パスワード(確認用)"
                    required
                  ></v-text-field>
                </v-col> -->

              </v-row>
              <div class="back-color">
                  <v-btn href="submit" class="start">この内容ではじめる</v-btn>
              </div>
            </v-container>
          </v-flex>

        </v-layout>
      </v-form>
    </v-card>
  </div>

</template>



<script>
import GlobalHeader from '../components/GlobalHeader'

export default {
  components: {
    GlobalHeader,
  },
  data (){
    return {
      form: {
        valid: false,
        // profname: '',
        password: '',
        // password2: '',
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
      // サインアップボタン押下
      submitSignup: function () {
        // サインアップ
        this.$store.dispatch('auth/signup', {
          email: this.form.email,
          password: this.form.password
        })
          .then(() => {
            console.log('Signup succeeded.')
            this.$store.dispatch('message/setInfoMessage', { message: 'サインアップしました。' })
            // クエリ文字列に「next」がなければ、ホーム画面へ
            const next = this.$route.query.next || '/login'
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

    .back-color{
      a.start{
        background-color: #329eff!important;
        font-size: 0.9rem;
        color: #fff;
        font-weight: bold;
        margin-top: 20px;
        padding: 20px;
        text-decoration: none;
      }
    }
  }
}
</style>