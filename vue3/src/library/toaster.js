import Toaster from "@meforma/vue-toaster";

export default {
    install: (app, options) => {    
        app.config.globalProperties.$toast = Toaster; 
    }
}