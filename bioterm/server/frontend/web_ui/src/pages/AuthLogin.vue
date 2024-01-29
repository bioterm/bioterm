<template>
  <q-page
    class="bg-primary window-height window-width row justify-center items-center"
  >
    <div class="column">
      <div class="row">
        <q-card flat bordered class="q-pa-lg shadow-1">
          <q-card-section class="text-center q-pa-none">
            <q-avatar rounded size="150px">
              <img src="~assets/bioterm_icon.svg" />
            </q-avatar>
          </q-card-section>
          <q-card-section class="text-center q-pa-none">
            <p class="text-h5 text-grey-6">bioterm</p>
          </q-card-section>
          <q-card-actions class="q-px-md">
            <q-btn
              unelevated
              color="primary"
              size="lg"
              class="full-width"
              label="Login"
              @click="login"
            />
          </q-card-actions>
          <q-card-section class="text-center q-pa-none">
            <p class="text-grey-6">Not registered? Contact the admin</p>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import auth from "src/services/AuthService";
//const auth = new AuthService();
export default {
  name: "AuthLogin",
  methods: {
    goToAuth() {
      window.location.href = `${
        process.env.AUTHENTIK_AUTHORIZE_URI
      }?client_id=${
        process.env.AUTHENTIK_CLIENT_ID
      }&response_type=code&redirect_uri=${encodeURIComponent(
        process.env.BASE_URL,
      )}`;
    },
    login() {
      console.log("Hello World Logging in");
      auth.login();
    },
    logout() {
      auth.logout();
    },
  },
};
</script>

<style scoped></style>
