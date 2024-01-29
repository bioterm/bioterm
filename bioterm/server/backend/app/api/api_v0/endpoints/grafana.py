from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .......common.core.logger import get_module_logger
from .......common.models.grafana.base_models import DashboardCreate
from .......common.models.grafana.base_models import DashboardUpdate
from .......common.models.grafana.base_models import PanelCreate
from .......common.models.grafana.base_models import PanelUpdate
from .......common.models.grafana.database_models import DashboardModel
from .......common.models.grafana.database_models import PanelModel
from .....core.config import SQLALCHEMY_DATABASE_URI
from ....core.metadata import generate_metadata
from ...utils.security import credentials_noadmin_exception
from ...utils.security import User
from ...utils.security import validate

# from ....grafana.service import GrafanaService

# from .....core.config import GF_SECURITY_ADMIN_PASSWORD
# from .....core.config import GF_SECURITY_ADMIN_USERNAME
# from .....core.config import GF_SERVER_ROOT_URL

router = APIRouter()
logger = get_module_logger(__name__)

# SQLAlchemy setup
engine = create_engine(SQLALCHEMY_DATABASE_URI)  # set echo=True to increase verbosity
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@router.post("/dashboards/", tags=["grafana"])
async def create_dashboard(
    dashboard: DashboardCreate, current_user: User = Depends(validate)
):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    new_dashboard = DashboardModel(**dashboard.dict())
    db.add(new_dashboard)
    db.commit()
    db.refresh(new_dashboard)
    db.close()
    return new_dashboard


@router.get("/dashboards/", tags=["grafana"])
async def read_dashboards(current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    dashboards = db.query(DashboardModel).all()
    db.close()
    return dashboards


@router.put("/dashboards/{dashboard_id}", tags=["grafana"])
async def update_dashboard(
    dashboard_id: int,
    dashboard: DashboardUpdate,
    current_user: User = Depends(validate),
):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_dashboard = (
        db.query(DashboardModel).filter(DashboardModel.id == dashboard_id).first()
    )
    if not db_dashboard:
        db.close()
        raise HTTPException(status_code=404, detail="Dashboard not found")
    for key, value in dashboard.dict().items():
        setattr(db_dashboard, key, value)
    db.commit()
    db.close()
    return db_dashboard


@router.delete("/dashboards/{dashboard_id}", tags=["grafana"])
async def delete_dashboard(dashboard_id: int, current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_dashboard = (
        db.query(DashboardModel).filter(DashboardModel.id == dashboard_id).first()
    )
    if not db_dashboard:
        db.close()
        raise HTTPException(status_code=404, detail="Dashboard not found")

    db.delete(db_dashboard)
    db.commit()
    db.close()
    return {"status": "success"}


@router.get("/dashboards/metadata", tags=["grafana"])
async def get_metadata_dashboards(current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    form_elements_create = generate_metadata(PanelCreate)
    form_elements_update = generate_metadata(PanelUpdate)

    columns = [
        {
            "name": column.name,
            "label": column.name.upper(),
            "field": column.name,
            "align": "left",
            "sortable": True if column.primary_key else False,
        }
        for column in DashboardModel.__table__.columns
    ]

    return {
        "formElementsUpdate": form_elements_update,
        "formElementsCreate": form_elements_create,
        "columns": columns,
    }


@router.post("/panels/", tags=["grafana"])
async def create_panel(panel: PanelCreate, current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    new_panel = PanelModel(**panel.dict())
    db.add(new_panel)
    db.commit()
    db.refresh(new_panel)
    db.close()
    return new_panel


@router.get("/panels/", tags=["grafana"])
async def read_panels(current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    panels = db.query(PanelModel).all()
    db.close()
    return panels


@router.put("/panels/{panel_id}", tags=["grafana"])
async def update_panel(
    panel_id: int,
    panel: PanelUpdate,
    current_user: User = Depends(validate),
):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_panel = db.query(PanelModel).filter(PanelModel.id == panel_id).first()
    if not db_panel:
        db.close()
        raise HTTPException(status_code=404, detail="Panel not found")
    for key, value in panel.dict().items():
        setattr(db_panel, key, value)
    db.commit()
    db.close()
    return db_panel


@router.delete("/panels/{panel_id}", tags=["grafana"])
async def delete_panel(panel_id: int, current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_panel = db.query(PanelModel).filter(PanelModel.id == panel_id).first()
    if not db_panel:
        db.close()
        raise HTTPException(status_code=404, detail="Panel not found")

    db.delete(db_panel)
    db.commit()
    db.close()
    return {"status": "success"}


@router.get("/panels/metadata", tags=["grafana"])
async def get_metadat_panels(current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    form_elements_create = generate_metadata(PanelCreate)
    form_elements_update = generate_metadata(PanelUpdate)

    columns = [
        {
            "name": column.name,
            "label": column.name.upper(),
            "field": column.name,
            "align": "left",
            "sortable": True if column.primary_key else False,
        }
        for column in PanelModel.__table__.columns
    ]

    return {
        "formElementsUpdate": form_elements_update,
        "formElementsCreate": form_elements_create,
        "columns": columns,
    }


# class DataSource(BaseModel):
#     name: str
#     url: str
#     database: str
#     user: str
#     password: str


# class Dashboard(BaseModel):
#     name: str


# @router.post("/datasource", tags=["Grafana"])
# async def add_datasource(datasource: DataSource):
#     grafana = Grafana(
#         GF_SERVER_ROOT_URL, GF_SECURITY_ADMIN_USERNAME, GF_SECURITY_ADMIN_PASSWORD
#     )
#     return grafana.add_timescaledb_datasource(
#         datasource.name,
#         datasource.url,
#         datasource.database,
#         datasource.user,
#         datasource.password,
#     )


# @router.get("/datasource/postgres", tags=["Grafana"])
# async def get_postgres_datasources(current_user: User = Depends(validate)):
#     if "authentik Admins" not in current_user.groups:
#         raise credentials_noadmin_exception
#     grafana = Grafana(
#         GF_SERVER_ROOT_URL, GF_SECURITY_ADMIN_USERNAME, GF_SECURITY_ADMIN_PASSWORD
#     )
#     return grafana.get_postgres_data_sources()


# @router.post("/dashboard", tags=["Grafana"])
# async def create_dashboard(dashboard: Dashboard):
#     grafana = Grafana(
#         GF_SERVER_ROOT_URL, GF_SECURITY_ADMIN_USERNAME, GF_SECURITY_ADMIN_PASSWORD
#     )
#     return grafana.create_dashboard(dashboard.name)


# @router.get("/dashboard/{uid}", tags=["Grafana"])
# async def read_dashboard(uid: str):
#     grafana = Grafana(
#         GF_SERVER_ROOT_URL, GF_SECURITY_ADMIN_USERNAME, GF_SECURITY_ADMIN_PASSWORD
#     )
#     return grafana.read_dashboard(uid)


# @router.post("/dashboard/{uid}/update", tags=["Grafana"])
# async def update_dashboard(uid: str, dashboard: Dashboard):
#     grafana = Grafana(
#         GF_SERVER_ROOT_URL, GF_SECURITY_ADMIN_USERNAME, GF_SECURITY_ADMIN_PASSWORD
#     )
#     db = grafana.read_dashboard(uid)
#     db.json["dashboard"]["title"] = dashboard.name
#     return grafana.update_dashboard(db)
