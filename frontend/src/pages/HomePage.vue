<template>
  <v-app>
    <div id="home-page">
      <GlobalHeader/>
      <GlobalMessage/>

      <!-- メインエリア -->
      <main class="container">
        <p class="h5 mb-4">ホーム</p>
        <b-form @submit.prevent="submitSave">
          <div class="row form-group">
            <label class="col-sm-3 col-form-label">タイトル</label>
            <div class="col-sm-8">
              <input type="text" class="form-control" v-model="form.post.title">
            </div>
          </div>
          <div class="row form-group">
            <label class="col-sm-3 col-form-label">本文</label>
            <div class="col-sm-8">
              <input type="text" class="form-control" v-model="form.post.text">
            </div>
          </div>
          <div class="row form-group">
            <label class="col-sm-3 col-form-label">価格</label>
            <div class="col-sm-8">
              <input type="text" class="form-control" v-model="form.post.price">
            </div>
          </div>
          <div class="row text-center mt-5">
            <div class="col-sm-12">
              <b-button type="submit" variant="primary">{{ isCreated ? '更新' : '登録' }}</b-button>
            </div>
          </div>
        </b-form>
      </main>
    </div>
  </v-app>
</template>

<script>
  import api from '@/services/api'
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
          post: {
            title: '',
            text: '',
            price: 0,
          }
        }
      }
    },
    computed: {
      isCreated: function () {
        console.log('これ', this.form.post.id)
        return this.form.post.id !== undefined
      }
    },
    methods: {
      // 登録・更新ボタン押下
      submitSave: function () {
        api({
          // 登録済みかどうかでHTTPメソッドとエンドポイントを切り替える
          method: this.isCreated ? 'put' : 'post',
          url: this.isCreated ? '/posts/' + this.form.post.id + '/' : '/posts/',
          data: {
            'id': this.form.post.id,
            'title': this.form.post.title,
            'text': this.form.post.text,
            'price': this.form.post.price
          }
        })
          .then(response => {
            const message = this.isCreated ? '更新しました。' : '登録しました。'
            this.$store.dispatch('message/setInfoMessage', { message: message })
            this.form.post = response.data
          })
      }
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