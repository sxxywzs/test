<template>
    <div>
        <p>欢迎来到主页</p>
        <button @click="add_user">一键清空并快速添加用户</button>
    </div>
</template>

<script>
import users from "./users";

export default {
    name: "home",
    methods:{
        add_user(){
            localStorage.clear()
            let user1= {id:1,username:"jason",age:18,content:"我是jason"}
            let user2= {id:2,username:"lenny",age:19,content:"我是lenny"}
            let user3= {id:3,username:"rex",age:30,content:"我是rex"}
            localStorage.setItem(user1.id,JSON.stringify(user1))
            localStorage.setItem(user2.id,JSON.stringify(user2))
            localStorage.setItem(user3.id,JSON.stringify(user3))
            localStorage.removeItem("loglevel:webpack-dev-server")

        }
    }
}


</script>

<style scoped>

</style>
