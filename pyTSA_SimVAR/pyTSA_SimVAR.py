from statsmodels.tsa.vector_ar.var_model import VARProcess
import numpy as np
import matplotlib.pyplot as plt
coefs = np.array([[[0.5, 0.2, 0.0], [0.4, 0.3, 0.5], [0.5, 0.2, 0.3]], 
[[0.0, 0.01, 0.0], [-0.19, -0.2, 0.0], [-0.31, 0.01, -0.1]]])
sigma_u = np.array([[0.28, 0.03, 0.07], [0.03, 0.3, 0.14], 
[0.07, 0.14, 0.4]])
coefs_exog = np.array([0, 0, 0])
# the constant vector is zero
varProcess = VARProcess(coefs,  coefs_exog,  sigma_u)
varSimul = varProcess.simulate_var(steps = 300,  seed = 1237)
# Draw a sample of size 300 from the VAR(2) process
varProcess.plotsim(steps = 300,  seed = 1237)
plt.savefig('pyTSA_SimVAR_fig7-8.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
# Plot the sample
varProcess.plot_acorr(linewidth = 2,  nlags = 10)
plt.savefig('pyTSA_SimVAR_fig7-9.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
# Plot theoretical correlation functions

