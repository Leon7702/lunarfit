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

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
