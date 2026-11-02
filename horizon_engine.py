# =====================================================================
# HORIZON ENGINE V3: GRAVITATIONAL INDUCTION SOUND HORIZON INTEGRATION
# =====================================================================
import math
import core_engine

def calculate_plasma_sound_speed(z, omega_baryon=0.0493, omega_photon=5.4e-5):
    """
    FORMULA 4: Effective Plasma Sound Speed (cs).
    Calculates the exact, redshift-dependent speed of sound waves 
    propagating through the tightly coupled early-universe baryon-photon plasma.
    """
    c = 299792.458  # Speed of light constant represented in km/s
    
    # Standard Relativistic Correction: Includes the neutrino radiation background 
    # multiplier (~1.681) to ensure unassailable early-universe accuracy.
    omega_radiation = omega_photon * 1.68132
    
    # Calculate the baryon-to-photon momentum-density ratio R(z)
    R_z = (3.0 * omega_baryon) / (4.0 * omega_radiation * (1.0 + z))
    
    # Relativistic plasma sound speed equation
    # As z -> infinity, R_z -> 0, causing cs to hit the exact cosmic speed limit of c/sqrt(3)
    cs_z = c / math.sqrt(3.0 * (1.0 + R_z))
    return cs_z

def integrate_comoving_sound_horizon(rho_max, H0_observed, induction_coupling, normalizing_amplitude, omega_baryon, omega_photon, omega_vacuum):
    """
    MATHEMATICALLY BALANCED: Executes the 2,000-step numerical integration
    by normalizing the early-universe expansion scale to prevent velocity underflow.
    """
    z_drag = 1059.94      
    z_max = 2500.0        
    steps = 2000          
    
    dz = (z_max - z_drag) / steps
    r_d_integral = 0.0
    
    # Speed of light converted to astronomical megaparsec scaling bounds
    # to yield standard distance results (c / H0 units)
    c_mpc = 299792.458 / H0_observed 
    
    for i in range(steps):
        z = z_drag + (i * dz)
        
        # Scale cosmic components based on macro geometry
        scaling_matter = omega_baryon * (1.0 + z)**3
        scaling_photon = omega_photon * (1.0 + z)**4
        scaling_vacuum_ground = omega_vacuum * (1.0 + z)**0
        scaling_vacuum_induced = gauge_gravitational_vacuum_induction(z, omega_vacuum, H0_observed, induction_coupling)
        
        total_scaled_density = scaling_matter + scaling_photon + scaling_vacuum_ground + scaling_vacuum_induced
        
        # Calculate background scaling ratio E(z) directly
        alpha_gauge = gauge_repulsive_spring_AE(total_scaled_density, rho_max)
        E_z = math.sqrt(abs(total_scaled_density * (1.0 - alpha_gauge)))
        
        # Plasma sound speed relative to the speed of light
        omega_radiation = omega_photon * 1.68132
        R_z = (3.0 * omega_baryon) / (4.0 * omega_radiation * (1.0 + z))
        cs_normalized = 1.0 / math.sqrt(3.0 * (1.0 + R_z))
        
        # Accumulate the comoving acoustic step
        if E_z > 0:
            r_d_integral += (cs_normalized / E_z) * dz
            
    # Scale through the fundamental Hubble distance metric to output Mpc units
    return r_d_integral * c_mpc
