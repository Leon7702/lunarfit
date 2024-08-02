<template>
    <div class="size-container">
        <div class="q-pa-lg q-gutter-sm">

            <h1>{{ $t('account.password-forgotten') }}</h1>

            <p>{{ $t('account.password-forgotten-text') }}</p>

            <q-input color="teal" outlined v-model="email" :label="$t('email')">
                <template v-slot:prepend>
                    <q-icon>
                        <img src="../assets/Communication.svg" alt="Email Icon" />
                    </q-icon>
                </template>
            </q-input>
        </div>
        <div class="q-pa-md q-gutter-sm row justify-center">
            <q-btn no-caps rounded style="background: #50C1BA; color: white" :label="$t('continue')" padding="sm lg"
                size="16px" @click="sendMail" />
        </div>
        <p style="text-align: center;">
            <router-link to="/login">{{ $t('login.back') }}</router-link>
        </p>
    </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
    setup() {
        const router = useRouter();
        const email = ref('');


        const sendMail = () => {
            router.push('/password-inbox');
        };

        return {
            sendMail, email
        };
    },
};
</script>

<style scoped>
h1 {
    padding-top: 137px;
    font-size: 24px;
    font-weight: 600;
    line-height: 31px;
}

p {
    color: #000;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: 24px;
    /* 150% */
}

a {
    color: #50c1ba;
    font-weight: bold;
    font-size: 14px;
    text-decoration: none;
}

.logo {
    display: block;
    margin: 6rem auto 6rem;
}

.password-forget {
    text-align: right;
    margin: 1rem 0;
}
</style>