<template>
    <div>
        Signin
    </div>
</template>

<script>
import { inject } from "vue";

export default {
    setup() {
       const appName = inject('appName');
       console.log(appName);
    },
    created(){
        console.log(this);

        console.log("Created");
    }
}
</script>

