import Toaster from "@meforma/vue-toaster";
import { createToaster } from "@meforma/vue-toaster";

export default {
    install: (app, options) => {    
        app.config.globalProperties.$toast = Toaster; 
        
        const toaster = createToaster({ /* options */ });
        app.provide('toast', toaster)
    }
}