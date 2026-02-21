from typing import Any, Dict

import esphome.config_validation as cv
from esphome.components import binary_sensor

from . import const, schema, validate, generate

DEPENDENCIES = [ const.OPENTHERM ]
COMPONENT_TYPE = const.BINARY_SENSOR

def get_entity_validation_schema(entity: schema.BinarySensorSchema) -> cv.Schema:
    return binary_sensor.binary_sensor_schema(
        device_class = entity.get("device_class", ""),
        icon = entity.get("icon", "")
    )

CONFIG_SCHEMA = validate.create_component_schema(schema.BINARY_SENSORS, get_entity_validation_schema)

async def to_code(config: Dict[str, Any]) -> None:
    await generate.component_to_code(
        COMPONENT_TYPE,
        schema.BINARY_SENSORS,
        binary_sensor.BinarySensor, 
        generate.create_only_conf(binary_sensor.new_binary_sensor), 
        config
    )
