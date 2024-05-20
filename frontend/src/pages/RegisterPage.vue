<template>
  <header>
    <img alt="Lunafit logo" class="logo" src="../assets/LunaFit.svg" height="45" />
  </header>
  <div class="q-pa-lg q-gutter-sm">
    <q-input color="teal" outlined v-model="email" label="E-Mail">
      <template v-slot:prepend>
        <q-icon>
          <img src="../assets/Communication.svg" alt="Email Icon" />
        </q-icon>
      </template>
    </q-input>
    <q-input :type="showPassword ? 'text' : 'password'" color="teal" outlined v-model="password" label="Password">
      <template v-slot:prepend>
        <q-icon>
          <img src="../assets/System.svg" alt="Lock Icon" />
        </q-icon>
      </template>
      <template v-slot:append>
        <q-icon @click="togglePasswordVisibility" :name="showPassword ? 'visibility' : 'visibility_off'"
          class="cursor-pointer"> </q-icon>
      </template>
    </q-input>
    <q-input :type="showConfirmPassword ? 'text' : 'password'" color="teal" outlined v-model="passwordConfirm"
      label="Password bestätigen">
      <template v-slot:prepend>
        <q-icon>
          <img src="../assets/System.svg" alt="Lock Icon" />
        </q-icon>
      </template>
      <template v-slot:append>
        <q-icon @click="toggleConfirmPasswordVisibility" :name="showConfirmPassword ? 'visibility' : 'visibility_off'"
          class="cursor-pointer"> </q-icon>
      </template>
    </q-input>
  </div>
  <div class="q-pa-md q-gutter-sm row justify-center">
    <q-btn no-caps rounded style="background: #50C1BA; color: white" label="Registrieren" padding="xs lg" size="16px" @click="showNotif"/>
  </div>
  <p style="text-align: center;">
    Du hast einen Account?
    <a href="#/login">Jetzt anmelden</a>
  </p>
</template>

<script>
import { ref } from 'vue';
import { useQuasar } from 'quasar'


export default {
  setup() {
    const text = ref('');
    const $q = useQuasar();
    const showNotif = () => {
      $q.notify({
        message: 'Registrierung erfolgreich!',
        color: 'grey'
      });
    };
    return { text, showNotif };
  },
  data() {
    return {
      email: '',
      password: '',
      passwordConfirm: '',
      showPassword: false,
      showConfirmPassword: false,
    };
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },
    toggleConfirmPasswordVisibility() {
      this.showConfirmPassword = !this.showConfirmPassword;
    },
  },
}
</script>

<style scoped>
/* @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap'); */

header {
  line-height: 1.5;
}

p {
  font-size: 14px;
  margin: 20px;
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
