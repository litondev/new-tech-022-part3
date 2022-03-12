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

router.beforeEach((to, from,next) => {
  if(['profil','product'].includes(to.name) && !localStorage.getItem("token")){
		next({path: "/signin"});
	}else if(['signin','signup','reset-password','forgot-password'].includes(to.name) && localStorage.getItem("token")){			
		next({path: "/profil"});
	}else{
		next();
	}
});

export default router
