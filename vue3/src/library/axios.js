import axios from "axios";

axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
axios.defaults.baseURL = process.env.VUE_APP_API_URL;

export default {
    install: (app, options) => {    
        app.config.globalProperties.$axios = axios;         
        app.provide('axios', axios)
    }
}