<template>
  <div class="size-container">
    <div class="q-pa-md">

      <div class="title">
        {{ $t('chat.title') }}
        {{ $t('chat.subtitle') }}
      </div>

      <div class="description">
        <div>{{ $t('chat.description1') }}</div>
        <p></p>
        <div>{{ $t('chat.description2') }} {{ $t('chat.thanks') }}</div>
      </div>
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
.title {
  padding-top: 15vh;
  font-size: 24px;
  font-weight: 600;
}

.description {
  padding-top: 5vh;
  padding-bottom: 3vh;
}
</style>
