from typing import Any, Dict

import esphome.config_validation as cv
from esphome.components import sensor

from . import const, schema, validate, generate

DEPENDENCIES = [ const.OPENTHERM ]
COMPONENT_TYPE = const.SENSOR

def get_entity_validation_schema(entity: schema.SensorSchema) -> cv.Schema:
    return sensor.sensor_schema(
        unit_of_measurement = entity.get("unit_of_measurement", ""),
        accuracy_decimals = entity["accuracy_decimals"],
        device_class = entity.get("device_class", ""),
        icon = entity.get("icon", ""),
        state_class = entity["state_class"]
    )

CONFIG_SCHEMA = validate.create_component_schema(schema.SENSORS, get_entity_validation_schema)

async def to_code(config: Dict[str, Any]) -> None:
    await generate.component_to_code(
        COMPONENT_TYPE, 
        schema.SENSORS,
        sensor.Sensor, 
        generate.create_only_conf(sensor.new_sensor), 
        config
    )
