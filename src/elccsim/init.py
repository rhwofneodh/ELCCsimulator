# src/elccsim/init.py
import yaml
from pathlib import Path

from .models import (
    ThermalGenSpec,
    SolarGenSpec,
    BenchmarkInputs,
)

def load_benchmark_inputs(
    filename: str = "benchmark_inputs.yaml",
    inputs_dir: str = None,
) -> BenchmarkInputs:
    """
    Load the year-0 benchmark inputs from a YAML file and return a populated
    BenchmarkInputs dataclass.
    """
    # if inputs_dir not provided, assume project_root/inputs/
    if inputs_dir is None:
        # find project root by looking for this file's parent twice
        project_root = Path(__file__).parent.parent.parent
        inputs_dir = project_root / "inputs"
    else:
        inputs_dir = Path(inputs_dir)

    path = inputs_dir / filename
    if not path.exists():
        raise FileNotFoundError(f"Benchmark inputs file not found: {path}")

    # parse YAML
    with open(path, "r") as fp:
        data = yaml.safe_load(fp)

    # Build dataclasses
    thermal_data = data["thermal"]
    solar_data = data["solar"]
    year0 = data["year0"]

    thermal = ThermalGenSpec(
        name=thermal_data["name"],
        icap=thermal_data["net_summer_icap_mw"],
        overnight_cost=thermal_data["overnight_cost_usd_per_kw"],
        fixed_om=thermal_data["fixed_om_usd_per_kw_yr"],
        variable_om=thermal_data["variable_om_usd_per_mwh"],
        heat_rate_full=thermal_data["heat_rate_full_btu_per_kwh"],
        heat_rate_duct=thermal_data["heat_rate_duct_btu_per_kwh"],
        eford=thermal_data["eford_pct"],
        elcc=thermal_data["elcc_pct"],
        age=thermal_data["current_age_yr"],
        life=thermal_data["economic_life_yr"],
        lead_time=thermal_data["build_lead_time_yr"],
    )

    solar = SolarGenSpec(
        name=solar_data["name"],
        nameplate=solar_data["nameplate_mw_ac"],
        overnight_cost=solar_data["overnight_cost_usd_per_kw"],
        fixed_om=solar_data["fixed_om_usd_per_kw_yr"],
        var_om=solar_data["variable_om_usd_per_mwh"],
        cap_factor=solar_data["capacity_factor_pct"],
        degradation=solar_data["degradation_pct_per_yr"],
        elcc=solar_data["elcc_pct"],
        age=solar_data["current_age_yr"],
        life_fin=solar_data["economic_life_fin_yr"],
        life_phys=solar_data["economic_life_phys_yr"],
        lead_time=solar_data["build_lead_time_yr"],
    )

    inputs = BenchmarkInputs(
        thermal=thermal,
        solar=solar,
        peak_load=year0["peak_load_mw"],
        irm=year0["irm_pct"],
        fpr=year0["fpr"],
        elcc_ref=year0["elcc_ref_pct"],
    )

    return inputs
