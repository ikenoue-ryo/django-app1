import axios from 'axios'
import store from '@/store'

const api = axios.create({
  baseURL: process.env.VUE_APP_ROOT_API,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest'
  }
})

// リクエストを送る前の共通処理
api.interceptors.request.use(function (config) {
  // メッセージをクリア
  store.dispatch('message/clearMessages')
  // 認証用トークンがあればリクエストヘッダに乗せる
  const token = localStorage.getItem('access')
  // console.log('トークン', localStorage.getItem("access"));
  if (token) {
    config.headers.Authorization = 'JWT ' + token
    return config
  }
  return config
}, function (error) {
  return Promise.reject(error)
})

// 共通エラー処理
api.interceptors.response.use(function (response) {
  return response
}, function (error) {
  console.log('error.response=', error.response)
  const status = error.response ? error.response.status : 500

  // エラーの内容に応じてstoreのメッセージを更新
  let message
  if (status === 400) {
    // バリデーションNG
    let messages = [].concat.apply([], Object.values(error.response.data))
    store.dispatch('message/setWarningMessages', {
      messages: messages
    })

  } else if (status === 401) {
    // 認証エラー
    const token = localStorage.getItem('access')
    if (token != null) {
      message = 'ログイン有効期限切れ'
    } else {
      message = '認証エラー'
    }
    store.dispatch('auth/logout')
    store.dispatch('message/setErrorMessage', {
      message: message
    })

  } else if (status === 403) {
    // 権限エラー
    message = '権限エラーです。'
    store.dispatch('message/setErrorMessage', {
      message: message
    })

  } else {
    // その他のエラー
    message = '想定外のエラーです。'
    store.dispatch('message/setErrorMessage', {
      message: message
    })
  }
  return Promise.reject(error)
})

export default api