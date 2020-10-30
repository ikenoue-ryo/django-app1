import Vue from 'vue'
import VueMeta from 'vue-meta'

// BootstrapVue
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import App from './App.vue'
import router from './router'
import store from './store'

import vuetify from './plugins/vuetify';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
import { fab } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

// アイコンを読み込み
library.add(fas, far, fab);

// Vueコンポーネントを作成
Vue.component('v-fa', FontAwesomeIcon);

Vue.config.productionTip = process.env.NODE_ENV === 'production'
Vue.use(BootstrapVue)
Vue.use(VueMeta)

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
