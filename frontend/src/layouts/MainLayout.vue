<template>
  <q-layout view="hHh lpR fFf">
    <!-- Main Content Area -->
    <q-page-container>
      <router-view />
    </q-page-container>

    <!-- Flat Footer with Toolbar and Divider Line -->
    <q-footer class="footer-toolbar">
      <div class="footer-divider"></div>
      <q-toolbar class="footer-toolbar-content">
        <div class="toolbar-item" @click="goToHome" :class="{ 'active-tab': activeTab === 'home' }">
          <img :src="getIconSrc('Home')" class="toolbar-icon" alt="Home" />
          <div class="toolbar-label" :class="{ 'active-label': activeTab === 'home' }">{{ $t('toolbar.start') }}</div>
        </div>
        <div class="toolbar-item" @click="goToCalendar" :class="{ 'active-tab': activeTab === 'calendar' }">
          <img :src="getIconSrc('Calendar')" class="toolbar-icon" alt="Calendar" />
          <div class="toolbar-label" :class="{ 'active-label': activeTab === 'calendar' }">{{ $t('toolbar.calendar') }}
          </div>
        </div>
        <div class="toolbar-item" @click="goToLogEntry">
          <q-btn class="log-entry-btn">
            <q-icon name="add" style="color: white;" />
          </q-btn>
        </div>
        <div class="toolbar-item" @click="goToChat" :class="{ 'active-tab': activeTab === 'chat' }">
          <img :src="getIconSrc('Chat')" class="toolbar-icon" alt="Chat" />
          <div class="toolbar-label" :class="{ 'active-label': activeTab === 'chat' }">{{ $t('toolbar.chat') }}</div>
        </div>
        <div class="toolbar-item" @click="goToSettings" :class="{ 'active-tab': activeTab === 'settings' }">
          <img :src="getIconSrc('Settings')" class="toolbar-icon" alt="Settings" />
          <div class="toolbar-label" :class="{ 'active-label': activeTab === 'settings' }">{{ $t('toolbar.settings') }}
          </div>
        </div>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script>
export default {
  name: 'MainLayout',
  data() {
    return {
      activeTab: 'home' // Default active tab
    };
  },
  methods: {
    getIconSrc(name) {
      return this.activeTab === name.toLowerCase()
        ? `src/assets/${name}_active.svg`
        : `src/assets/${name}.svg`;
    },
    goToHome() {
      this.activeTab = 'home';
      this.$router.push('/home');
    },
    goToCalendar() {
      this.activeTab = 'calendar';
      this.$router.push('/calendar');
    },
    goToLogEntry() {
      this.$router.push('/log');
    },
    goToChat() {
      this.activeTab = 'chat';
      this.$router.push('/chat');
    },
    goToSettings() {
      this.activeTab = 'settings';
      this.$router.push('/settings');
    }
  }
}
</script>

<style scoped>
.footer-divider {
  height: 1px;
  background-color: #e0e0e0;
}

.footer-toolbar {
  background-color: white;
  padding-bottom: 5px;
}

.footer-toolbar-content {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding: 0;
}


.toolbar-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  padding: 5px;
  width: 80px;
  /* Set a fixed width for each toolbar item */
}

.toolbar-icon {
  width: 30px;
  height: 30px;
}

.toolbar-label {
  font-size: 10px;
  color: #A3A3A3;
  white-space: nowrap;
  /* Prevent label from wrapping */
  overflow: hidden;
  /* Hide overflowing text */
  text-overflow: ellipsis;
  /* Show ellipsis (...) for overflow */
  text-align: center;
  /* Center align the text */
}

.log-entry-btn {
  background-color: #50C1BA;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
}

.active-tab {
  color: #50C1BA;
  /* Example of active tab color */
}

.active-label {
  color: #50C1BA;
  /* Color for active label */
}
</style>
