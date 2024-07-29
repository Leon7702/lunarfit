<template>
  <div class="size-container">
    <div class="q-pa-md">
      <img src="~assets/404.svg" alt="Chat Image" class="image" />

      <div class="title">
        404 - <br>
        {{ $t('error.notFound') }}
      </div>

      <div class="description">
        <div>{{ $t('error.description') }}</div>
      </div>

      <div class="q-pa-lg q-gutter-sm row justify-center">
        <q-btn no-caps rounded style="background: #50C1BA; color: white" :label="$t('buttons.home')" padding="sm lg"
          size="16px" to="/" />
      </div>
    </div>
  </div>
</template>

<script setup>
defineOptions({
  name: 'ErrorNotFound'
});
</script>

<style scoped>
.title {
  padding-top: 6vh;
  font-size: 24px;
  font-weight: 600;
}

.description {
  padding-top: 2vh;
  padding-bottom: 5vh;
  font-size: 16px;
}

.image {
  padding-top: 30px;
  object-fit: cover;
  object-position: center;
  margin: 0 auto;
  width: 90%;
  display: block;
}

</style>
