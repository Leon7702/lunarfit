<template>
  <header>
    <img alt="Lunafit logo" class="logo" src="../assets/LunaFit.svg" height="45" />
  </header>
  <div>
    <q-input color="teal" outlined v-model="text" label="E-Mail">
      <template v-slot:prepend>
        <q-icon name="email" />
      </template>
    </q-input>
    <q-input color="teal" filled v-model="text" label="Password">
        <template v-slot:prepend>
          <q-icon name="password" />
        </template>
        <template v-slot:append>
          <q-icon name="check" />
        </template>
      </q-input>
      <q-input color="teal" filled v-model="text" label="Password bestätigen">
        <template v-slot:prepend>
          <q-icon name="lock" />
        </template>
        <template v-slot:append>
          <q-icon name="check" />
        </template>
      </q-input>
  </div>
  <p style="text-align: center;">
    Du hast einen Account?
    <a href="/login">Jetzt anmelden</a>
  </p>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const text = ref('');
    return { text };
  }
}
</script>
