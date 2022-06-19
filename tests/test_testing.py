import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    LongType,
    IntegerType,
    StringType,
    DoubleType,
)
from inklings_spark_utils.testing import are_dfs_equal, are_dfs_approx_equal


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local").appName("chispa").getOrCreate()


def test_are_dataframe_equals(spark):

    schema = StructType(
        [StructField("id", LongType()), StructField("txt", StringType())]
    )
    mockInput1 = spark.createDataFrame(
        [
            (1, "foo"),
            (2, "bar"),
        ],
        schema,
    )

    mockInput2 = spark.createDataFrame(
        [
            (1, "foo"),
            (2, "bar"),
        ],
        schema,
    )

    assert are_dfs_equal(mockInput1, mockInput2)


def test_are_dataframe_equals_fails_with_diff_schemas(spark):
    mockInput1 = spark.createDataFrame(
        [
            (1, "foo"),
            (2, "bar"),
        ],
        StructType([StructField("id", LongType()), StructField("txt", StringType())]),
    )

    mockInput2 = spark.createDataFrame(
        [
            (1, "foo"),
            (2, "bar"),
        ],
        StructType(
            [StructField("id", IntegerType()), StructField("txt", StringType())]
        ),
    )
    assert not are_dfs_equal(mockInput1, mockInput2)


def test_are_dataframe_equals_fails_with_diff_values(spark):

    schema = StructType(
        [StructField("id", LongType()), StructField("txt", StringType())]
    )

    mockInput1 = spark.createDataFrame(
        [
            (1, "foo"),
            (2, "bar"),
        ],
        schema,
    )

    mockInput2 = spark.createDataFrame(
        [
            (2, "foo"),
            (1, "bar"),
        ],
        schema,
    )
    assert not are_dfs_equal(mockInput1, mockInput2)


def test_are_dataframe_approx_equals_works_with_precision(spark):

    schema = StructType(
        [StructField("id", LongType()), StructField("price", DoubleType())]
    )

    mockInput1 = spark.createDataFrame(
        [
            (1, 1.88),
            (2, 1.99),
        ],
        schema,
    )

    mockInput2 = spark.createDataFrame(
        [
            (1, 1.87),
            (2, 1.99),
        ],
        schema,
    )
    assert are_dfs_approx_equal(mockInput1, mockInput2)
