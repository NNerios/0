import numpy as np

class ZeroCosmologicalEngine:
    def __init__(self, rho_max=1.0e5):
        """
        Initializes the zÆro (Æ "0") Thermodynamic Cosmological Engine v3.4.0.
        All inner calculations operate in pure dimensionless frequency/density space.
        """
        # 🪐 Satellite-Verified Observables (Dimensionless Reference Baselines at z=0)
        self.Omega_b = 0.0493     # Baryon Vector fraction (Planck 2018)
        self.Omega_gamma = 5.4e-5 # Photon Vector fraction (COBE/FIRAS)
        self.Omega_fluid_0 = 1.0 - (self.Omega_b + self.Omega_gamma)
        
        # 🧱 Core Microscopic Substrate Bounds
        self.rho_max = rho_max    # Maximum physical compaction threshold 
        self.c2 = 1.0             # Normalized signal speed constant
        
        # 🔥 Dynamic Thermodynamic Coupling Variables
        self.alpha_furnace = 0.1152   # Galactic Furnace outgassing/thrust momentum 
        self.chi_web = 0.0021         # Cosmic Web channel drag 
        self.chi_insulation = 0.0034  # Vacuum substrate thermal insulation profile
        self.psi_smbh = 0.0012        # Escaping Hawking steam loss parameter
        
    def calculate_ae_spring(self, rho_total):
        """
        Calculates the Dimensionless Suppression Fraction Æ(ρ) evaluated to the 4th power.
        Acts as the quantum bulk modulus of the vacuum substrate.
        """
        if rho_total >= self.rho_max:
            return 1.0
        ae_fraction = (rho_total / self.rho_max) ** 4
        return min(max(ae_fraction, 0.0), 1.0)

    def compute_normalized_densities(self, redshift):
        """
        Computes interactive cosmic density components.
        Replaces geometric dilution with continuous thermodynamic feedback work loops.
        """
        # Matter modified by Galactic Furnace thrust momentum
        rho_b = self.Omega_b * (1.0 + redshift) ** (3.0 - self.alpha_furnace)
        
        # Radiation modified by Cosmic Web filamentary drag channel routing
        rho_gamma = self.Omega_gamma * (1.0 + redshift) ** (4.0 - self.chi_web)
        
        # Background fluid substrate modified by cumulative insulation and escaping Hawking steam
        exponent = self.chi_insulation + self.psi_smbh
        rho_fluid = self.Omega_fluid_0 * (1.0 + redshift) ** exponent
        
        return rho_b, rho_gamma, rho_fluid

    def compute_hubble_squared(self, redshift):
        """
        Computes the Hubble expansion rate squared in normalized frequency space.
        Standstill Symmetry is maintained: H^2 = 0 if and only if ae_spring = 1.0.
        """
        rho_b, rho_gamma, rho_fluid = self.compute_normalized_densities(redshift)
        rho_total = rho_b + rho_gamma + rho_fluid
        
        ae_spring = self.calculate_ae_spring(rho_total)
        h2_classical = rho_total
        h2_modified = h2_classical * (1.0 - ae_spring)
        
        return max(h2_modified, 0.0)
