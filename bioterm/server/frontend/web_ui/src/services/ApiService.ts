import axios from "axios";
import { AxiosInstance, AxiosResponse } from "axios";
import { Controller, Dashboard, Device } from "src/types/types";
import auth from "./AuthService";
import { showError, showSuccess } from "./NotificationService";
import { RuleCreate, RuleModel, RuleUpdate } from "src/types/rules";

export class ApiService {
  private api: AxiosInstance;

  constructor() {
    this.api = axios.create({
      baseURL: process.env.API_URL,
      // headers: {
      //     'Content-Type': 'application/json',
      // }
    });

    this.api.interceptors.request.use(
      async (config) => {
        try {
          const access_token = await auth.getAccessToken();
          if (access_token) {
            config.headers.Authorization = `Bearer ${access_token}`;
          }
          return config;
        } catch (error) {
          throw new Error("Error retrieving access token");
        }
      },
      (error: Error) => {
        return Promise.reject(error);
      },
    );
  }

  public async getControllers(): Promise<Controller[]> {
    return this.api
      .get("/api/v0/controller/")
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        showError("Error fetching controllers.");
        throw error;
      });
  }

  public async getDashboard(controller_uuid: string): Promise<Dashboard> {
    return this.api
      .get(`/api/v0/controller/${controller_uuid}/dashboard`)
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        showError("Error fetching dashboard.");
        throw error;
      });
  }

  public async getDevices(controller_uuid: string): Promise<Device[]> {
    return this.api
      .get(`/api/v0/controller/${controller_uuid}/devices`)
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        showError("Error fetching devices.");
        throw error;
      });
  }

  public async getRules(controller_uuid: string): Promise<RuleModel[]> {
    return this.api
      .get(`/api/v0/rules/${controller_uuid}`)
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        showError("Error fetching rules.");
        throw error;
      });
  }

  public async syncRules(controller_uuid: string): Promise<AxiosResponse> {
    return this.api
      .get(`/api/v0/rules/${controller_uuid}/sync`)
      .catch((error) => {
        showError("Error syncing rules.");
        throw error;
      });
  }

  public async addRule(
    controller_uuid: string,
    rule: RuleCreate,
  ): Promise<void> {
    await this.api
      .post(`/api/v0/rules/${controller_uuid}`, rule)
      .then(() => {
        showSuccess("Successfully created rule");
      })
      .catch((error) => {
        showError("Failed to create rule");
        console.log(error);
        throw error;
      });
  }

  public async updateRule(
    controller_uuid: string,
    rule_uuid: string,
    rule: RuleUpdate,
  ): Promise<void> {
    await this.api
      .put(`/api/v0/rules/${controller_uuid}/${rule_uuid}`, rule)
      .then(() => {
        showSuccess("Successfully updated rule");
      })
      .catch((error) => {
        showError("Failed to update rule");
        console.log(error);
        throw error;
      });
  }

  public async deleteRule(
    controller_uuid: string,
    rule_uuid: string,
  ): Promise<void> {
    await this.api
      .delete(`/api/v0/rules/${controller_uuid}/${rule_uuid}`)
      .then(() => {
        showSuccess("Successfully deleted rule");
      })
      .catch((error) => {
        showError("Failed to delete rule");
        console.log(error);
        throw error;
      });
  }

  public async getDataExport(
    controller_uuid: string,
    start_date: string,
    end_date: string,
    device_uuids: string,
  ): Promise<AxiosResponse> {
    const apiUrl = `${process.env.API_URL}/api/v0/controller/${controller_uuid}/devices/data/?start_date=${start_date}&end_date=${end_date}&uuids=${device_uuids}`;

    // Step 1: Initiate the export process and get the task ID
    let response;
    try {
      response = await this.api.get(apiUrl);
    } catch (error) {
      showError("Error initiating data export.");
      throw error;
    }

    const taskId = response.data.task_id;

    // Step 2: Poll for task completion status
    let statusResponse;
    do {
      try {
        await new Promise((resolve) => setTimeout(resolve, 5000)); // Wait for 5 seconds before polling again
        statusResponse = await this.api.get(
          `${process.env.API_URL}/api/v0/controller/tasks/${taskId}/status`,
        );
      } catch (error) {
        showError("Error checking export task status.");
        throw error;
      }
    } while (statusResponse.data.status !== "completed");

    // Step 3: Download the file once the task is completed
    try {
      return await this.api.get(
        `${process.env.API_URL}/api/v0/controller/tasks/${taskId}/download`,
        { responseType: "blob" },
      );
    } catch (error) {
      showError("Error downloading exported data.");
      throw error;
    }
  }
}

const apiservice = new ApiService();
export default apiservice;
