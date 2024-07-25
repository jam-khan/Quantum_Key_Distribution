import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def plot_multiple_curves(k_values, pairs_array):
    """
    Plots multiple sets of (x, y) pairs using Matplotlib with specific axis labels and ranges.
    Connects the points with smooth curves and labels each curve with a different color corresponding to k values.
    
    Parameters:
    k_values (list): A list of k values.
    pairs_array (list of lists of tuples): A list where each element is a list of (x, y) pairs corresponding to a k value.
    """
    # Define the Y-axis range
    y_min, y_max = -0.1, np.log2(3)
    
    # Define the X-axis range
    x_min, x_max = 4.0, 5.0
    
    # Create a plot
    plt.figure(figsize=(10, 6))
    
    # Define a color map
    colors = plt.cm.viridis(np.linspace(0, 1, len(k_values)))
    
    for i, pairs in enumerate(pairs_array):
        # Unzip the pairs into two separate lists for x and y coordinates
        x_values, y_values = zip(*pairs)
        
        # Create a smooth curve using B-spline interpolation
        x_new = np.linspace(min(x_values), max(x_values), 300)
        spl = make_interp_spline(x_values, y_values, k=3)
        y_smooth = spl(x_new)
        
        # Plot the smooth curve
        plt.plot(x_new, y_smooth, color=colors[i], linestyle='-', label=f'k = {k_values[i]}')
        
        # Scatter plot
        # plt.scatter(x_values, y_values, color=colors[i], marker='o')
    
    # Add titles and labels
    plt.title('Randomness Certification')
    plt.xlabel('Bell Value')
    plt.ylabel('Randomness [bits]')
    
    # Set axis ranges
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    
    # Add custom Y-axis tick labels
    y_ticks = np.linspace(0, y_max, num=7)
    y_tick_labels = [f'{tick:.2f}' for tick in y_ticks[:-1]] + ['log2(3)']
    plt.yticks(y_ticks, y_tick_labels)
    
    # Show legend
    plt.legend()
    
    # Show the plot
    plt.grid(True)
    plt.show()

# Example usage
k_values = [2, 1]
pairs_array = [
        [(4.01, 0),
        (4.062105263157894, 0),
        (4.114210526315789, 0),
        (4.166315789473685, 0),
        (4.218421052631579, 0.003443015708558455),
        (4.270526315789474, 0.039581826257855356),
        (4.322631578947369, 0.08099517715404568),
        (4.374736842105263, 0.12519939545113454),
        (4.426842105263158, 0.17142423789126401),
        (4.478947368421053, 0.21938989315328764),
        (4.531052631578947, 0.2693066621839655),
        (4.583157894736842, 0.32131522523476264),
        (4.6352631578947365, 0.376231084321439),
        (4.687368421052631, 0.4348240679660648),
        (4.739473684210527, 0.4974702331894018),
        (4.791578947368421, 0.5661657594378091),
        (4.843684210526316, 0.6493347479458591),
        (4.895789473684211, 0.7695199322910391),
        (4.947894736842105, 0.939198227888254),
        (5.0, 1.5510629936461002)],
        [(4.01, 0),
    (4.035384615384616, 0),
    (4.060769230769231, 0),
    (4.086153846153846, 0),
    (4.111538461538461, 0),
    (4.136923076923077, 0),
    (4.162307692307692, 0),
    (4.187692307692307, 0),
    (4.213076923076923, 0),
    (4.2384615384615385, 0),
    (4.263846153846154, 0),
    (4.28923076923077, 0),
    (4.314615384615385, 0),
    (4.34, 0),
    (4.365384615384615, 0),
    (4.390769230769231, 0),
    (4.416153846153846, 0),
    (4.441538461538461, 0),
    (4.466923076923077, 0),
    (4.492307692307692, 0),
    (4.5176923076923075, 0),
    (4.5430769230769235, 6.326093072860611e-5),
    (4.568461538461539, 0.020029387478106092),
    (4.593846153846154, 0.0618552578013686),
    (4.619230769230769, 0.11246010047884243),
    (4.644615384615385, 0.15662057443141078),
    (4.67, 0.20617924048487737),
    (4.695384615384615, 0.2536784312751975),
    (4.720769230769231, 0.2938317581167907),
    (4.746153846153846, 0.34534458877638624),
    (4.771538461538461, 0.41025692770864153),
    (4.796923076923077, 0.4545810576770136),
    (4.822307692307692, 0.5127781957992519),
    (4.8476923076923075, 0.5798584058703115),
    (4.873076923076923, 0.6378367399734903),
    (4.898461538461539, 0.705757303186838),
    (4.923846153846154, 0.792865551825233),
    (4.949230769230769, 0.8877768129324429),
    (4.974615384615385, 1.031023901773218),
    (5.0, 1.54894726310632)]
]
plot_multiple_curves(k_values, pairs_array)

# Example usage
# pairs = [(4.1, 0.5), (4.2, 0.7), (4.3, 0.9), (4.4, 1.1), (4.5, 1.3), (4.6, 1.5)]
# plot_xy_pairs_with_details(pairs)

# Example usage
# pairs = [(4.01, 0),
#         (4.062105263157894, 0),
#         (4.114210526315789, 0),
#         (4.166315789473685, 0),
#         (4.218421052631579, 0.003443015708558455),
#         (4.270526315789474, 0.039581826257855356),
#         (4.322631578947369, 0.08099517715404568),
#         (4.374736842105263, 0.12519939545113454),
#         (4.426842105263158, 0.17142423789126401),
#         (4.478947368421053, 0.21938989315328764),
#         (4.531052631578947, 0.2693066621839655),
#         (4.583157894736842, 0.32131522523476264),
#         (4.6352631578947365, 0.376231084321439),
#         (4.687368421052631, 0.4348240679660648),
#         (4.739473684210527, 0.4974702331894018),
#         (4.791578947368421, 0.5661657594378091),
#         (4.843684210526316, 0.6493347479458591),
#         (4.895789473684211, 0.7695199322910391),
#         (4.947894736842105, 0.939198227888254),
#         (5.0, 1.5510629936461002)]


# plot_xy_pairs_with_details(pairs)