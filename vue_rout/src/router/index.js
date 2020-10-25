import Vue from 'vue'
import Router from 'vue-router'
import User from "../components/User";
import home from "../components/home";
import users from "../components/users";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/user',
      name: 'User',
      component: User,
    },
      {
          path: '/home',
          name: 'home',
          component: home,
      },
      {
          path: '/users/:id/:name',
          name: 'users',
          component:users,
      },
      {
          path:"/",
          redirect: "/home",
      }

  ]
})
