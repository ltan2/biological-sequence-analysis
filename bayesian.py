# conditional probability
# P(X) = n
# join probability
# P(X, Y) = P(X|Y)P(Y)
# marginal probability
# sum is all possibilities of event B
# P(A)= ∑ P(A,B) - (for discrete variable) 
# P(A)= ∫ P(A,B) dB - (continuous variable)

# posterior probability calculation using bayes theorem
# Posterior probability is the possibility of X given Y
# P(X|Y) = (P(Y|X)P(X))/P(Y) - comparing model

# bayes theorem for parameter estimation
# prior knowledge is known
# P(θ∣D) = (P(D∣θ)P(θ))/P(D)
# P(θ∣D): The updated belief about the parameters after seeing the data (posterior).
# 𝑃(𝐷∣𝜃): How well the data fits a given parameter value (likelihood).
# 𝑃(𝜃): What we believed about the parameters before seeing the data (prior).
# 𝑃(𝐷): The total probability of the data (normalizes everything).

# Maximum a Posteriori (MAP): Choose the parameter value with the highest posterior probability 
# (the most likely after combining prior and data).

# Mean of the Posterior: Use the average of all possible parameter values, weighted by how 
# likely they are (posterior).

import numpy as np

def bayes_theorem(prior, likelihood, evidence):
    """
    Calculate Bayes' theorem.

    Parameters:
        prior (float): P(A), prior probability of hypothesis.
        likelihood (float): P(B|A), likelihood of data given hypothesis.
        evidence (float): P(B), probability of data under all hypotheses.

    Returns:
        float: Posterior probability P(A|B).
    """
    posterior = (likelihood * prior) / evidence
    return posterior

def bayesian_parameter_estimation(data, prior_mean, prior_var, likelihood_var):
    """
    Perform Bayesian parameter estimation.

    Parameters:
        data (list or np.array): Observed data points.
        prior_mean (float): Mean of the prior distribution.
        prior_var (float): Variance of the prior distribution.
        likelihood_var (float): Variance of the likelihood (data model).

    Returns:
        tuple: Posterior mean and variance.
    """
    # Number of data points
    n = len(data)
    
    # Sample mean from the data
    data_mean = np.mean(data)
    
    # Calculate posterior variance
    posterior_var = 1 / ((1 / prior_var) + (n / likelihood_var))
    
    # Calculate posterior mean
    posterior_mean = posterior_var * ((prior_mean / prior_var) + (n * data_mean / likelihood_var))
    
    return posterior_mean, posterior_var

# Example usage
if __name__ == "__main__":
    # Bayes' theorem example
    prior = 0.3  # P(A)
    likelihood = 0.8  # P(B|A)
    evidence = 0.5  # P(B)
    posterior = bayes_theorem(prior, likelihood, evidence)
    print(f"Posterior Probability (P(A|B)): {posterior:.4f}")

    # Bayesian parameter estimation example
    data = [5.0, 5.2, 4.8, 5.1, 4.9]  # Observed data points
    prior_mean = 5.0  # Prior mean
    prior_var = 0.1  # Prior variance
    likelihood_var = 0.2  # Variance of the likelihood (data model)

    posterior_mean, posterior_var = bayesian_parameter_estimation(data, prior_mean, prior_var, likelihood_var)
    print(f"Posterior Mean: {posterior_mean:.4f}, Posterior Variance: {posterior_var:.4f}")




