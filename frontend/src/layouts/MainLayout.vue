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
          <div class="toolbar-label" :class="{ 'active-label': activeTab === 'home' }">Start</div>
        </div>
        <div class="toolbar-item" @click="goToCalendar" :class="{ 'active-tab': activeTab === 'calendar' }">
          <img :src="getIconSrc('Calendar')" class="toolbar-icon" alt="Calendar" />
          <div class="toolbar-label" :class="{ 'active-label': activeTab === 'calendar' }">Kalendar</div>
        </div>
        <div class="log-entry-btn-wrapper">
          <q-btn class="log-entry-btn" @click="goToLogEntry">
            <q-icon name="add" style="color: white;" />
          </q-btn>
        </div>
        <div class="toolbar-item" @click="goToChat" :class="{ 'active-tab': activeTab === 'chat' }">
          <img :src="getIconSrc('Chat')" class="toolbar-icon" alt="Chat" />
          <div class="toolbar-label" :class="{ 'active-label': activeTab === 'chat' }">Chat</div>
        </div>
        <div class="toolbar-item" @click="goToProfile" :class="{ 'active-tab': activeTab === 'profile' }">
          <img :src="getIconSrc('Profile')" class="toolbar-icon" alt="Profile" />
          <div class="toolbar-label" :class="{ 'active-label': activeTab === 'profile' }">Profil</div>
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
    goToProfile() {
      this.activeTab = 'profile';
      this.$router.push('/profile');
    }
  }
}
</script>

<style scoped>
.footer-divider {
  height: 1px;
  background-color: #e0e0e0;
  margin-top: 10px;
}

.footer-toolbar {
  background-color: white;
}

.footer-toolbar-content {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 10px 0;
  /* Vergrößerte Toolbar */
}

.toolbar-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  padding: 5px;
}

.toolbar-icon {
  width: 30px;
  height: 30px;
}

.toolbar-label {
  font-size: 14px;
  /* Vergrößerte Schriftgröße */
  color: #A3A3A3;
}

.active-label {
  color: #50C1BA;
}

.log-entry-btn-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}

.log-entry-btn {
  background-color: #50C1BA;
  border-radius: 50%;
  width: 50px;
  /* Größere Kreisgröße */
  height: 50px;
  /* Größere Kreisgröße */
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
}
</style>
