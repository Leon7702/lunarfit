<template>
  <div class="size-container">
    <header>
      <img alt="Lunafit logo" class="logo" src="../assets/LunaFit_logo.png" height="68" />
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
      <div class="password-forget">
        <router-link to="/password-forgot">{{ $t('account.password-forgotten') }}</router-link>
      </div>
    </div>
    <div class="q-gutter-sm row justify-center">
      <q-btn
        no-caps
        rounded
        style="background: #50C1BA; color: white"
        :label="$t('login.title')"
        padding="sm lg"
        size="16px"
        @click="loginUser"
      />
    </div>
    <p style="text-align: center;">
      {{ $t('login.no-account') }}
      <router-link to="/register">
        {{ $t('login.register-now') }}
      </router-link>
    </p>

    <div class="language-toggle">
      <q-option-group :options="languageOptions" type="radio" v-model="selectedLanguage" inline />
    </div>
  </div>
</template>

<script>
import { ref, watch, getCurrentInstance } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from 'src/stores/auth';
import { useI18n } from 'vue-i18n';
import { api } from 'src/boot/axios';
import { QBtn, QInput, QOptionGroup, QIcon } from 'quasar';

export default {
  components: {
    QBtn,
    QInput,
    QOptionGroup,
    QIcon,
  },
  setup() {
    const { t } = useI18n();
    const email = ref('');
    const password = ref('');
    const router = useRouter();
    const authStore = useAuthStore();
    const showPassword = ref(false);

    const emailRef = ref(null);
    const passwordRef = ref(null);

    const { proxy } = getCurrentInstance();
    const i18n = useI18n();

    // Load the locale from localStorage if it exists
    const savedLocale = localStorage.getItem('locale') || i18n.locale.value;
    i18n.locale.value = savedLocale;

    const selectedLanguage = ref(i18n.locale.value);

    const getLanguageOptions = () => {
      return [
        { label: i18n.t('language.german'), value: 'de', color: 'primary' },
        { label: i18n.t('language.english'), value: 'en', color: 'primary' },
      ];
    };

    const languageOptions = ref(getLanguageOptions());

    watch(selectedLanguage, (newLocale) => {
      i18n.locale.value = newLocale;
      // Save the new locale to localStorage
      localStorage.setItem('locale', newLocale);
      languageOptions.value = getLanguageOptions(); // Update options when language changes
    });

    const emailRules = [
      val => !!val || t('validation.emailRequired'),
      val => /^((?!\.)[\w-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$/gim.test(val) || t('validation.invalidEmail')
    ];

    const passwordRules = [
      val => !!val || t('validation.passwordRequired'),
      val => val.length >= 6 || t('validation.passwordLength')
    ];

    const loginUser = async () => {
      emailRef.value.validate();
      passwordRef.value.validate();

      if (emailRef.value.hasError || passwordRef.value.hasError) {
        alert(t('validation.fixErrors'));
        return;
      }

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
        // console.error("There was an error logging in:", error);
        if (error.response && error.response.status === 401) {
          alert(t('validation.noActiveAccount'));
        } else {
          alert(t('validation.loginError'));
        }
      }
    };

    const togglePasswordVisibility = () => {
      showPassword.value = !showPassword.value;
    };

    return {
      email,
      password,
      loginUser,
      showPassword,
      togglePasswordVisibility,
      selectedLanguage,
      languageOptions,
      emailRef,
      passwordRef,
      emailRules,
      passwordRules
    };
  },
};
</script>

<style scoped>
header {
  line-height: 1.5;
}

p {
  font-size: 0.875rem;
  margin-top: 1.875rem;
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

.password-forget {
  text-align: right;
}

.language-toggle {
  margin-top: 1.25rem;
  text-align: center;
}

.q-option-group__container--inline {
  display: flex;
  justify-content: center;
  gap: 0.625rem;
}
</style>
