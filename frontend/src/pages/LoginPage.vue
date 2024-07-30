<template>
  <div class="size-container">
    <header>
      <img alt="Lunafit logo" class="logo" src="../assets/LunaFit_logo.png" height="68" />
    </header>
    <div class="q-pa-lg q-gutter-sm">
      <q-input color="teal" outlined v-model="email" :label="$t('email')">
        <template v-slot:prepend>
          <q-icon>
            <img src="../assets/Communication.svg" alt="Email Icon" />
          </q-icon>
        </template>
      </q-input>
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
      <div class="password-forget"><router-link to="/password-forgot">Passwort vergessen?</router-link></div>
    </div>
    <div class="q-gutter-sm row justify-center">
      <q-btn no-caps rounded style="background: #50C1BA; color: white" :label="$t('login.title')" padding="sm lg"
        size="16px" @click="loginUser" />
    </div>
    <p style="text-align: center;">
      {{ $t('login.no-account') }}
      <router-link to="/register">{{ $t('login.register-now') }}</router-link>
    </p>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from 'src/stores/auth';
import { api } from 'src/boot/axios';

export default {
  setup() {
    const email = ref('');
    const password = ref('');
    const router = useRouter();
    const authStore = useAuthStore();
    const showPassword = ref(false);

    const loginUser = async () => {
      try {

        await authStore.login({ email: email.value, password: password.value });

        // Fetch user profile to check onboarding status
        const response = await api.get(`/users/profile/${authStore.userId}/`);
        const userProfile = response.data;


        if (userProfile.onboarding_finished) {
          router.push('/home'); // Redirect to home if onboarding is finished
        } else {
          router.push('/onboarding'); // Redirect to onboarding if not finished
        }
      } catch (error) {
        alert("There was an error logging in: " + error);
      }
    };

    const togglePasswordVisibility = () => {
      showPassword.value = !showPassword.value;
    };

    return { email, password, loginUser, showPassword, togglePasswordVisibility };
  },
};
</script>


<style scoped>
header {
  line-height: 1.5;
}

p {
  font-size: 14px;
  margin: 30px;
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
  margin-top: 1rem 0;
}
</style>
