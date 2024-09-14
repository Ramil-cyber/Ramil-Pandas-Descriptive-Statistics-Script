import pandas as pd
import matplotlib.pyplot as plt


def read_csv(file_name):
    """
    Read file name and return pandas dataframe

    file_name
    """

    dataframe = pd.read_csv(file_name)

    return dataframe


def get_descriptive_stats(dataframe):
    """
    Return descriptive statistics from dataframe
    """

    return dataframe.describe()


def get_histogram(dataframe, col):
    """
    Return histogram from given column based on given dataframe
    """
    plt.hist(dataframe[col], bins=5, edgecolor="black")
    plt.title(f"Histogram of {col}")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()
    return True


def get_line_graph(dataframe, x_col, y_col):
    """
    Return line graph from given x and y columns based on given dataframe
    """
    plt.close()
    dataframe.plot(kind="line", x=x_col, y=y_col, legend=True)

    plt.title("Line Graph of Value over Time")
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    # Show plot
    plt.show()
    return True
