import matplotlib.pyplot as plt
from scipy.integrate import odeint

class SusInfRec:
    def __init__(self, N, I0, b, k, days):
        """
        S = S(t)	is the number of susceptible individuals,
        I = I(t)	is the number of infected individuals, and
        R = R(t)	is the number of recovered individuals.
        
        N is the total population 
        I0 is the initial number of infected individuals, 
        S0 - Everyone else is susceptible to infection initially
        
        b is contacts per day that are sufficient to spread the disease, and 
        k is our assumption that a fixed fraction k of the infected group will recover during any given day i.e., mean recovery rate, (in 1/days)
        """
        self.N = N
        self.I0 = I0
        self.b = b
        self.k = k
        self.S0 = N - I0 
        self.days = days

    
    @staticmethod
    def _compute(y, t, N, b, k):
        """
        The SIR model differential equations
        
        y - SIR vector
        t - Time in days
        N - Population
        b - Contacts per day
        k - Mean Recovery Rate
        
        The equations are referred from https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model 
        """
        S, I, R = y
        #print(t)
        '''The Susceptible Equation'''
        dSdt = -b[int(t)] * S * I / N
        
        '''The Infected Equation = -The Susceptible Equation  - The Recovered Equation'''
        dIdt = b[int(t)] * S * I / N - k * I
        
        '''The Recovered Equation'''
        dRdt = k * I
        return dSdt, dIdt, dRdt
    
    def run(self):
        """
        y0 - Initial conditions vector
        S0 - Initial Susceptible ( N - I0 )
        I0 - Initial Infected
        R0 - zero recovered at initial stage
        """ 
        y0 = self.S0, self.I0, 0
        
        """
        Integrating the SIR equations over the time grid, t
        """ 
        t = list(range(0, self.days))
        
        """
        odeint - Solve differential equations
        """
        result = odeint(self._compute, y0, t, args=(self.N, self.b, self.k))
        S, I, R = result.T
        
        """
        Returing values of S, I & R
        """
        return S, I, R