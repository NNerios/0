import numpy as np

# =====================================================================
# THE UNIFIED THERMODYNAMIC BUBBLED FLUID ENGINE (v3.6.0 COMPLETE)
# =====================================================================
# 🪐 Zero SI Constraints. Zero Curvature Metrics. Zero Unverified Fields.
# 🌌 Implements Emergent State Transitions & Bubbled Vacuum Boundaries.
# =====================================================================

class ZeroCosmologicalEngine:
    def __init__(self, rho_max=1.0e5):
        """
        Initializes the zÆro (Æ "0") Thermodynamic Cosmological Engine v3.6.0.
        All calculations execute natively in pure dimensionless frequency/density space.
        """
        # Satellite-Verified Reference Observables (Dimensionless Baselines at z=0)
        self.Omega_b = 0.0493     # Baryon Vector fraction (Planck 2018)
        self.Omega_gamma = 5.4e-5 # Photon Vector fraction (COBE/FIRAS)
        self.Omega_fluid_0 = 1.0 - (self.Omega_b + self.Omega_gamma)
        
        # Core Microscopic Substrate Bounds
        self.rho_max = rho_max    # Maximum physical compaction threshold before bounce
        self.c2 = 1.0             # Normalized signal transmission speed constant
        
        # Emergent Root State Coefficients
        self.alpha_0 = 0.0824     # Root Galactic Furnace momentum coefficient
        self.chi_0 = 0.0015       # Root Substrate Thermal Insulation coefficient
        self.psi_0 = 0.0008       # Root Escaping Hawking Steam coefficient
        
    def calculate_ae_spring(self, rho_total):
        """Calculates the dimensionless micro-suppression fraction (Bulk Modulus)."""
        if rho_total >= self.rho_max:
            return 1.0
        return min(max((rho_total / self.rho_max) ** 4, 0.0), 1.0)

    def compute_emergent_conditions(self, redshift):
        """
        The Invisible Equation Layer.
        Generates dynamic parameter scaling only as local conditions are met by the substrate.
        """
        xi_emergent = np.log(1.0 + redshift * (self.Omega_fluid_0 / self.rho_max))
        
        alpha_dynamic = self.alpha_0 * (1.0 + xi_emergent)
        chi_dynamic = self.chi_0 * (1.0 + xi_emergent)
        psi_dynamic = self.psi_0 * (1.0 + xi_emergent)
        
        return alpha_dynamic, chi_dynamic, psi_dynamic

    def compute_normalized_densities(self, redshift):
        """Computes active density scaling driven by thermodynamic work exchange loop."""
        alpha, chi, psi = self.compute_emergent_conditions(redshift)
        
        rho_b = self.Omega_b * (1.0 + redshift) ** (3.0 - alpha)
        rho_gamma = self.Omega_gamma * (1.0 + redshift) ** 4.0
        
        exponent = chi + psi
        rho_fluid = self.Omega_fluid_0 * (1.0 + redshift) ** exponent
        
        return rho_b, rho_gamma, rho_fluid

    def compute_hubble_squared(self, redshift):
        """Computes the Hubble expansion rate squared in normalized frequency space."""
        rho_b, rho_gamma, rho_fluid = self.compute_normalized_densities(redshift)
        rho_total = rho_b + rho_gamma + rho_fluid
        
        ae_spring = self.calculate_ae_spring(rho_total)
        h2_classical = rho_total
        h2_modified = h2_classical * (1.0 - ae_spring)
        
        return max(h2_modified, 0.0)


class ZeroHorizonEngine:
    def __init__(self, rho_max=1.0e5):
        self.rho_max = rho_max
        self.c2 = 1.0
        self.gamma_steam_root = 0.0025   
        self.eta_base_seal = 0.985  
        
    def calculate_bubble_physics(self, core_mass, rho_local):
        """
        Models the Event Horizon strictly as a compressed vacuum bubble wall.
        Calculates surface tension pressure gradients and net escaping steam.
        """
        compression_ratio = rho_local / self.rho_max
        sigma_bubble_tension = (compression_ratio) ** 4
        
        # Gravitational containment seal degrades as internal bubble pressure rises
        gravitational_seal = self.eta_base_seal * (1.0 - np.exp(-core_mass)) * (1.0 - sigma_bubble_tension * 0.01)
        escape_fraction = 1.0 - max(min(gravitational_seal, 1.0), 0.0)
        
        # Local signal sound speed inside the bubble wall skin
        cs_squared = self.c2 * (1.0 - sigma_bubble_tension)
        return sigma_bubble_tension, escape_fraction, cs_squared


