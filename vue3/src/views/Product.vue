<template>
    <default>
        {{ user }}
        Product
    </default>
</template>

<script>
import Default from "../layouts/default.vue";
import { useStore } from 'vuex'
import { computed } from "vue";

export default {
    components : { 
        Default,
    },
    
    setup(){
        const $store = useStore();

        return {
            user : computed(() => $store.state.user)
        }
    }
}
</script>