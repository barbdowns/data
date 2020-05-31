# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict, List, Tuple
from pandas import DataFrame, merge, Int64Dtype
from lib.pipeline import DataPipeline, DataPipeline, PipelineChain
from pipelines.mobility.apple_mobility_pipeline import AppleMobilityPipeline
from pipelines.mobility.google_mobility_pipeline import GoogleMobilityPipeline


class MobilityPipelineChain(PipelineChain):

    schema: Dict[str, type] = {
        "date": str,
        "key": str,
        "mobility_driving": float,
        "mobility_transit": float,
        "mobility_walking": float,
        "mobility_retail_and_recreation": float,
        "mobility_grocery_and_pharmacy": float,
        "mobility_parks": float,
        "mobility_transit_stations": float,
        "mobility_workplaces": float,
        "mobility_residential": float,
    }

    pipelines: List[Tuple[DataPipeline, Dict[str, Any]]] = [
        (AppleMobilityPipeline(), {}),
        (GoogleMobilityPipeline(), {}),
    ]
