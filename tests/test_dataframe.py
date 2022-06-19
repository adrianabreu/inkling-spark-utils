import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, LongType, IntegerType, StringType
from inklings_spark_utils.dataframe import (
    complete_dataframe,
    select_schema_columns,
    cast_dataframe,
)


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local").appName("chispa").getOrCreate()


def test_complete_dataframe(spark):
    mockInput = spark.createDataFrame(
        [
            (1, "foo"),
            (2, "bar"),
        ],
        ["id", "txt"],
    )

    mockSchema = StructType(
        [
            StructField("id", LongType()),
            StructField("txt", StringType()),
            StructField("age", LongType()),
        ]
    )

    expected_schema = [("id", LongType()), ("txt", StringType()), ("age", LongType())]

    actual = [
        (x.name, x.dataType)
        for x in complete_dataframe(mockInput, mockSchema).schema.fields
    ]

    assert expected_schema == actual


def test_cast_dataframe(spark):
    mockInput = spark.createDataFrame(
        [
            (1, "foo"),
            (2, "bar"),
        ],
        ["id", "txt"],
    )

    mockSchema = StructType(
        [StructField("id", LongType()), StructField("txt", StringType())]
    )

    expected_schema = [StructField("id", LongType()), StructField("txt", StringType())]

    actual = [
        (x.name, x.dataType)
        for x in cast_dataframe(mockInput, mockSchema).schema.fields
    ]

    assert set([(x.name, x.dataType) for x in expected_schema]) == set(actual)


def test_select_schema_cols(spark):
    mockInput = spark.createDataFrame(
        [
            (1, "foo", "bar"),
            (2, "bar", "baz"),
        ],
        ["id", "txt", "name"],
    )

    target_schema = StructType([StructField("id", IntegerType())])

    actual = [
        (x.name) for x in select_schema_columns(mockInput, target_schema).schema.fields
    ]

    assert [x.name for x in target_schema.fields] == actual
