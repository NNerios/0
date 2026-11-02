# =====================================================================
# CORE ENGINE: CER-C GRAVITATIONAL INDUCTION & VACUUM POLARIZATION
# =====================================================================
import math

def gauge_quantum_decay_w(density_vac, rho_max, decay_constant=0.1):
    if not rho_max > 0:
        return -1.0
    density_ratio = density_vac / rho_max
    decay_profile = math.exp(-decay_constant * (1.0 - density_ratio))
    return max(min(-1.0 * density_ratio * decay_profile, 0.0), -1.0)

def gauge_repulsive_spring_AE(density_total, rho_max, polarization_power=2.0):
    if not rho_max > 0 or not density_total > 0:
        return 0.0
    return min((density_total / rho_max) ** polarization_power, 1.0)

def gauge_gravitational_vacuum_induction(z, omega_vacuum, H0_observed, induction_coupling=1.5e-5):
    """
    GRAVITATIONAL VACUUM INDUCTION FIELD:
    Calculates the energetic excitation of virtual states caused by 
    high-redshift space-time compression and gravitational shaking.
    """
    gravitational_compression = (1.0 + z) ** 3
    induced_excitation = omega_vacuum * induction_coupling * (H0_observed ** 2) * gravitational_compression
    return induced_excitation

def compute_sound_speed_diagnostic(density_vac, rho_max, decay_constant=0.1):
    """
    INTERNAL STRUCTURAL DIAGNOSTIC: Bounded to the observable speed of light.
    """
    if not rho_max > 0:
        return 0.0
    w_val = gauge_quantum_decay_w(density_vac, rho_max, decay_constant)
    cs_squared = abs(w_val) + ((density_vac / rho_max) * decay_constant)
    return max(min(cs_squared, 1.0), 0.0)

def calculate_h_squared_observable(total_macro_density, rho_max, normalizing_amplitude):
    """
    STRICTLY LOCKED MACRO VARIABLE:
    Fuses background densities with the alpha cyclical bounce gauge.
    """
    alpha_cyclical_gauge = gauge_repulsive_spring_AE(total_macro_density, rho_max)
    macro_kinetic_sum = total_macro_density * normalizing_amplitude
    return max(0.0, macro_kinetic_sum * (1.0 - alpha_cyclical_gauge))
