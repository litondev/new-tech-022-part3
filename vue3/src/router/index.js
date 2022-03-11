import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : "/signin",
      name : "signin",
      component : () => import("../views/Signin.vue")
    },
    {
      path : "/signup",
      name : "signup",
      component : () => import("../views/Signup.vue")
    },
    {
      path : "/reset-password",
      name : "reset-password",
      component : () => import("../views/ResetPassword.vue")
    },
    {
      path : "/forgot-password",
      name : "forgot-password",
      component : () => import("../views/ForgotPassword.vue")
    },
    {
      path : "/product",
      name : "product",
      component : () => import("../views/Product.vue")
    },
    {
      path : "/profil",
      name : "profil",
      component : () => import("../views/Profil.vue")
    }
  ]
})

router.beforeEach((to, from) => {
  console.log("Oke");
});

export default router
