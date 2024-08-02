<template>
    <div class="size-container">
        <div class="q-pa-lg q-gutter-sm">

            <h1>{{ $t('inbox') }}</h1>

            <p>{{ $t('reset-instruction') }}</p>

        </div>

        <div class="q-pa-md q-gutter-sm row justify-center">
            <q-btn no-caps rounded style="background: #50C1BA; color: white" :label="$t('login.back')" padding="sm lg"
                size="16px" @click="toLogin" />
        </div>
    </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
    setup() {
        const router = useRouter();


        const toLogin = () => {
            router.push('/login');
        };

        return {
            toLogin
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