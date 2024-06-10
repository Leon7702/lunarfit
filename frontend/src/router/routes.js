const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') }, // Beispiel: Hier wird die IndexPage angezeigt
    ]
  },
  {
    path: '/onboarding',
    name: 'OnboardingStart',
    component: () => import('pages/onboarding/OnboardingStart.vue')
  },
  {
    path: '/onboardingStep1',
    name: 'OnboardingStep1',
    component: () => import('pages/onboarding/OnboardingStep1.vue')
  },
  {
    path: '/onboardingStep2',
    name: 'OnboardingStep2',
    component: () => import('pages/onboarding/OnboardingStep2.vue')
  },
  {
    path: '/onboardingStep3',
    name: 'OnboardingStep3',
    component: () => import('pages/onboarding/OnboardingStep3.vue')
  },
  {
    path: '/onboardingStep4',
    name: 'OnboardingStep4',
    component: () => import('pages/onboarding/OnboardingStep4.vue')
  },
  {
    path: '/onboardingStep5',
    name: 'OnboardingStep5',
    component: () => import('pages/onboarding/OnboardingStep5.vue')
  },
  {
    path: '/onboardingStep6',
    name: 'OnboardingStep6',
    component: () => import('pages/onboarding/OnboardingStep6.vue')
  },
  {
    path: '/onboardingEnd',
    name: 'OnboardingEnd',
    component: () => import('pages/onboarding/OnboardingEnd.vue')
  },
  {
    path: '/register',
    component: () => import('pages/RegisterPage.vue')
  },
  {
    path: '/login',
    component: () => import('pages/LoginPage.vue')
  },

  { 
    path: '/log', 
    name: 'LogHome', 
    component: () => import('pages/log/LogHome.vue') 
  },
  { 
    path: '/log-cycle', 
    name: 'LogCycleHome', 
    component: () => import('pages/log/LogCycleHome.vue') 
  },
  { 
    path: '/log-cycle-list', 
    name: 'LogCycleHomeList', 
    component: () => import('pages/log/LogCycleHomeList.vue') 
  },
  {
    path: '/log-cycle-mens',
    name: 'LogCycleMens',
    component: () => import('pages/log/LogCycleMens.vue')
  },
  {
    path: '/log-cycle-temp',
    name: 'LogCycleTemp',
    component: () => import('pages/log/LogCycleTemp.vue')
  },
  {
    path: '/log-cycle-cerfix',
    name: 'LogCycleCerfix',
    component: () => import('pages/log/LogCycleCerfix.vue')
  },
  {
    path: '/log-cycle-gebaermutterhals',
    name: 'LogCycleGebaermutter',
    component: () => import('pages/log/LogCycleGebaermutter.vue')
  },
  {
    path: '/log-cycle-sex',
    name: 'LogCycleSex',
    component: () => import('pages/log/LogCycleSex.vue')
  },
  {
    path: '/log-cycle-contraceptive',
    name: 'LogCycleContraceptive',
    component: () => import('pages/log/LogCycleContraceptive.vue')
  },
  {
    path: '/log-cycle-medicine',
    name: 'LogCycleMedicine',
    component: () => import('pages/log/LogCycleMedicine.vue')
  },
  {
    path: '/log-cycle-ovulation-test',
    name: 'LogCycleOvulationTest',
    component: () => import('pages/log/LogCycleOvulationTest.vue')
  },
  {
    path: '/log-cycle-pregnancy-test',
    name: 'LogCyclePregnancyTest',
    component: () => import('pages/log/LogCyclePregnancyTest.vue')
  },
  {
    path: '/log-training-complaints',
    name: 'LogTrainingComplaints',
    component: () => import('pages/log/LogTrainingComplaints.vue')
  },
  {
    path: '/log-training-mood',
    name: 'LogTrainingMood',
    component: () => import('pages/log/LogTrainingMood.vue')
  },
  {
    path: '/log-training-recovery',
    name: 'LogTrainingRecovery',
    component: () => import('pages/log/LogTrainingRecovery.vue')
  },
  {
    path: '/log-training-strain',
    name: 'LogTrainingStrainPre',
    component: () => import('pages/log/LogTrainingStrainPre.vue')
  },
  {
    path: '/log-training-strain-2',
    name: 'LogTrainingStrain',
    component: () => import('pages/log/LogTrainingStrain.vue')
  },
  {
    path: '/log-notes',
    name: 'LogNotes',
    component: () => import('pages/log/LogNotes.vue')
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
