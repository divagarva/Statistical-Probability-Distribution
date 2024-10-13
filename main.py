import numpy as np
import matplotlib.pyplot as plt

# Function to generate different probability distributions
def generate_distribution(distribution_type, size=1000, **kwargs):
    """
    Generates random samples for the specified probability distribution.

    Parameters:
    distribution_type (str): Type of distribution ('normal', 'binomial', 'poisson')
    size (int): Number of random samples
    **kwargs: Additional parameters for specific distributions

    Returns:
    np.ndarray: Random samples from the chosen distribution
    """
    if distribution_type == 'normal':
        return np.random.normal(loc=kwargs.get('mean', 0), scale=kwargs.get('std_dev', 1), size=size)
    elif distribution_type == 'binomial':
        return np.random.binomial(n=kwargs.get('n', 10), p=kwargs.get('p', 0.5), size=size)
    elif distribution_type == 'poisson':
        return np.random.poisson(lam=kwargs.get('lam', 3), size=size)
    else:
        raise ValueError("Unsupported distribution type. Choose from 'normal', 'binomial', 'poisson'.")

# Function to visualize a distribution
def plot_distribution(data, distribution_type):
    """
    Plots the histogram of a given data distribution.

    Parameters:
    data (np.ndarray): Data samples to plot
    distribution_type (str): Name of the distribution for labeling
    """
    plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title(f'{distribution_type.capitalize()} Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Main function to run the project
def main():
    print("Generating and visualizing probability distributions")

    # Generate and plot Normal Distribution
    normal_data = generate_distribution('normal', size=1000, mean=0, std_dev=1)
    plot_distribution(normal_data, 'normal')

    # Generate and plot Binomial Distribution
    binomial_data = generate_distribution('binomial', size=1000, n=10, p=0.5)
    plot_distribution(binomial_data, 'binomial')

    # Generate and plot Poisson Distribution
    poisson_data = generate_distribution('poisson', size=1000, lam=3)
    plot_distribution(poisson_data, 'poisson')

if __name__ == "__main__":
    main()
