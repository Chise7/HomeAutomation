<template>
<header class ="top-bar">
    <nav>
        <button @click="navigateToHome">Home</button>
        <button @click="navigateToSystems">Systems</button>
        <!-- Add here notifications and github link -->
    </nav>
</header>
</template>

<script setup lang="ts">
import {useRouter} from 'vue-router'

//methods
const navigateToHome = () => router.push('./Home')
const navigateToSystems = () => router.push('./Systems')

const router = useRouter()
</script>