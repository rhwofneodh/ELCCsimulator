def thermal_acc_factor(eford: float, use_elcc: bool, elcc: float) -> float:
    return 1 - eford if not use_elcc else elcc

def renewable_acc_factor(elcc: float, perf_adj: float=1.0) -> float:
    return elcc * perf_adj
