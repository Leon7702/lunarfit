// src/boot/i18n.js
import { boot } from 'quasar/wrappers';
import { createI18n } from 'vue-i18n';
import messages from 'src/i18n';

const savedLocale = localStorage.getItem('locale') || 'de';

const i18n = createI18n({
  legacy: false, 
  locale: savedLocale, // default locale from localStorage
  fallbackLocale: 'de', // fallback locale
  messages // set locale messages
});

export default boot(({ app }) => {
  app.use(i18n);
});

export { i18n };
