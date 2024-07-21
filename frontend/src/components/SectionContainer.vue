<template>
  <div class="section-container">
    <div class="section-header">
      {{ title }}
      <router-link :to="link">{{ linkText }}</router-link>
    </div>
    <div class="section-list">
      <div class="q-pa-md">
        <div class="emoji-wrapper q-gutter-l">
          <q-spinner v-if="loading" color="primary" size="2em" />
          <div v-else v-for="item in emojis" :key="item.emoji" class="emoji-container">
            <span class="emoji">{{ item.emoji }}</span>
            <span class="emoji-label">{{ abbreviateLabel(item.label) }}</span>
          </div>
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
      required: true,
      validator: value => value.every(item => 'emoji' in item && 'label' in item)
    },
    loading: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    abbreviateLabel(label) {
      const maxLength = 8;
      return label.length > maxLength ? label.substring(0, maxLength) + '...' : label;
    }
  }
};
</script>

<style scoped>
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
  margin: 1.25rem auto;
  /* Center container with top margin */
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #000;
  font-size: 1rem;
  font-style: normal;
  font-weight: 600;
  line-height: 1.3125rem;
  /* 150% */
}

.section-list {
  display: flex;
  justify-content: center;
  align-items: center;
  color: #000;
  font-size: 1rem;
  font-style: normal;
  font-weight: 600;
  line-height: 1.3125rem;
  /* 150% */
}

.emoji-wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.emoji-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 4rem;
  height: 4rem;
  margin: 0.5rem;
  padding: 0.5rem;
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.08);
  border-radius: 0.5rem;
  background-color: #fff;
}

.emoji {
  font-size: 1.75rem;
  /* Adjust size as needed */
}

.emoji-label {
  font-size: 0.775rem;
  margin-top: 0.15rem;
  text-align: center;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
