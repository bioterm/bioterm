from requests.auth import HTTPBasicAuth

from .....common.core.logger import get_module_logger
from .....common.models.grafana.base_models import DashboardCreate
from ...core.config import GF_SECURITY_ADMIN_PASSWORD
from ...core.config import GF_SECURITY_ADMIN_USERNAME
from ...core.config import GF_SERVER_ROOT_URL
from .api import GrafanaAPI

# from .api import GrafanaAPIResponse

logger = get_module_logger(__name__)


class GrafanaService:
    def __init__(self) -> None:
        self.api = GrafanaAPI(
            url=GF_SERVER_ROOT_URL,
            auth=HTTPBasicAuth(GF_SECURITY_ADMIN_USERNAME, GF_SECURITY_ADMIN_PASSWORD),
        )

    def setup_controller(self, uuid: str) -> DashboardCreate:
        try:
            # creating an organization and sorting users into them might be one
            # possible way to hide certain data from them
            # org_response = self.api.create_organization(org_name=uuid)
            # if not org_response.is_successful():
            #     raise Exception(f"Error in create_team: {org_response.message}")
            # parsed_org_response = org_response.raw_response.json()
            # org_id = parsed_org_response.get("id")

            team_response = self.api.create_team(team_name=uuid)
            if not team_response.is_successful():
                raise Exception(f"Error in create_team: {team_response.message}")

            folder_response = self.api.create_folder(folder_name=f"FLR_{uuid}")
            if not folder_response.is_successful():
                raise Exception(f"Error in create_folder: {folder_response.message}")

            parsed_folder_response = folder_response.raw_response.json()
            folder_uid = parsed_folder_response.get("uid")
            logger.debug(f"Folder UID is {folder_uid}")

            dashboard_response = self.api.create_dashboard(
                dashboard_name=uuid, folder_uid=folder_uid
            )
            if not dashboard_response.is_successful():
                raise Exception(
                    f"Error in create_dashboard: {dashboard_response.message}"
                )

            parsed_dashboard_response = dashboard_response.raw_response.json()
            dashboard_uid = parsed_dashboard_response.get("uid")
            dashboard_url = parsed_dashboard_response.get("url")

        except Exception as e:
            logger.error(f"Error while setting up controller: {e}")
            self.remove_controller(uuid=uuid)
            dashboard_uid = None

        if dashboard_uid:
            return DashboardCreate(uid=dashboard_uid, link=dashboard_url)
        return None

        # methods = [
        #     (self.api.create_team, {"team_name": uuid}),
        #     (self.api.create_folder, {"folder_name": uuid}),
        #     (
        #         self.api.create_dashboard,
        #         {"dashboard_name": uuid},
        #     ),
        # ]

        # dashboard_uid = None

        # for method, kwargs in methods:
        #     try:
        #         response = method(**kwargs)

        #         # Check if the returned object is of type APIResponse
        #         if not isinstance(response, GrafanaAPIResponse):
        #             raise InvalidAPIResponseError(
        #                 f"Method {method.__name__} did not return an "
        #                 f"GrafanaAPIResponse object."
        #             )

        #         # Check the status of the returned APIResponse
        #         if not response.is_successful():
        #             logger.error(
        #                 f"Error while executing {method.__name__}: {response.message}"
        #             )
        #             self.remove_controller(uuid=uuid)
        #             dashboard_uid = None
        #             break

        #         if method == self.api.create_dashboard:
        #             parsed_response = response.raw_response.json()
        #             dashboard_uid = parsed_response.get("uid")

        #     except InvalidAPIResponseError as e:
        #         logger.error(str(e))
        #         self.remove_controller(uuid=uuid)
        #         dashboard_uid = None
        #         break

        #     except Exception as e:
        #         logger.error(f"Error while executing {method.__name__}: {e}")
        #         self.remove_controller(uuid=uuid)
        #         dashboard_uid = None
        #         break

        # return dashboard_uid

    def remove_controller(self, uuid: str):
        pass


# class InvalidAPIResponseError(Exception):
#     """Raised when a method does not return an expected APIResponse object."""

#     pass
