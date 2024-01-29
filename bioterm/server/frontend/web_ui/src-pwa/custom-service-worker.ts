/*
 * This file (which will be your service worker)
 * is picked up by the build system ONLY if
 * quasar.config.js > pwa > workboxPluginMode is set to "InjectManifest"
 */

declare const self: ServiceWorkerGlobalScope & typeof globalThis;

import { precacheAndRoute } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { NetworkOnly } from 'workbox-strategies';

// Use with precache injection
precacheAndRoute(self.__WB_MANIFEST);

// Prevent caching for OIDC server routes
registerRoute(
  ({ url }) => url.origin === process.env.AUTH0_DOMAIN,
  new NetworkOnly(),
);

// Prevent caching for callback route
registerRoute(
  ({ url }) => url.pathname.startsWith('/callback'),
  new NetworkOnly(),
);
