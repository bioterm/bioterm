/* eslint-env node */

/*
 * This file runs in a Node context (it's NOT transpiled by Babel), so use only
 * the ES6 features that are supported by your Node version. https://node.green/
 */

// Configuration for your app
// https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js

/* eslint-disable @typescript-eslint/no-var-requires */

require('dotenv').config();
const { configure } = require('quasar/wrappers');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = configure(function (ctx) {
  return {
    // https://v2.quasar.dev/quasar-cli-webpack/supporting-ts
    supportTS: {
      tsCheckerConfig: {
        eslint: {
          enabled: true,
          files: './src/**/*.{ts,tsx,js,jsx,vue}',
        },
      },
    },

    // https://v2.quasar.dev/quasar-cli-webpack/prefetch-feature
    // preFetch: true,

    // app boot file (/src/boot)
    // --> boot files are part of "main.js"
    // https://v2.quasar.dev/quasar-cli-webpack/boot-files
    boot: ['addressbar-color', 'i18n', 'axios'],

    // https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js#Property%3A-css
    css: ['app.scss'],

    // https://github.com/quasarframework/quasar/tree/dev/extras
    extras: [
      // 'ionicons-v4',
      // 'mdi-v5',
      'fontawesome-v6',
      // 'eva-icons',
      // 'themify',
      // 'line-awesome',
      // 'roboto-font-latin-ext', // this or either 'roboto-font', NEVER both!

      'roboto-font', // optional, you are not bound to it
      'material-icons', // optional, you are not bound to it
    ],

    // Full list of options: https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js#Property%3A-build
    build: {
      env: {
        API_URL: process.env.API_URL,
        BASE_URL: process.env.BASE_URL,
        AUTH0_DOMAIN: process.env.AUTH0_DOMAIN,
        AUTHENTIK_METADATA_URL: process.env.AUTHENTIK_METADATA_URL,
        AUTHENTIK_CLIENT_ID: process.env.AUTHENTIK_CLIENT_ID,
        AUTHENTIK_REDIRECT_URI: process.env.AUTHENTIK_REDIRECT_URI,
        AUTHENTIK_POST_LOGOUT_REDIRECT_URI:
          process.env.AUTHENTIK_POST_LOGOUT_REDIRECT_URI,
        AUTHENTIK_AUTHORIZE_URI: process.env.AUTHENTIK_AUTHORIZE_URI,
        ELN_DOMAIN: process.env.ELN_DOMAIN,
        GRAFANA_DOMAIN: process.env.GRAFANA_DOMAIN,
      },
      vueRouterMode: 'hash', // available values: 'hash', 'history'

      // transpile: false,
      // publicPath: '/',

      // Add dependencies for transpiling with Babel (Array of string/regex)
      // (from node_modules, which are by default not transpiled).
      // Applies only if "transpile" is set to true.
      // transpileDependencies: [],

      // rtl: true, // https://quasar.dev/options/rtl-support
      // preloadChunks: true,
      // showProgress: false,
      // gzip: true,
      // analyze: true,

      // Options below are automatically set depending on the env, set them if you want to override
      // extractCSS: false,

      // uglifyOptions: {
      //   compress: {
      //     drop_console: true,
      //   },
      // },

      // https://v2.quasar.dev/quasar-cli-webpack/handling-webpack
      // "chain" is a webpack-chain object https://github.com/neutrinojs/webpack-chain
      extendWebpack(cfg) {
        cfg.plugins.push(
          new CopyWebpackPlugin({
            patterns: [
              {
                from: 'node_modules/oidc-client-ts/dist/browser/oidc-client-ts.min.js',
                to: 'js',
              },
            ],
          }),
        ),
          cfg.plugins.push(
            new HtmlWebpackPlugin({
              filename: 'callback.html',
              // This is the source file you edit.
              template: 'src/callback.ejs',
              templateParameters: {
                METADATA_URL: process.env.AUTHENTIK_METADATA_URL,
                AUTH0_DOMAIN: process.env.AUTH0_DOMAIN,
                AUTHENTIK_CLIENT_ID: process.env.AUTHENTIK_CLIENT_ID,
              },
            }),
          );
      },
    },

    // Full list of options: https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js#Property%3A-devServer
    devServer: {
      // the following lines can be enabled to deactivate the HMR when developing
      // hot: false,
      // liveReload: false,
      // webSocketServer: false,

      // to get protocol/hostname/port from browser use
      client: {
        webSocketURL: 'auto://0.0.0.0:0/ws',
      },

      server: {
        type: 'http',
      },
      port: 8081,
      open: true, // opens browser window automatically
    },

    // https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js#Property%3A-framework
    framework: {
      config: {},

      // iconSet: 'material-icons', // Quasar icon set
      // lang: 'en-US', // Quasar language pack

      // For special cases outside of where the auto-import strategy can have an impact
      // (like functional components as one of the examples),
      // you can manually specify Quasar components/directives to be available everywhere:
      //
      // components: [],
      // directives: [],

      // Quasar plugins
      plugins: ['Loading', 'Notify', 'AddressbarColor'],
      config: {
        loading: {
          delay: 400,
        },
        notify: {
          textColor: 'white',
          progress: true,
          timeout: 3000,
        },
      },
    },

    // animations: 'all', // --- includes all animations
    // https://quasar.dev/options/animations
    animations: [],

    // https://v2.quasar.dev/quasar-cli-webpack/developing-ssr/configuring-ssr
    ssr: {
      pwa: false,

      // manualStoreHydration: true,
      // manualPostHydrationTrigger: true,

      prodPort: 3000, // The default port that the production server should use
      // (gets superseded if process.env.PORT is specified at runtime)

      maxAge: 1000 * 60 * 60 * 24 * 30,
      // Tell browser when a file from the server should expire from cache (in ms)

      // chainWebpackWebserver (/* chain */) {},

      middlewares: [
        ctx.prod ? 'compression' : '',
        'render', // keep this as last one
      ],
    },

    // https://v2.quasar.dev/quasar-cli-webpack/developing-pwa/configuring-pwa
    pwa: {
      workboxPluginMode: 'InjectManifest', // 'GenerateSW' or 'InjectManifest'
      workboxOptions: {}, // only for GenerateSW
      useCredentials: true,

      // for the custom service worker ONLY (/src-pwa/custom-service-worker.[js|ts])
      // if using workbox in InjectManifest mode
      chainWebpackCustomSW(/* chain */) {},

      manifest: {
        name: 'bioterm',
        short_name: 'bioterm',
        description: '',
        display: 'standalone',
        orientation: 'portrait',
        background_color: '#08a29e',
        theme_color: '#08a29e',
        id: '/',
        icons: [
          {
            src: 'icons/bioterm_icon_128x128.png',
            sizes: '128x128',
            type: 'image/png',
          },
          {
            src: 'icons/bioterm_icon_192x192.png',
            sizes: '192x192',
            type: 'image/png',
          },
          {
            src: 'icons/bioterm_icon_256x256.png',
            sizes: '256x256',
            type: 'image/png',
          },
          {
            src: 'icons/bioterm_icon_384x384.png',
            sizes: '384x384',
            type: 'image/png',
          },
          {
            src: 'icons/bioterm_icon_512x512.png',
            sizes: '512x512',
            type: 'image/png',
          },
          {
            src: 'icons/bioterm_icon_maskable.png',
            sizes: '192x192',
            type: 'image/png',
            purpose: 'any maskable',
          },
        ],
      },
    },

    // Full list of options: https://v2.quasar.dev/quasar-cli-webpack/developing-cordova-apps/configuring-cordova
    cordova: {
      // noIosLegacyBuildFlag: true, // uncomment only if you know what you are doing
    },

    // Full list of options: https://v2.quasar.dev/quasar-cli-webpack/developing-capacitor-apps/configuring-capacitor
    capacitor: {
      hideSplashscreen: true,
    },

    // Full list of options: https://v2.quasar.dev/quasar-cli-webpack/developing-electron-apps/configuring-electron
    electron: {
      bundler: 'packager', // 'packager' or 'builder'

      packager: {
        // https://github.com/electron-userland/electron-packager/blob/master/docs/api.md#options
        // OS X / Mac App Store
        // appBundleId: '',
        // appCategoryType: '',
        // osxSign: '',
        // protocol: 'myapp://path',
        // Windows only
        // win32metadata: { ... }
      },

      builder: {
        // https://www.electron.build/configuration/configuration

        appId: 'bioterm',
      },

      // "chain" is a webpack-chain object https://github.com/neutrinojs/webpack-chain
      chainWebpackMain(/* chain */) {
        // do something with the Electron main process Webpack cfg
        // extendWebpackMain also available besides this chainWebpackMain
      },

      // "chain" is a webpack-chain object https://github.com/neutrinojs/webpack-chain
      chainWebpackPreload(/* chain */) {
        // do something with the Electron main process Webpack cfg
        // extendWebpackPreload also available besides this chainWebpackPreload
      },
    },
  };
});
