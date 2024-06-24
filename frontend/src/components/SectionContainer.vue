<template>
  <div class="section-container">
    <div class="section-header">
      {{ title }}
      <router-link :to="link">{{ linkText }}</router-link>
    </div>
    <div class="section-list">
      <div class="q-pa-md">
        <div class="text-blue q-gutter-md">
          <q-icon v-for="size in ['md', 'md', 'md', 'md', 'md']" :key="size" :size="size" name="font_download" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },
    link: {
      type: String,
      required: true
    },
    linkText: {
      type: String,
      required: true
    }
  }
};
</script>

<style>
.section-container {
  margin: 20px auto;
  /* Center container with top margin */
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #000;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  line-height: 21px;
  /* 150% */
}

.section-list {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  color: #000;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  line-height: 21px;
  /* 150% */
}
</style>