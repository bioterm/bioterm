import { defineStore } from 'pinia';
import auth from 'src/services/AuthService';
import { User, UserProfile } from 'oidc-client-ts';
import gravatar from 'gravatar';

// we need to extend oidc-client-ts UserProfile to work with the extra JWT properties returned by authentik
type MyUserProfile = UserProfile & {
  groups: string[] | null;
};

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null as User | null,
    adminView: false,
  }),
  getters: {
    isAdmin() {
      // returns false in any case other than a correctly set group
      const profile = <MyUserProfile | null>this.user?.profile;
      const groups: string[] = profile?.groups ?? [];
      return groups.includes('authentik Admins');
    },
    userName(): string | null {
      return this.user?.profile?.name ?? null;
    },
    gravatarURI(): string {
      return gravatar.url(this.user?.profile?.email ?? '', {
        protocol: 'https',
        s: '100',
        d: 'monsterid',
      });
    },
  },
  actions: {
    async fetchUser() {
      auth.getUser().then((user) => this.setUser(user));
    },
    setUser(user: User | null) {
      this.user = user;
    },
  },
});

export async function initializeUserStore() {
  const userStore = useUserStore();
  const events = auth.getUserManager().events;
  events.addUserLoaded((user: User) => userStore.setUser(user));
  // events.addUserUnloaded(() => userStore.setUser(null));
  await userStore.fetchUser();
}
