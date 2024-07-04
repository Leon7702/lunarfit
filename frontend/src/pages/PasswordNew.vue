<template>
    <div class="size-container">
        <div class="q-pa-lg q-gutter-sm">

            <h1>Neues Passwort anlegen</h1>

            <p>Bitte gib dein neues Passwort ein und bestätige es. Achte darauf, ein sicheres Passwort zu wählen, das du
                dir
                gut merken kannst.</p>

            <q-input :type="showPassword ? 'text' : 'password'" color="teal" outlined v-model="password"
                :label="$t('password')">
                <template v-slot:prepend>
                    <q-icon>
                        <img src="../assets/System.svg" alt="Lock Icon" />
                    </q-icon>
                </template>
                <template v-slot:append>
                    <q-icon @click="togglePasswordVisibility" :name="showPassword ? 'visibility_off' : 'visibility'"
                        class="cursor-pointer"> </q-icon>
                </template>
            </q-input>
            <q-input :type="showPassword ? 'text' : 'password'" color="teal" outlined v-model="passwordConfirm"
                :label="$t('confirm-password')">
                <template v-slot:prepend>
                    <q-icon>
                        <img src="../assets/System.svg" alt="Lock Icon" />
                    </q-icon>
                </template>
                <template v-slot:append>
                    <q-icon @click="togglePasswordVisibility" :name="showPassword ? 'visibility_off' : 'visibility'"
                        class="cursor-pointer"> </q-icon>
                </template>
            </q-input>
        </div>
        <div class="q-pa-md q-gutter-sm row justify-center">
            <q-btn no-caps rounded style="background: #50C1BA; color: white" label="Passwort ändern" padding="sm lg"
                size="16px" @click="changePassword" />
        </div>
        <p style="text-align: center;">
            <router-link to="/login">Zurück zum Login</router-link>
        </p>
    </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
    setup() {
        const router = useRouter();
        const password = ref('');
        const passwordConfirm = ref('');
        const showPassword = ref(false);

        const togglePasswordVisibility = () => {
            showPassword.value = !showPassword.value;
        };

        const changePassword = () => {
            router.push('/password-reset');
        };

        return {
            togglePasswordVisibility, password, passwordConfirm, changePassword, showPassword
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

@media (min-width: 1024px) {
    header {
        display: flex;
        place-items: center;
        padding-right: calc(var(--section-gap) / 2);
    }

    .logo {
        margin: 0 2rem 0 0;
    }

    header .wrapper {
        display: flex;
        place-items: flex-start;
        flex-wrap: wrap;
    }
}
</style>