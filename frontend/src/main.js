import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import http from './plugins/http.js'
import Index from './pages/index.vue'
import Board from './pages/board/index.vue'
import Posts from './pages/board/posts/index.vue'
import PostsWrite from './pages/board/posts/write.vue'
import UserCreate from './pages/user/create.vue'
import { createRouter, createWebHashHistory } from 'vue-router'

// routes는 다른 파일로 생성해서 하는 방법 고려
const routes = [
    { path: '/', component: Index },
    { path: '/board', component: Board },
    { path: '/board/posts/:posts_id', component: Posts, name: 'posts'},
    { path: '/board/posts/write', component: PostsWrite },
    { path: '/user/create', component: UserCreate }

]

const router = createRouter({
    history: createWebHashHistory(),
    routes, // `routes: routes`와 같음
})

const app = createApp(App)

app.use(router)
app.use(http)

app.mount('#app')
