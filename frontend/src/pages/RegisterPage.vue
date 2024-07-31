<template>
  <div class="size-container">
    <header>
      <img alt="Lunafit logo" class="logo" src="../assets/LunaFit_logo.png" />
    </header>
    <div class="q-pa-lg q-gutter-sm">
      <q-input
        ref="emailRef"
        color="teal"
        outlined
        v-model="email"
        :label="$t('email')"
        :rules="emailRules"
      >
        <template v-slot:prepend>
          <q-icon>
            <img src="../assets/Communication.svg" alt="Email Icon" />
          </q-icon>
        </template>
      </q-input>

      <q-input
        ref="passwordRef"
        :type="showPassword ? 'text' : 'password'"
        color="teal"
        outlined
        v-model="password"
        :label="$t('password')"
        :rules="passwordRules"
      >
        <template v-slot:prepend>
          <q-icon>
            <img src="../assets/System.svg" alt="Lock Icon" />
          </q-icon>
        </template>
        <template v-slot:append>
          <q-icon
            @click="togglePasswordVisibility"
            :name="showPassword ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
          >
          </q-icon>
        </template>
      </q-input>

      <q-input
        ref="passwordConfirmRef"
        :type="showPassword ? 'text' : 'password'"
        color="teal"
        outlined
        v-model="passwordConfirm"
        :label="$t('confirm-password')"
        :rules="passwordConfirmRules"
      >
        <template v-slot:prepend>
          <q-icon>
            <img src="../assets/System.svg" alt="Lock Icon" />
          </q-icon>
        </template>
        <template v-slot:append>
          <q-icon
            @click="togglePasswordVisibility"
            :name="showPassword ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
          >
          </q-icon>
        </template>
      </q-input>
    </div>
    <div class="q-pa-md q-gutter-sm row justify-center">
      <q-btn
        no-caps
        rounded
        style="background: #50C1BA; color: white"
        :label="$t('register.title')"
        padding="sm lg"
        size="16px"
        @click="registerUser"
      />
    </div>
    <p style="text-align: center;">
      {{ $t('register.account') }}
      <router-link to="/login">
        {{ $t('register.login-now') }}
      </router-link>
    </p>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { api } from 'src/boot/axios';

export default {
  setup() {
    const { t } = useI18n();
    const email = ref('');
    const password = ref('');
    const passwordConfirm = ref('');
    const showPassword = ref(false);
    const router = useRouter();

    const emailRef = ref(null);
    const passwordRef = ref(null);
    const passwordConfirmRef = ref(null);

    const togglePasswordVisibility = () => {
      showPassword.value = !showPassword.value;
    };

    const emailRules = [
      val => !!val || t('validation.emailRequired'),
      val => /^((?!\.)[\w-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$/gim.test(val) || t('validation.invalidEmail')
    ];

    const passwordRules = [
      val => !!val || t('validation.passwordRequired'),
      val => val.length >= 6 || t('validation.passwordLength')
    ];

    const passwordConfirmRules = [
      val => !!val || t('validation.passwordConfirmRequired'),
      val => val === password.value || t('validation.passwordsDoNotMatch')
    ];

    const registerUser = async () => {
      emailRef.value.validate();
      passwordRef.value.validate();
      passwordConfirmRef.value.validate();

      if (emailRef.value.hasError || passwordRef.value.hasError || passwordConfirmRef.value.hasError) {
        return;
      }

      try {
        const response = await api.post('/users/register/', {
          first_name: email.value,
          last_name: email.value,
          email: email.value,
          password: password.value
        });
        const token = response.data.token;
        localStorage.setItem('token', token);
        alert(t('registration.success'));
        router.push('/login');
      } catch (error) {
        // console.error("There was an error registering:", error);
        if (error.response && error.response.data && error.response.data.email) {
          alert(t('registration.emailExists'));
        } else {
          alert(t('registration.failed'));
        }
      }
    };

    return {
      email,
      password,
      passwordConfirm,
      showPassword,
      emailRef,
      passwordRef,
      passwordConfirmRef,
      emailRules,
      passwordRules,
      passwordConfirmRules,
      togglePasswordVisibility,
      registerUser
    };
  }
};
</script>

<style scoped>
header {
  line-height: 1.5;
}

p {
  font-size: 0.875rem;
  margin: 1.25rem 0;
}

a {
  color: #50c1ba;
  font-weight: bold;
  font-size: 0.875rem;
  text-decoration: none;
}

.logo {
  display: block;
  margin: 6rem auto 3rem;
  height: 68px;
}
</style>
