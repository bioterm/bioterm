import { UserManager, WebStorageStateStore, User, Log } from 'oidc-client-ts';

if (process.env.DEV) {
  Log.setLogger(console);
}
export class AuthService {
  private userManager: UserManager;

  constructor() {
    //const settings: any = {
    const settings = {
      userStore: new WebStorageStateStore({ store: window.localStorage }),
      authority: process.env.AUTH0_DOMAIN || '',
      metadataUrl: process.env.AUTHENTIK_METADATA_URL || '',
      client_id: process.env.AUTHENTIK_CLIENT_ID || '',
      redirect_uri: window.location.origin + '/callback.html', //this could also be replaced by an env variable, but this way development with localhost works
      //response_type: 'id_token token',
      response_type: 'code',
      scope: 'openid profile email',
      includeIdTokenInSilentRenew: true,
      loadUserInfo: true,
      automaticSilentRenew: true,
      monitorSession: true,
      post_logout_redirect_uri:
        process.env.AUTHENTIK_POST_LOGOUT_REDIRECT_URI || '',
      filterProtocolClaims: true,
    };

    this.userManager = new UserManager(settings);
  }

  public getUserManager(): UserManager {
    return this.userManager;
  }

  public getUser(): Promise<User | null> {
    return this.userManager.getUser();
  }

  public getAccessToken(): Promise<string | null> {
    return this.getUser().then((user) => user?.access_token ?? null);
  }

  public login(): Promise<void> {
    return this.userManager.signinRedirect();
  }

  public logout(): Promise<void> {
    return this.userManager.signoutRedirect();
  }

  public async isLoggedIn(): Promise<boolean> {
    const user: User | null = await this.getUser();

    return user !== null && !user.expired;
  }
}

const auth = new AuthService();
export default auth;
