import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import axios from "./library/axios.js";
import toaster from "./library/toaster.js"
import "./library/vee-validate.js";
import store from "./store/index.js";
import './assets/index.css'

const app = createApp(App)

app.use(store)
app.use(router)
app.use(axios);
app.use(toaster);
app.mount('#app')
app.provide('appName', 'Vue3');
