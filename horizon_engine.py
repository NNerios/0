import numpy as np

# =====================================================================
# THE BUBBLED VACUUM FLUID ENGINE (v3.6.0 HYDRODYNAMIC)
# =====================================================================
class ZeroCosmologicalEngine:
    def __init__(self, rho_max=1.0e5):
        self.Omega_b = 0.0493     
        self.Omega_gamma = 5.4e-5 
        self.Omega_fluid_0 = 1.0 - (self.Omega_b + self.Omega_gamma)
        self.rho_max = rho_max    
        
        # Emergent Root Parameters for the State-Transition Loop
        self.alpha_0 = 0.0824     
        self.chi_0 = 0.0015       
        self.psi_0 = 0.0008       
        
    def calculate_ae_spring(self, rho_total):
        if rho_total >= self.rho_max:
            return 1.0
        return min(max((rho_total / self.rho_max) ** 4, 0.0), 1.0)

    def compute_emergent_conditions(self, redshift):
        xi_emergent = np.log(1.0 + redshift * (self.Omega_fluid_0 / self.rho_max))
        alpha_dynamic = self.alpha_0 * (1.0 + xi_emergent)
        chi_dynamic = self.chi_0 * (1.0 + xi_emergent)
        psi_dynamic = self.psi_0 * (1.0 + xi_emergent)
        return alpha_dynamic, chi_dynamic, psi_dynamic

    def compute_normalized_densities(self, redshift):
        alpha, chi, psi = self.compute_emergent_conditions(redshift)
        rho_b = self.Omega_b * (1.0 + redshift) ** (3.0 - alpha)
        rho_gamma = self.Omega_gamma * (1.0 + redshift) ** 4.0
        
        exponent = chi + psi
        rho_fluid = self.Omega_fluid_0 * (1.0 + redshift) ** exponent
        return rho_b, rho_gamma, rho_fluid

    def compute_hubble_squared(self, redshift):
        rho_b, rho_gamma, rho_fluid = self.compute_normalized_densities(redshift)
        rho_total = rho_b + rho_gamma + rho_fluid
        ae_spring = self.calculate_ae_spring(rho_total)
        return max(rho_total * (1.0 - ae_spring), 0.0)


class ZeroHorizonEngine:
    def __init__(self, rho_max=1.0e5):
        self.rho_max = rho_max
        self.c2 = 1.0
        self.gamma_steam_root = 0.0025   
        self.eta_base_seal = 0.985  
        
    def calculate_bubble_physics(self, core_mass, rho_local):
        """
        Models the Event Horizon strictly as a compressed vacuum bubble skin.
        Calculates surface tension pressure and net escaping steam.
        """
        # Surface tension scales non-linearly with the compression ratio
        compression_ratio = rho_local / self.rho_max
        sigma_bubble_tension = (compression_ratio) ** 4
        
        # The gravitational seal degrades if internal bubble pressure wins the battle
        gravitational_seal = self.eta_base_seal * (1.0 - np.exp(-core_mass)) * (1.0 - sigma_bubble_tension * 0.01)
        escape_fraction = 1.0 - max(min(gravitational_seal, 1.0), 0.0)
        
        # Boundary sound speed inside the bubble wall skin
        cs_squared = self.c2 * (1.0 - sigma_bubble_tension)
        return sigma_bubble_tension, escape_fraction, cs_squared


if __name__ == "__main__":
    core = ZeroCosmologicalEngine()
    horizon = ZeroHorizonEngine()
    
    print("=== zÆro Framework v3.6.0 Bubble Horizon Validation ===")
    
    # Analyze a compressed vacuum bubble near its critical compaction threshold
    test_mass = 4.5
    test_rho = 0.92 * horizon.rho_max
    
    tension, escape, cs2 = horizon.calculate_bubble_physics(core_mass=test_mass, rho_local=test_rho)
    
    print(f"\n--- Compressed Vacuum Bubble Analysis (92% Compaction) ---")
    print(f" * Horizon Surface Tension Skin Metric (Σ_bubble): {tension:.4f}")
    print(f" * Escaping Vacuum Steam Leakage Fraction:        {escape * 100:.3f}%")
    print(f" * Substrate Sound Speed Inside Bubble Wall (c_s²): {cs2:.4f}")
    print(f" * Structural Causality Safety Baseline:           {0.0 <= cs2 <= 1.0}")
