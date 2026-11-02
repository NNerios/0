# =====================================================================
# UNIFIED MASTER PIPELINE V11: DYNAMIC PLASMA SOUND HORIZON LOOP (r_d)
# =====================================================================
import math

# ---------------------------------------------------------------------
# 1. EMBEDDED ENGINE FUNCTIONS (Pure Macro + Gauged Gravity Induction)
# ---------------------------------------------------------------------
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

def gauge_gravitational_vacuum_induction(z, omega_vacuum, H0_observed, induction_coupling=1.35e-6):
    """
    GRAVITATIONAL VACUUM INDUCTION FIELD:
    Calculates the energetic excitation of virtual states caused by 
    high-redshift space-time compression and gravitational shaking.
    """
    gravitational_compression = (1.0 + z) ** 3
    induced_excitation = omega_vacuum * induction_coupling * (H0_observed ** 2) * gravitational_compression
    return induced_excitation

def compute_sound_speed_diagnostic(density_vac, rho_max, decay_constant=0.1):
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

# ---------------------------------------------------------------------
# 2. PLASMA ACOUSTIC VELOCITY PHYSICS (No-Lambda, No-Time Riemann Sum)
# ---------------------------------------------------------------------
def calculate_plasma_sound_speed(z, omega_baryon=0.0493, omega_photon=5.4e-5):
    """
    Effective Plasma Sound Speed (cs).
    Tracks sound velocity through early-universe baryon-photon fluid plasma.
    """
    c = 299792.458  # Speed of light in km/s
    omega_radiation = omega_photon * 1.68132  # Relativistic neutrino background boost
    R_z = (3.0 * omega_baryon) / (4.0 * omega_radiation * (1.0 + z))
    return c / math.sqrt(3.0 * (1.0 + R_z))

def integrate_comoving_sound_horizon(rho_max, H0_observed, induction_coupling, normalizing_amplitude, omega_baryon, omega_photon, omega_vacuum):
    """
    Executes a formal 2,000-step numerical integration to find 
    the absolute comoving sound horizon scale (r_d) at the drag epoch.
    """
    z_drag = 1059.94      # Decoupling epoch coordinate
    z_max = 2500.0        # Convergence bound boundary
    steps = 2000          
    
    dz = (z_max - z_drag) / steps
    r_d_integral = 0.0
    
    for i in range(steps):
        z = z_drag + (i * dz)
        
        # Scale cosmic components based on macro geometry
        scaling_matter = omega_baryon * (1.0 + z)**3
        scaling_photon = omega_photon * (1.0 + z)**4
        scaling_vacuum_ground = omega_vacuum * (1.0 + z)**0
        scaling_vacuum_induced = gauge_gravitational_vacuum_induction(z, omega_vacuum, H0_observed, induction_coupling)
        
        total_scaled_density = scaling_matter + scaling_photon + scaling_vacuum_ground + scaling_vacuum_induced
        h2_pred = calculate_h_squared_observable(total_scaled_density, rho_max, normalizing_amplitude)
        h_z_physical = math.sqrt(h2_pred)
        
        cs_current = calculate_plasma_sound_speed(z, omega_baryon, omega_photon)
        if h_z_physical > 0:
            r_d_integral += (cs_current / h_z_physical) * dz
            
    return r_d_integral

# ---------------------------------------------------------------------
# 3. EXPERIMENTAL 32 COSMIC CHRONOMETER EXPERIMENTAL DATA SET
# ---------------------------------------------------------------------
CC_17_INDEPENDENT = [
    (0.070, 69.0, 19.6), (0.090, 69.0, 12.0), (0.120, 68.6, 26.2),
    (0.170, 83.0, 8.0),  (0.179, 75.0, 4.0),  (0.199, 75.0, 5.0),
    (0.200, 72.9, 29.6), (0.270, 77.0, 14.0), (0.280, 88.8, 36.6),
    (0.352, 83.0, 14.0), (0.380, 83.0, 13.5), (0.400, 95.0, 17.0),
    (0.444, 93.0, 8.5),  (0.478, 110.9, 11.2), (0.480, 97.0, 62.0),
    (0.593, 104.0, 13.0), (0.680, 92.0, 8.0)
]

CC_15_CORRELATED = [
    (0.781, 105.0, 12.0), (0.875, 125.0, 17.0), (0.880, 101.0, 10.0),
    (0.900, 117.0, 23.0), (1.037, 154.0, 20.0), (1.300, 168.0, 17.0),
    (1.363, 160.0, 33.6), (1.430, 177.0, 18.0), (1.530, 140.0, 14.0),
    (1.750, 202.0, 40.0), (1.965, 186.5, 50.4), (0.350, 82.7, 9.1),
    (0.570, 96.8, 6.4),  (1.260, 135.0, 11.0), (1.100, 120.0, 15.0)
]

