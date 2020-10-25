<template>
  <div id="app">
    <h1>主页</h1>
      <router-link to="/home">主页</router-link>
      <router-link to="/user">用户表</router-link>
      <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>
