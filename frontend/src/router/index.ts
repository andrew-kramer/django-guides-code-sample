import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import EmailConfirm from '../views/auth/EmailConfirm.vue'
import Home from '../views/Home.vue'
import Login from '../views/auth/Login.vue'
import Register from '../views/auth/Register.vue'
import ResetConfirm from '../views/auth/ResetConfirm.vue'
import PasswordReset from '../views/auth/PasswordReset.vue'
import PageNotFound from '../views/PageNotFound.vue'

const routes: Array<RouteRecordRaw> = [

  // Home Page

  {
    path: '/',
    name: 'Home',
    component: Home
  },

  // Authentication

  {
    path: '/login',
    name: 'Login',
    component: Login
  },

  {
    path: '/register',
    name: 'Register',
    component: Register
  },

  {
    path: '/password-reset',
    name: 'Reset Password',
    component: PasswordReset
  },

  {
    path: '/password-reset/confirm/:uidb64/:token',
    name: 'Confirm Reset Password',
    component: ResetConfirm,
    props: true
  },

  {
    path: '/confirm-email/:token',
    name: 'Confirm Email',
    component: EmailConfirm,
    props: true
  },

  // Site Pages
  // Error 404

  {
    path: '/:catchAll(.*)*',
    name: 'PageNotFound',
    component: PageNotFound
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
