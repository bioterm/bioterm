import json

import requests
from requests.auth import HTTPBasicAuth

from .....common.core.config import getenv_boolean
from .....common.core.logger import get_module_logger


logger = get_module_logger(__name__)


class GrafanaAPIResponse:
    def __init__(self, status: str, message: str, raw_response: requests.Response):
        self.status = status
        self.message = message
        self.raw_response = raw_response

    def is_successful(self) -> bool:
        return self.status == "success"

    def __str__(self) -> str:
        return self.message


class GrafanaAPI:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    def __init__(self, url: str, auth: HTTPBasicAuth):
        self.url = url
        self.auth = auth

    def _switch_organization(
        self,
        endpoint: str,
        data: dict,
    ) -> GrafanaAPIResponse:
        response = requests.post(
            f"{self.url}{endpoint}",
            data=json.dumps(data),
            headers=self.headers,
            auth=self.auth,
            verify=getenv_boolean("USE_TLS"),
        )

        if response.status_code == 200:
            return GrafanaAPIResponse(
                status="success",
                message=(
                    f"Success creating resource {data} at {endpoint}: "
                    f"{response.status_code} {response.text}"
                ),
                raw_response=response,
            )
        else:
            return GrafanaAPIResponse(
                status="error",
                message=(
                    f"Error creating resource {data} at {endpoint}: "
                    f"{response.status_code} {response.text}"
                ),
                raw_response=response,
            )

    def _create_resource_apikey(
        self,
        endpoint: str,
        data: dict,
        apikey: str,
    ) -> GrafanaAPIResponse:
        # response = requests.post(
        #     f"{self.url}{endpoint}",
        #     data=json.dumps(data),
        #     headers=self.headers,
        #     auth=self.auth,
        #     verify=getenv_boolean("USE_TLS"),
        # )
        pass

    def _create_resource_basic_auth(
        self,
        endpoint: str,
        data: dict,
    ) -> GrafanaAPIResponse:
        response = requests.post(
            f"{self.url}{endpoint}",
            data=json.dumps(data),
            headers=self.headers,
            auth=self.auth,
            verify=getenv_boolean("USE_TLS"),
        )

        if response.status_code == 200:
            return GrafanaAPIResponse(
                status="success",
                message=(
                    f"Success creating resource {data} at {endpoint}: "
                    f"{response.status_code} {response.text}"
                ),
                raw_response=response,
            )
        else:
            return GrafanaAPIResponse(
                status="error",
                message=(
                    f"Error creating resource {data} at {endpoint}: "
                    f"{response.status_code} {response.text}"
                ),
                raw_response=response,
            )

    def create_folder(self, folder_name: str) -> GrafanaAPIResponse:
        folder_json = {
            "title": folder_name,
        }
        return self._create_resource_basic_auth(
            endpoint="/api/folders",
            data=folder_json,
        )

    def create_team(self, team_name: str) -> GrafanaAPIResponse:
        team_json = {
            "name": team_name,
        }
        return self._create_resource_basic_auth(
            endpoint="/api/teams",
            data=team_json,
        )

    def create_organization(self, org_name: str) -> GrafanaAPIResponse:
        team_json = {
            "name": org_name,
        }
        return self._create_resource_basic_auth(
            endpoint="/api/orgs",
            data=team_json,
        )

    def create_dashboard(
        self, dashboard_name: str, folder_uid: str
    ) -> GrafanaAPIResponse:
        dashboard_json = {
            "dashboard": {
                "id": None,
                "uid": None,
                "title": dashboard_name,
                "schemaVersion": 30,
                "refresh": "1s,5s,10s,30s",
            },
            "folderUid": folder_uid,
            "overwrite": True,
        }

        return self._create_resource_basic_auth(
            endpoint="/api/dashboards/db",
            data=dashboard_json,
        )

    def update_dashboard(self, dashboard):
        response = requests.post(
            f"{self.url}/api/dashboards/db",
            data=json.dumps(dashboard.json),
            headers=self.headers,
            auth=self.auth,
            verify=getenv_boolean("USE_TLS"),
        )

        if response.status_code == 200:
            print("Dashboard updated successfully")
        else:
            print(f"Error updating dashboard: {response.status_code} {response.text}")

    def read_dashboard(self, uid):
        response = requests.get(
            f"{self.url}/api/dashboards/uid/{uid}",
            headers=self.headers,
            auth=self.auth,
            verify=getenv_boolean("USE_TLS"),
        )

        if response.status_code == 200:
            print("Dashboard read successfully")
            response_json = response.json()
            return Dashboard(response_json, response_json["dashboard"]["uid"])
        else:
            print(f"Error reading dashboard: {response.status_code} {response.text}")
            return None

    def add_timescaledb_datasource(self, name, url, database, user, password):
        datasource_json = {
            "name": name,
            "type": "postgres",
            "url": url,
            "database": database,
            "user": user,
            "password": password,
            "access": "proxy",
            "basicAuth": False,
        }

        response = requests.post(
            f"{self.url}/api/datasources",
            data=json.dumps(datasource_json),
            headers=self.headers,
            auth=self.auth,
            verify=getenv_boolean("USE_TLS"),
        )

        if response.status_code == 200:
            print("Data source added successfully")
            response_json = response.json()
            return response_json["id"]
        else:
            print(f"Error adding data source: {response.status_code} {response.text}")
            return None

    def get_postgres_data_sources(self):
        response = requests.get(
            f"{self.url}/api/datasources",
            headers=self.headers,
            auth=self.auth,
            verify=getenv_boolean("USE_TLS"),
        )
        logger.debug(response.json())

        if response.status_code == 200:
            data_sources_json = response.json()
            postgres_data_sources = [
                ds for ds in data_sources_json if ds["type"] == "postgres"
            ]
            return postgres_data_sources
        else:
            print(f"Error getting data sources: {response.status_code} {response.text}")
            return None


class Dashboard:
    ALLOWED_PANEL_TYPES = {"timeseries"}

    def __init__(self, dashboard_json, uid=None):
        self.json = dashboard_json
        self.uid = uid

    def get_title(self):
        return self.json["dashboard"]["title"]

    # def get_panels(self):
    #     return self.json["dashboard"]["panels"]

    # def add_panel(self, panel_title, panel_type, gridPos, targets):
    #     if panel_type not in self.ALLOWED_PANEL_TYPES:
    #         raise ValueError(
    #             f"Invalid panel type: {panel_type}. Allowed types are: "
    #             f"{', '.join(self.ALLOWED_PANEL_TYPES)}"
    #         )
    #     new_panel = {
    #         "title": panel_title,
    #         "type": panel_type,
    #         "gridPos": gridPos,
    #         "targets": targets,
    #     }
    #     self.json["dashboard"]["panels"].append(new_panel)
