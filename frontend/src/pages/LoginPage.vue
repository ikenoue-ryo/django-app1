<template>
  <div id="login-page">
    <GlobalHeader/>
    <GlobalMessage/>

    <!-- メインエリア -->
    <main class="container">
      <p class="h5 mb-4">ログイン</p>
      <b-form @submit.prevent="submitLogin">
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">メールアドレス</label>
          <div class="col-sm-8">
            <b-form-input type="email" v-model="form.email" required/>
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">パスワード</label>
          <div class="col-sm-8">
            <b-form-input type="password" v-model="form.password" required/>
          </div>
        </div>
        <div class="row text-center mt-5">
          <div class="col-sm-12">
            <b-button type="submit" variant="primary">ログイン</b-button>
          </div>
        </div>
      </b-form>
    </main>
  </div>
</template>

<script>
  import GlobalHeader from '@/components/GlobalHeader.vue'
  import GlobalMessage from '@/components/GlobalMessage.vue'
  export default {
    components: {
      GlobalHeader,
      GlobalMessage
    },
    data () {
      return {
        form: {
          email: '',
          password: ''
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