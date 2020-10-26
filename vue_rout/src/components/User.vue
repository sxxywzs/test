<template>

    <div>
        User
        <h3>用户列表</h3>
        <table border="2">
            <tr>
                <td>ID</td>
                <td>姓名</td>
                <td>年龄</td>
                <td>个人信息</td>
                <td>操作</td>
            </tr>
            <tr v-for="user in users":key="user.id">
                <td>{{user.id}}</td>
                <td>{{user.username}}</td>
                <td>{{user.age}}</td>
                <td>{{user.content}}</td>
                <td><a href="/user#/user" @click="delete_user(user.id)">删除</a>|<a href="javascript:" @click="look_user(user.id,user.username)">查看详情</a></td>
            </tr>
        </table>
        <hr>
        请输入姓名：<input type="text" v-model="name"> <br>
        请输入年龄：<input type="text" v-model="age"> <br>
        请输入个人简介：<input type="text" v-model="content"> <br>
        <input type="button" value="提交" @click="add">

    </div>
</template>

<script>

    let User_list=function(){
        let list=[]

        localStorage.removeItem("loglevel:webpack-dev-server")
        for (let n = 0; n < localStorage.length; n++) {
            let user=localStorage.getItem(localStorage.key(n))
            console.log(user)
            list.push(JSON.parse(user))
        }

        return list
    }

export default {
name: "uesr",
    data(){
        return{
            users:User_list(),
            id:'',
            name: '',
            age: '',
            content: '',

        }
    },
    methods:{
        delete_user(id){

            localStorage.removeItem(id)
            for(let i=0;i<this.users.length;i++ ){
                let uid=this.users[i].id
                if(uid===id){
                    this.users.splice(this.users[i],1)


                }
            }

        },
        look_user(id,name){
            console.log(name)
            this.$router.push({
                path:"/users/"+id+"/"+name
            })
        },

        add() {
            if (this.name) {
                localStorage.removeItem("loglevel:webpack-dev-server")
                if(localStorage.length!==0){
                    let key = (localStorage.length)
                    console.log(localStorage.getItem(key))
                    let id = (JSON.parse(localStorage.getItem(key)).id);
                    console.log(id)
                    let new_user={id:Number(id)+1,username:this.name,age:this.age,content:this.content}
                    this.users.push(new_user)
                    localStorage.setItem(id,JSON.stringify(new_user))
                }
                else {
                    let id=1
                    let new_user={id:Number(id),username:this.name,age:this.age,content:this.content}
                    this.users.push(new_user)
                    console.log(id)
                    localStorage.setItem(id,JSON.stringify(new_user))
                }


            }
        },

    },

}

</script>

<style scoped>

</style>
