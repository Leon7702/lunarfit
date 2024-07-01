<template>
  <div class="container">
    <q-layout view="hHh lpR fFf">
      <q-page-container>
        <router-view />
      </q-page-container>
      <q-footer class="footer-toolbar">
        <div class="size-container">
        <div class="footer-divider"></div>
        
        <q-toolbar class="footer-toolbar-content">
          <div class="toolbar-item" @click="goToHome" :class="{ 'active-tab': activeTab === 'home' }">
            <img :src="getIconSrc('Home')" class="toolbar-icon" alt="Home" />
            <div class="toolbar-label" :class="{ 'active-label': activeTab === 'home' }">{{ $t('toolbar.start') }}</div>
          </div>
          <div class="toolbar-item" @click="goToCalendar" :class="{ 'active-tab': activeTab === 'calendar' }">
            <img :src="getIconSrc('Calendar')" class="toolbar-icon" alt="Calendar" />
            <div class="toolbar-label" :class="{ 'active-label': activeTab === 'calendar' }">{{ $t('toolbar.calendar')
              }}</div>
          </div>
          <div class="toolbar-item log-entry-btn-container" @click="goToLogEntry">
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
            <div class="toolbar-label" :class="{ 'active-label': activeTab === 'settings' }">{{ $t('toolbar.settings')
              }}</div>
          </div>
        </q-toolbar>
      </div>
      </q-footer>
    </q-layout>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: '',
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
      localStorage.setItem('activeTab', 'home');
      this.$router.push('/home');
    },
    goToCalendar() {
      this.activeTab = 'calendar';
      localStorage.setItem('activeTab', 'calendar');
      this.$router.push('/calendar');
    },
    goToLogEntry() {
      this.activeTab = 'log';
      localStorage.setItem('activeTab', 'log');
      this.$router.push('/log');
    },
    goToChat() {
      this.activeTab = 'chat';
      localStorage.setItem('activeTab', 'chat');
      this.$router.push('/chat');
    },
    goToSettings() {
      this.activeTab = 'settings';
      localStorage.setItem('activeTab', 'settings');
      this.$router.push('/settings');
    }
  },
  mounted() {
    const currentRoute = this.$route.path.substring(1);
    this.activeTab = currentRoute || 'home';
    localStorage.setItem('activeTab', this.activeTab);
  },
  watch: {
    $route(to) {
      const currentRoute = to.path.substring(1);
      this.activeTab = currentRoute || 'home';
      localStorage.setItem('activeTab', this.activeTab);
    }
  }
};
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
  justify-content: space-between;
  align-items: center;
  padding: 0;
  width: 100%;
}

.toolbar-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  padding: 5px;
  flex: 1;
  text-align: center;
}

.toolbar-icon {
  width: 30px;
  height: 30px;
}

.toolbar-label {
  font-size: 10px;
  color: #A3A3A3;
}

.log-entry-btn-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
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
}

.active-label {
  color: #50C1BA;
}


</style>
