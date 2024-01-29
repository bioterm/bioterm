import os
from logging.config import fileConfig

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from sqlalchemy import pool


load_dotenv()

POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", default="timescaledb:5432")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
)


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
from bioterm.common.models.base import Base  # noqa: E402
from bioterm.common.models.apikeys.database_models import APIKeyModel  # noqa: E402
from bioterm.common.models.controllers.database_models import (  # noqa: E402
    ControllerModel,
)
from bioterm.common.models.devices.database_models import DeviceModel  # noqa: E402
from bioterm.common.models.grafana.database_models import PanelModel  # noqa: E402
from bioterm.common.models.grafana.database_models import DashboardModel  # noqa: E402
from bioterm.common.models.gdpr.database_models import LegalContent  # noqa: E402
from bioterm.common.models.logs.database_models import LogEntry  # noqa: E402
from bioterm.common.models.rules.database_models import RuleModel  # noqa: E402

# List all table models here, to limit alembic to these tables
imported_models = [
    APIKeyModel,
    ControllerModel,
    DeviceModel,
    PanelModel,
    DashboardModel,
    LegalContent,
    LogEntry,
    RuleModel,
]

target_metadata = Base.metadata
# target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def include_object(object, name, type_, reflected, compare_to):
    # If it's a table, check if it's in our imported models' tables
    if type_ == "table":
        return object in [model.__table__ for model in imported_models]
    return True


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # Override the value in alembic.ini with the constructed URL
    config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URI)

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
