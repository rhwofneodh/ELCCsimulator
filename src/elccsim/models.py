# src/elccsim/models.py
from dataclasses import dataclass
from typing import List

@dataclass
class ThermalGenSpec:
    name: str
    icap: float
    overnight_cost: float
    fixed_om: float
    variable_om: float
    heat_rate_full: float
    heat_rate_duct: float
    eford: float
    elcc: float
    age: int
    life: int
    lead_time: int

@dataclass
class SolarGenSpec:
    name: str
    nameplate: float
    overnight_cost: float
    fixed_om: float
    var_om: float
    cap_factor: float
    degradation: float
    elcc: float
    age: int
    life_fin: int
    life_phys: int
    lead_time: int

@dataclass
class BenchmarkInputs:
    thermal: ThermalGenSpec
    solar: SolarGenSpec
    peak_load: float
    irm: float
    fpr: float
    elcc_ref: float
