import {createRouter, createWebHistory } from 'vue-router';
import type {RouteRecordRaw} from 'vue-router';
import Home from "../views/HomePage.vue";
import Systems from "../views/SystemsPage.vue";

const routes: Array<RouteRecordRaw> = [
    {
        path: '/Home',
        name: 'Home',
        component: Home
    },
    {
        path: '/Systems',
        name: "Systems",
        component: Systems
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
