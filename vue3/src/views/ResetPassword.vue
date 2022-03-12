<template>
    <div className="flex justify-center items-center h-screen">
        <div className="container-small">
            <h1 className="text-4xl">Reset Password</h1>

            <form
                @submit="onSubmit">
                <div class="col-12 mt-2">
                    <div class="form-group mb-2">
                        <label for="token" class="mb-2">Token</label>
                        <Field
                            v-model="token"
                            name="token" 
                            type="text" 
                            class="bg-white p-2 border-b-2 border-indigo-500 input-focus-gone w-full"                            
                            :class='errors.token ? "is-invalid" : ""'
                            />

                        <span 
                            class="text-red-600 text-sm text-right w-full pt-3">
                            {{ errors.token }}
                        </span>
                    </div>               

                    <div class="form-group mb-2">
                        <label for="password" class="mb-2">Password</label>
                        <Field
                            v-model="password"
                            name="password" 
                            type="password" 
                            class="bg-white p-2 border-b-2 border-indigo-500 input-focus-gone w-full"                            
                            :class='errors.password ? "is-invalid" : ""'
                            />

                        <span 
                            class="text-red-600 text-sm text-right w-full pt-3">
                            {{ errors.password }}
                        </span>
                    </div>                    

                    <div class="form-group mb-2">
                        <label for="password_confirmation" class="mb-2">Password Konfrimasi</label>
                        <Field
                            v-model="password_confirmation"
                            name="password_confirmation" 
                            type="password" 
                            class="bg-white p-2 border-b-2 border-indigo-500 input-focus-gone w-full"                            
                            :class='errors.password_confirmation ? "is-invalid" : ""'
                            />

                        <span 
                            class="text-red-600 text-sm text-right w-full pt-3">
                            {{ errors.password_confirmation }}
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
import { inject, ref } from "vue";
import { Field, useForm } from 'vee-validate';
import { useRouter } from 'vue-router';

export default {
    created(){
        this.email = this.$route.query.email;

        console.log(this.email);

        console.log("Created");
    },

    components: {
        Field,
    },
    
    setup() {    
       const $axios = inject('axios')
       const $toast = inject('toast')
       const $router = useRouter();

       const isLoadingForm = ref(false);
       const email = ref('');
       const token = ref('');
       const password = ref('');
       const password_confirmation = ref('');

        const { handleSubmit, errors ,resetForm } = useForm({
            validationSchema: {
                token: 'required',
                password : 'required',
                password_confirmation : 'required'
            }
        });

        const onSubmit = handleSubmit(() => {    
            isLoadingForm.value = true;

            $axios.post("/reset-password",{       
                email : email.value,
                token : token.value,
                password : password.value,
                password_confirmation : password_confirmation.value
            }).then(() => {             
                $router.push("/signin");
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
            token,
            email,
            password,
            password_confirmation,            
            isLoadingForm,
            errors
        }
    }   
}
</script>