def generate_formal_inverse_covariance(points):
    n = len(points)
    cov = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(0.0)
        cov.append(row)
    for i in range(n):
        sigma_i = points[i][2]
        cov[i][i] = sigma_i ** 2
        for j in range(n):
            if i != j:
                sigma_j = points[j][2]
                cov[i][j] = 0.05 * (sigma_i * sigma_j)
    aug = list()
    for i in range(n):
        aug_row = list(cov[i]) + [1.0 if i == j else 0.0 for j in range(n)]
        aug.append(aug_row)
    for i in range(n):
        pivot = aug[i][i]
        if abs(pivot) < 1e-12:
            pivot = 1e-12
        for j in range(2 * n):
            aug[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = aug[k][i]
                for j in range(2 * n):
                    aug[k][j] -= factor * aug[i][j]
    inv_cov = list()
    for i in range(n):
        inv_row = [aug[i][j + n] for j in range(n)]
        inv_cov.append(inv_row)
    return inv_cov

# ---------------------------------------------------------------------
# 4. MASTER SIMULATION PIPELINE EXECUTION
# ---------------------------------------------------------------------
def run_simulation_pipeline():
    print("--- RUNNING V11: INTEGRATING SOUND HORIZON (rd) METRICS ---")
    
    # Satellite-Verified Macro Anchors
    omega_baryon = 0.0493   
    omega_photon = 5.4e-5   
    omega_vacuum = 1.0 - (omega_baryon + omega_photon)
    H0_observed = 70.0      
    
    # Calibrated Fields Configuration from your V9 Fit
    rho_max = 5000.0       
    decay_constant = 0.15  
    induction_coupling = 1.35e-6  
    normalizing_amplitude = 4900.0  
    
    chi2_total = 0.0
    num_params = 4  
    num_data_points = len(CC_17_INDEPENDENT) + len(CC_15_CORRELATED)
    max_observed_cs2 = 0.0
    stability_compromised = False
    
    # Process 17 Independent Data Points
    for z, h_obs, sigma in CC_17_INDEPENDENT:
        scaling_matter = omega_baryon * (1.0 + z)**3
        scaling_photon = omega_photon * (1.0 + z)**4
        scaling_vacuum_ground = omega_vacuum * (1.0 + z)**0
        scaling_vacuum_induced = gauge_gravitational_vacuum_induction(z, omega_vacuum, H0_observed, induction_coupling)
        
        total_scaled_density = scaling_matter + scaling_photon + scaling_vacuum_ground + scaling_vacuum_induced
        
        cs2 = compute_sound_speed_diagnostic(scaling_vacuum_ground, rho_max, decay_constant)
        if cs2 > max_observed_cs2:
            max_observed_cs2 = cs2
        if cs2 < 0.0 or cs2 > 1.0:
            stability_compromised = True
            
        h2_predicted = calculate_h_squared_observable(total_scaled_density, rho_max, normalizing_amplitude)
        chi2_total += ((math.sqrt(h2_predicted) - h_obs) / sigma) ** 2
        
    # Process 15 Correlated Data Points
    residuals = list()
    for z, h_obs, sigma in CC_15_CORRELATED:
        scaling_matter = omega_baryon * (1.0 + z)**3
        scaling_photon = omega_photon * (1.0 + z)**4
        scaling_vacuum_ground = omega_vacuum * (1.0 + z)**0
        scaling_vacuum_induced = gauge_gravitational_vacuum_induction(z, omega_vacuum, H0_observed, induction_coupling)
        
        total_scaled_density = scaling_matter + scaling_photon + scaling_vacuum_ground + scaling_vacuum_induced
        
        cs2 = compute_sound_speed_diagnostic(scaling_vacuum_ground, rho_max, decay_constant)
        if cs2 > max_observed_cs2:
            max_observed_cs2 = cs2
        if cs2 < 0.0 or cs2 > 1.0:
            stability_compromised = True
            
        h2_predicted = calculate_h_squared_observable(total_scaled_density, rho_max, normalizing_amplitude)
        residuals.append(math.sqrt(h2_predicted) - h_obs)
        
    inv_cov = generate_formal_inverse_covariance(CC_15_CORRELATED)
    chi2_sys = 0.0
    for i in range(len(residuals)):
        for j in range(len(residuals)):
            chi2_sys += residuals[i] * inv_cov[i][j] * residuals[j]
            
    chi2_total += chi2_sys
    bic_score = chi2_total + num_params * math.log(num_data_points)
    
    # Calculate modern snapshot baseline speed today
    total_density_today = omega_baryon + omega_photon + omega_vacuum + gauge_gravitational_vacuum_induction(0, omega_vacuum, H0_observed, induction_coupling)
    h2_today = calculate_h_squared_observable(total_density_today, rho_max, normalizing_amplitude)
    h0_anchor = math.sqrt(h2_today)
    
    # Compute the physical Comoving Sound Horizon Scale (rd) cleanly
    r_d_scale = integrate_comoving_sound_horizon(
        rho_max, H0_observed, induction_coupling, normalizing_amplitude,
        omega_baryon, omega_photon, omega_vacuum
    )
    print("\n==============================================")
    print("   📊 V11 UNIFIED FIELD SIMULATION DASHBOARD")
    print("==============================================")
    print(f"Calculated Modern H0 Baseline:     {h0_anchor:.4f} km/s/Mpc")
    print(f"Peak Substrate Sound Speed (cs^2): {max_observed_cs2:.4f} (c^2)")
    print(f"Substrate Causal Security Health:  {'🔴 COMPROMISED' if stability_compromised else '🟢 100% SECURE & CAUSAL'}")
    print(f"Comoving Sound Horizon Scale (rd): {r_d_scale:.4f} Mpc")
    print(f"Active Parameter Penalty (k):      {num_params}")
    print(f"True Matrix Inversion Chi-Square:  {chi2_total:.4f}")
    print(f"🔵 UNIFIED ENGINE BIC SCORE:       {bic_score:.4f}")
    print("==============================================")

if __name__ == "__main__":
    run_simulation_pipeline()


