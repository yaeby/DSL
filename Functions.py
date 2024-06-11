import numpy as np
import matplotlib.pyplot as plt
import json
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def rotate_points(points, angle):
    angle_rad = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad), np.cos(angle_rad)]
    ])

    rotated_points = []
    for sublist in points:
        sublist_array = np.array(sublist)
        rotated_sublist = np.dot(sublist_array, rotation_matrix)
        rotated_points.append(rotated_sublist.tolist())

    return rotated_points
def functions(data):
    # Set the DPI (dots per inch) for your figure
    dpi = 100
    figure_width = 351 / dpi  # Image width in inches
    figure_height = 512 / dpi  # Image height in inches

    # Set the figure size to match the image size
    plt.figure(figsize=(figure_width, figure_height), dpi=dpi)

    # Define the maximum degree to test for polynomials
    max_degree = 10
    degrees = range(1, max_degree + 1)

    # List to store the best degree for each edge
    best_degrees = []

    # Dictionary to store polynomial coefficients
    polynomial_functions = {}

    # Process each sublist (edge)
    for index, sublist in enumerate(data):
        edge = np.array(sublist)

        # Check if there are enough points for cross-validation
        if len(edge) < 5:
            continue

        x = edge[:, 0].reshape(-1, 1)  # Reshape for sklearn
        y = edge[:, 1]

        best_degree = None
        best_score = float('inf')

        # Iterate over degrees to find the best degree for polynomial fitting
        for degree in degrees:
            # Create a pipeline that creates polynomial features and fits a linear regressor
            model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

            # Perform k-fold cross-validation
            try:
                scores = cross_val_score(model, x, y, scoring='neg_mean_squared_error', cv=5)
            except ValueError:
                # Not enough samples for cross-validation
                continue

            score = -scores.mean()  # Negate to get positive MSE

            # Update the best degree if this score is better
            if score < best_score:
                best_score = score
                best_degree = degree

        # Skip if we couldn't compute a best degree
        if best_degree is None:
            continue

        best_degrees.append(best_degree)

        # Fit the model with the best degree found
        model = make_pipeline(PolynomialFeatures(best_degree), LinearRegression())
        model.fit(x, y)

        # Save the coefficients of the polynomial
        # The coefficients of the last step (LinearRegression) are the ones we want
        coefficients = model.steps[-1][1].coef_.tolist()
        polynomial_functions[f'function{index + 1}'] = coefficients

        # Generate points for plotting the smooth curve
        x_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
        y_range = model.predict(x_range)

        # Plot the original points and the fitted curve
        plt.plot(x_range, y_range, color='black')  # Fitted curve

    # Adjust the y-axis limits to fit all the data
    all_y = [point[1] for sublist in data for point in sublist]
    plt.ylim([min(all_y) - 10, max(all_y) + 10])

    # Show combined plot for all edges
    plt.title("Polynomial Fit for Edges")
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.show()

    # Save polynomial functions to a JSON file
    with open('functions.json', 'w') as file:
        json.dump(polynomial_functions, file, indent=4)