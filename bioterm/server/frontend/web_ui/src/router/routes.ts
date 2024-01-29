import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/LoginLayout.vue'),
    children: [{ path: '', component: () => import('pages/AuthLogin.vue') }],
  },
  {
    path: '/imprint',
    component: () => import('layouts/LoginLayout.vue'),
    children: [{ path: '', component: () => import('pages/ImprintPage.vue') }],
  },
  {
    path: '/home',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/home', component: () => import('pages/HomePage.vue') },
    ],
    meta: {
      isSecure: true,
    },
  },
  {
    path: '/devices',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/devices', component: () => import('pages/DevicesPage.vue') },
    ],
    meta: {
      isSecure: true,
    },
  },
  {
    path: '/device',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: ':uuid', // this makes it a "/device/<uuid>" path
        name: 'device',
        component: () => import('pages/SingleDevicePage.vue'),
        props: true,
      },
    ],
    meta: {
      isSecure: true,
    },
  },
  {
    path: '/data',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/data', component: () => import('pages/DataExportPage.vue') },
    ],
    meta: {
      isSecure: true,
    },
  },
  {
    path: '/experiments',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '/experiments',
        component: () => import('pages/ExperimentsPage.vue'),
      },
    ],
    meta: {
      isSecure: true,
    },
  },
  {
    path: '/protocols',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/protocols', component: () => import('pages/ProtocolPage.vue') },
    ],
    meta: {
      isSecure: true,
    },
  },
  {
    path: '/rules',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/rules', component: () => import('pages/RulesPage.vue') },
    ],
    meta: {
      isSecure: true,
    },
  },
  {
    path: '/rule',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: 'create',
        component: () => import('pages/SingleRulePage.vue'),
      },
      {
        path: ':uuid', // this makes it a "/rule/<uuid>" path
        name: 'rule',
        component: () => import('pages/SingleRulePage.vue'),
        props: true,
      },
    ],
    meta: {
      isSecure: true,
    },
  },
  {
    path: '/help',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/help', component: () => import('pages/HelpPage.vue') },
    ],
    meta: {
      isSecure: true,
    },
  },
  {
    path: '/admin',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/admin', component: () => import('pages/AdminDashboard.vue') },
    ],
    meta: {
      isSecure: true,
      isAdmin: true,
    },
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('layouts/ErrorLayout.vue'),
    children: [
      { path: '', component: () => import('pages/ErrorNotFound.vue') },
    ],
  },
];

export default routes;
