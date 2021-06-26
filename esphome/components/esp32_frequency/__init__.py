import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID, CONF_FREQUENCY

CODEOWNERS = ["@esphome/core"]

esp32_frequency_ns = cg.esphome_ns.namespace("esp32_frequency")
FrequencyComponent = esp32_frequency_ns.class_("FrequencyComponent", cg.Component)
CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(FrequencyComponent),
        cv.Optional(CONF_FREQUENCY, default="240MHz"): cv.frequency,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    cg.add(var.set_frequency(config[CONF_FREQUENCY]))
