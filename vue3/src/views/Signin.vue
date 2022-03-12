<template>
    <div className="flex justify-center items-center h-screen">
        <div className="container-small">
            <h1 className="text-4xl">Signin</h1>

            <form
                @submit="onSubmit">
                <div class="col-12 mt-2">
                    <div class="form-group mb-2">
                        <label for="email" class="mb-2">Email</label>
                        <Field
                            v-model="email"
                            name="email" 
                            type="text" 
                            class="bg-white p-2 border-b-2 border-indigo-500 input-focus-gone w-full"                            
                            :class='errors.email ? "is-invalid" : ""'
                            />

                        <span 
                            class="text-red-600 text-sm text-right w-full pt-3">
                            {{ errors.email }}
                        </span>
                    </div>                

                    <div class="form-group mb-2">
                        <label for="password" class="mb-2">Password</label>
                        <Field 
                            v-model="password"
                            name="password"
                            type="password"
                            class="bg-white p-2 border-b-2 border-indigo-500 input-focus-gone w-full"                            
                            :class='errors.password ? "is-invalid" : ""'/>

                        <span 
                            class="text-red-600 text-sm text-right w-full pt-3">
                            {{ errors.password }}
                        </span>
                    </div>
                </div>
                <div class="col-12 mt-4">
                    <button
                        type="submit"
                        class="pr-5 pl-5 pt-2 pb-2 bg-indigo-500 rounded-md text-white text-sm ml-2">
                        <span v-if="!isLoadingForm">
                            Kirim
                        </span>
                        <span v-else>
                            . . .
                        </span>
                    </button>
                    <button 
                        type="button"
                        class="pr-5 pl-5 pt-2 pb-2 bg-orange-500 rounded-md text-white text-sm ml-2"
                        @click="onResetForm()">
                        Reset
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { inject ,ref } from "vue";
import { Field, useForm } from 'vee-validate';

export default {
    components: {
        Field,
    },
    setup() {
    //    const vueApp = inject('appName');
       const $axios = inject('axios')
       const $toast = inject('toast')

       const isLoadingForm = ref(false);
       const email = ref('');
       const password = ref('');

        const { handleSubmit, errors ,resetForm } = useForm({
            validationSchema: {
                email: 'required|email',
                password: 'required|min:8',
            }
        });

        const onSubmit = handleSubmit(() => {    
            isLoadingForm.value = true;

            $axios.post("/signin",{            
                password : password.value,
                email : email.value,        
            }).then(res => {     
                console.log(res)  
                // token.value = res.data.access_token;
                // user.value = res.data.user;
                // tokewindow.localStorage.setItem("token",res.data.access_token);
                // console.log(res);
                // nuxtApp.$router.push("/profil");
            })
            .catch(err => {
                isLoadingForm.value = false;
                console.log(err);
                if(err.response && err.response.status == 422){
                    $toast.error(err.response.data.message || "Terjadi Kesalahan")
                }else{
                    $toast.error("Terjadi Kesalahan");
                }
            });        
        });
        function onResetForm(){
            resetForm();
        }
        return {
            onResetForm,
            onSubmit,
            email,
            password,
            isLoadingForm,
            errors
        }
    },
    created(){
        console.log(this);

        console.log("Created");
    }
}
</script>

