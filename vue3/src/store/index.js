import { createStore } from 'vuex'

const user = {
    namespaced: true,
    state(){
        return {
            data : JSON.parse(localStorage.getItem('user') || null)
        };        
    },
    mutations : {
        setUser (state,payload) {
            localStorage.setItem("user",JSON.stringify(payload)) 
            state.data = payload
        }
    },

}

const store = createStore({
    namespaced: true,
    modules : {
        user : user
    }
})

export default store;