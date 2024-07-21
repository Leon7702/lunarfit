<template>
  <div class="section-container">
    <div class="section-header">
      {{ title }}
      <router-link :to="link">{{ linkText }}</router-link>
    </div>
    <div class="section-list">
      <div class="q-pa-md">
        <div class="text-blue q-gutter-l">
          <q-spinner v-if="loading" color="primary" size="2em" />
          <span v-else v-for="emoji in emojis" :key="emoji" class="emoji">
            {{ emoji }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { QSpinner } from 'quasar';

export default {
  components: {
    QSpinner,
  },
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
    },
    emojis: {
      type: Array,
      required: true
    },
    loading: {
      type: Boolean,
      default: false
    }
  }
};
</script>

<style>
a {
  color: #50c1ba;
  text-decoration: none;
}

a:visited {
  color: #50c1ba;
}

a:hover {
  text-decoration: none;
}

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
  justify-content: center;
  align-items: center;
  color: #000;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  line-height: 21px;
  /* 150% */
}

.emoji {
  font-size: 28px;
  /* Adjust size as needed */
  margin: 0 4px;
}
</style>
