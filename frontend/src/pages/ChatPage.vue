<template>
  <div class="size-container">
    <div class="q-pa-md">

      <h6>Chat Funktion - Demnächst verfügbar</h6>

      <p>Bald wird unsere neue Chat Funktion verfügbar sein! Damit wirst du die Möglichkeit haben, direkt mit anderen
        Benutzerinnen und Trainer zu chatten.</p>
      <p>Unser LunarFit Team arbeitet intensiv daran, diese Funktion für dich bereitzustellen.

        Vielen Dank für deine Geduld!</p>

    </div>

    <div class="q-pa-md q-gutter-sm row justify-center">
      <q-btn no-caps rounded style="background: #50C1BA; color: white" label="Zum Dashboard" padding="sm lg" size="16px"
        @click="toHome" />
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  setup() {
    const router = useRouter();


    const toHome = () => {
      router.push('/home');
    };

    return {
      toHome
    };
  },
};
</script>

<style scoped>
h6 {
  padding-top: 10vh;
  font-size: 24px;
  font-weight: 600;
}

p {
  font-size: 14px;
}
</style>
