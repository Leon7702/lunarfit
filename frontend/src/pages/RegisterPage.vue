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
        <q-icon
          @click="togglePasswordVisibility"
          :name="showPassword ? 'visibility_off' : 'visibility'"
          class="cursor-pointer"> </q-icon>
      </template>
    </q-input>
    <q-input :type="showPassword ? 'text' : 'password'" color="teal" outlined v-model="passwordConfirm" label="Password bestätigen">
      <template v-slot:prepend>
        <q-icon>
          <img src="../assets/System.svg" alt="Lock Icon" />
        </q-icon>
      </template>
      <template v-slot:append>
        <q-icon
          @click="togglePasswordVisibility"
          :name="showPassword ? 'visibility_off' : 'visibility'"
          class="cursor-pointer"> </q-icon>
      </template>
    </q-input>
  </div>
  <div class="q-pa-md q-gutter-sm row justify-center">
    <q-btn no-caps rounded style="background: #50C1BA; color: white" label="Registrieren" padding="sm lg" size="16px" @click="registerUser"/>
  </div>
  <p style="text-align: center;">
    Du hast einen Account?
    <router-link to="/login">Jetzt anmelden</router-link>
  </p>
</template>


<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const email = ref('');
    const password = ref('');
    const passwordConfirm = ref('');
    const showPassword = ref(false);
    const router = useRouter();

    const togglePasswordVisibility = () => {
      showPassword.value = !showPassword.value;
    };

    const registerUser = async () => {
      if (password.value !== passwordConfirm.value) {
        alert("Passwords do not match!");
        return;
      }

      try {
        const response = await axios.post('http://localhost:8000/users/', {
          username: "first-user",
          email: email.value,
          password: password.value
        });
        const token = response.data.token;
        localStorage.setItem('token', token); // Store token in local storage
        alert("Registration successful!");
        router.push('/login');
      } catch (error) {
        console.error("There was an error registering:", error);
        alert("Registration failed!");
      }
    };

    return {
      email,
      password,
      passwordConfirm,
      showPassword,
      togglePasswordVisibility,
      registerUser
    };
  }
};
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
