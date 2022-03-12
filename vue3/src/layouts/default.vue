<template>
    <div>
        <ul>
            <li>
                <router-link to="/product">
                    Product 
                </router-link>
            </li>
            <li>
                <router-link to="/profil">
                    Profil
                </router-link>
            </li>
            <li>
                <a href="#"
                    @click="onLogout">
                    Keluar
                </a>
            </li>
        </ul>

        <br/>

        <slot/>
    </div>
</template>

<script>
import { inject } from "vue";
import { useRouter } from "vue-router";
import { useStore } from 'vuex'

export default {
    setup(){
        const $axios = inject('axios');
        const $router = useRouter();
        const $store  = useStore();

        const onLogout = () => {
            $axios.post("/logout")
            .finally(() => {
                $store.commit("user/setUser",null);
                localStorage.removeItem("token")
                $router.push("/signin");                    
            })
        }

        return {    
            onLogout
        }
    }
}
</script>