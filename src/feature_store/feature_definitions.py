# This is an example feature definition file

from datetime import timedelta

import pandas as pd

from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource,
    Project,
    PushSource,
    RequestSource
)
from feast.feature_logging import LoggingConfig
from feast.infra.offline_stores.file_source import FileLoggingDestination
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import PostgreSQLSource
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Float32, Float64, Int64, Json, Map, String, Struct

project = Project(name="iris_project")

iris_source = PostgreSQLSource(
    name="iris_source",
    query="""
        SELECT
            id,
            sepal_length,
            sepal_width,
            petal_length,
            petal_width,
            variety,
            event_timestamp
        FROM iris_table
    """,
    timestamp_field="event_timestamp"
)

iris = Entity(
    name="iris_id",
    join_keys=["id"]
)

iris_features = FeatureView(
    name="iris_features",
    entities=[iris],
    ttl=timedelta(days=365),
    source=iris_source,
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
        Field(name="variety", dtype=String)
    ],
)