class CERCPipeline:
    def __init__(self, core_engine, horizon_engine):
        self.engine = core_engine
        self.horizon = horizon_engine
        self.H0_calibration = 70.0  
        
        # 📊 32 Hard Observational Cosmic Chronometer Points (z, H_observed, sigma_H)
        self.cc_data = np.array([
            [0.07, 69.0, 19.6], [0.09, 69.0, 12.0], [0.12, 68.6, 26.2], [0.17, 83.0, 8.0],
            [0.179, 75.0, 4.0], [0.199, 75.0, 5.0], [0.20, 72.9, 29.6], [0.27, 77.0, 14.0],
            [0.28, 88.8, 36.6], [0.35, 82.7, 8.4], [0.352, 83.0, 14.0], [0.38, 83.0, 13.5],
            [0.3802, 89.0, 4.0], [0.40, 95.0, 17.0], [0.4004, 77.0, 10.2], [0.424, 87.1, 11.2],
            [0.44, 92.8, 12.9], [0.47, 89.0, 34.0], [0.4783, 80.9, 9.0], [0.48, 97.0, 62.0],
            [0.593, 104.0, 13.0], [0.68, 92.0, 8.0], [0.781, 105.0, 12.0], [0.875, 125.0, 17.0],
            [0.88, 90.0, 40.0], [0.90, 117.0, 23.0], [1.037, 130.0, 20.0], [1.30, 168.0, 17.0],
            [1.363, 160.0, 33.6], [1.43, 177.0, 18.0], [1.53, 140.0, 14.0], [1.75, 202.0, 40.0]
        ])

    def execute_statistical_validation(self):
        z_obs = self.cc_data[:, 0]
        H_obs = self.cc_data[:, 1]
        sigma_H = self.cc_data[:, 2]
        
        chi_squared = 0.0
        for i in range(len(z_obs)):
            h2_dim = self.engine.compute_hubble_squared(z_obs[i])
            h_pred = np.sqrt(h2_dim) * self.H0_calibration
            chi_squared += ((H_obs[i] - h_pred) / sigma_H[i]) ** 2
            
        reduced_chi_squared = chi_squared / len(z_obs)
        return chi_squared, reduced_chi_squared

if __name__ == "__main__":
    core = ZeroCosmologicalEngine()
    horizon = ZeroHorizonEngine()
    pipeline = CERCPipeline(core, horizon)
    
    print("=== zÆro Fluid Framework v3.6.0 Synchronized Verification ===")
    print(f"Baryon Vector Fraction (Ωb): {core.Omega_b}")
    print(f"Vacuum Initial Condition (Ω_fluid_0): {core.Omega_fluid_0:.4f}")
    
    total_chi2, red_chi2 = pipeline.execute_statistical_validation()
    print(f"\n--- Integrated Pipeline Real-Data Alignment ---")
    print(f"Total Framework Chi-Squared (𝜒²): {total_chi2:.4f}")
    print(f"Reduced Performance Score (𝜒²/dof): {red_chi2:.4f}")
    
    tension, escape, cs2 = horizon.calculate_bubble_physics(core_mass=4.5, rho_local=0.92*horizon.rho_max)
    print(f"\n--- Horizon Bubble Wall Analysis (92% Compaction) ---")
    print(f" * Horizon Surface Tension Skin (Σ_bubble): {tension:.4f}")
    print(f" * Escaping Vacuum Steam Leak Fraction:     {escape * 100:.3f}%")
    print(f" * Substrate Sound Speed Inside Wall (c_s²): {cs2:.4f}")
