import Vue from 'vue'
import Vuex from 'vuex'
import api from '@/services/api'

Vue.use(Vuex)

// 認証情報
const authModule = {
  strict: process.env.NODE_ENV !== 'production',
  namespaced: true,
  state: {
    id: '',
    username: '',
    isLoggedIn: false
  },
  getters: {
    id: state => state.id,
    username: state => state.username,
    isLoggedIn: state => state.isLoggedIn
  },
  mutations: {
    set(state, payload) {
      state.id = payload.user.id
      state.username = payload.user.username
      state.isLoggedIn = true
    },
    clear(state) {
      state.id = ''
      state.username = ''
      state.isLoggedIn = false
    }
  },
  actions: {
    /**
     * サインアップ
     */
    signup(context, payload) {
      return api.post('/auth/users/', {
          'email': payload.email,
          'username': payload.username,
          'password': payload.password
        })
    },
    /**
     * ログイン
     */
    login(context, payload) {
      return api.post('/auth/jwt/create/', {
          'email': payload.email,
          'password': payload.password
        })
        .then(response => {
          // 認証用トークンをlocalStorageに保存
          localStorage.setItem('access', response.data.access)
          // ユーザー情報を取得してstoreのユーザー情報を更新
          return context.dispatch('reload')
        })
    },
    /**
     * ログアウト
     */
    logout(context) {
      // 認証用トークンをlocalStorageから削除
      localStorage.removeItem('access')
      // storeのユーザー情報をクリア
      context.commit('clear')
      console.log('ログアウトしました')
    },
    /**
     * ユーザー情報更新
     */
    reload(context) {
      return api.get('/auth/users/me/')
        .then(response => {
          const user = response.data
          // storeのユーザー情報を更新
          context.commit('set', {
            user: user
          })
          return user
        })
    }
  }
}

// グローバルメッセージ
const messageModule = {
  strict: process.env.NODE_ENV !== 'production',
  namespaced: true,
  state: {
    error: '',
    warnings: [],
    info: ''
  },
  getters: {
    error: state => state.error,
    warnings: state => state.warnings,
    info: state => state.info
  },
  mutations: {
    set(state, payload) {
      if (payload.error) {
        state.error = payload.error
      }
      if (payload.warnings) {
        state.warnings = payload.warnings
      }
      if (payload.info) {
        state.info = payload.info
      }
    },
    clear(state) {
      state.error = ''
      state.warnings = []
      state.info = ''
    }
  },
  actions: {
    /**
     * エラーメッセージ表示
     */
    setErrorMessage(context, payload) {
      context.commit('clear')
      context.commit('set', {
        'error': payload.message
      })
    },
    /**
     * 警告メッセージ（複数）表示
     */
    setWarningMessages(context, payload) {
      context.commit('clear')
      context.commit('set', {
        'warnings': payload.messages
      })
    },
    /**
     * インフォメーションメッセージ表示
     */
    setInfoMessage(context, payload) {
      context.commit('clear')
      context.commit('set', {
        'info': payload.message
      })
    },
    /**
     * 全メッセージ削除
     */
    clearMessages(context) {
      context.commit('clear')
    }
  }
}

// 404
const windowModule = {
  strict: process.env.NODE_ENV !== 'production',
  namespaced: true,
  state: {
    notFound: false,
  },
  getters: {
    isNotFound(state) {
      return state.notFound
    }
  },
  mutations: {
    setNotFound(state, val) {
      state.notFound = val
    }
  },
}

const store = new Vuex.Store({
  modules: {
    auth: authModule,
    message: messageModule,
    window: windowModule
  }
})

export default store