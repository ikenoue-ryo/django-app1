import Vue from "vue";
import VueRouter from "vue-router";
import HomePage from "@/pages/HomePage";
import LoginPage from "@/pages/LoginPage";
import SignUpPage from "@/pages/SignUpPage";
import PostPage from "@/pages/PostPage";
import PostPreviewPage from "@/pages/PostPreviewPage";
import PostDetail from "@/pages/PostDetail";
import PostList from "@/pages/PostList";
import ProfilePage from "@/pages/ProfilePage";
import MessagePage from "@/pages/MessagePage";
import notFound from "@/pages/notFound";
import store from "@/store";

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  // ログインが必要な画面には「requiresAuth」フラグを付けておく
  routes: [
    { path: "/", component: HomePage, meta: { requiresAuth: true } },
    { path: "/login", component: LoginPage },
    { path: "/signup", component: SignUpPage },
    { path: "/post", component: PostPage, meta: { requiresAuth: true } },
    { path: "/post_preview/:id", component: PostPreviewPage, meta: { requiresAuth: true } },
    { path: "/:en_name", component: PostList },
    { path: "/post/:id", component: PostDetail },
    { path: "/profile/:username", component: ProfilePage, meta: { requiresAuth: true } },
    { path: "/message/:username", component: MessagePage, meta: { requiresAuth: true }},
    { path: "*", component: notFound, meta: { title: "ページが見つかりません" }},
    // { path: "*", redirect: "/" },
  ],
});

/**
 * Routerによって画面遷移する際に毎回実行される
 */
router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters["auth/isLoggedIn"];
  const token = localStorage.getItem("access");
  console.log("to.path=", to.path);
  console.log("isLoggedIn=", isLoggedIn);

  // ログインが必要な画面に遷移しようとした場合
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // ログインしている状態の場合
    if (isLoggedIn) {
      console.log("User is already logged in. So, free to next.");
      next();

      // ログインしていない状態の場合
    } else {
      // まだ認証用トークンが残っていればユーザー情報を再取得
      if (token != null) {
        console.log("User is not logged in. Trying to reload again.");

        store
          .dispatch("auth/reload")
          .then(() => {
            // 再取得できたらそのまま次へ
            console.log("Succeeded to reload. So, free to next.");
            next();
          })
          .catch(() => {
            // 再取得できなければログイン画面へ
            forceToLoginPage(to, from, next);
          });
      } else {
        // 認証用トークンが無い場合は、ログイン画面へ
        forceToLoginPage(to, from, next);
      }
    }
  } else {
    // ログインが不要な画面であればそのまま次へ
    console.log("Go to public page.");
    next();
  }
});

/**
 * ログイン画面へ強制送還
 */
function forceToLoginPage(to, from, next) {
  console.log("Force user to login page.");
  next({
    path: "/login",
    // 遷移先のURLはクエリ文字列として付加
    query: { next: to.fullPath },
  });
}

export default router;