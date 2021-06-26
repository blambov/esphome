#pragma once

#include "esphome/core/component.h"

namespace esphome {
namespace esp32_frequency {

class FrequencyComponent : public Component {
 public:
  void setup() override;
  void set_frequency(float frequency) { this->frequency_ = frequency; }
  float get_setup_priority() const override;
  void dump_config() override;

 protected:
  float frequency_;
};

}  // namespace esp32_frequency
}  // namespace esphome
