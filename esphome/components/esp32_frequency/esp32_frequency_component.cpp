#include "esp32_frequency_component.h"
#include "esphome/core/log.h"
#include "esphome/core/helpers.h"
#include "esphome/core/defines.h"
#include "esphome/core/version.h"

#ifdef ARDUINO_ARCH_ESP32
#include <esp32-hal-cpu.h>
#endif

namespace esphome {
namespace esp32_frequency {

static const char *const TAG = "esp32_frequency";

void FrequencyComponent::dump_config() {
#ifdef ARDUINO_ARCH_ESP32
  ESP_LOGD(TAG, "CPU Frequency: %u", getCpuFrequencyMhz());
  ESP_LOGD(TAG, "XTAL Frequency: %u", getXtalFrequencyMhz());
  ESP_LOGD(TAG, "APB Frequency: %u", getApbFrequency());
#endif
}
void FrequencyComponent::setup() {
#ifdef ARDUINO_ARCH_ESP32
  int freq = this->frequency_;
  ESP_LOGI(TAG, "Setting frequency to %u Mhz", freq);
  setCpuFrequencyMhz(freq);
  ESP_LOGD(TAG, "CPU Frequency: %u", getCpuFrequencyMhz());
#endif
}
float FrequencyComponent::get_setup_priority() const { return setup_priority::PROCESSOR; }

}  // namespace esp32_frequency
}  // namespace esphome
