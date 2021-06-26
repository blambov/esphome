import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID, CONF_FREQUENCY

CODEOWNERS = ["@esphome/core"]

ESP32_FREQUENCIES = [240000000.0, 160000000.0, 80000000.0]

esp32_frequency_ns = cg.esphome_ns.namespace("esp32_frequency")
FrequencyComponent = esp32_frequency_ns.class_("FrequencyComponent", cg.Component)
CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(FrequencyComponent),
        cv.Optional(CONF_FREQUENCY, default="240MHz"): cv.All(
            cv.only_on_esp32, cv.frequency, cv.one_of(*ESP32_FREQUENCIES)
        ),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    cg.add(var.set_frequency(config[CONF_FREQUENCY]))
