import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generating bins based on upper and lower thresholds
# Equally-sized

lower = 17
upper = 85
step = 8

def get_bins(lower, upper, step):
    """
    A function to get categorical equally-sized bins for a set of numbers.

    Parameters:
    -----------
        lower : int or float
            The minimum value of a set of numbers.
        upper : int or float
            The maximum value of a set of numbers.
        step : int
            The number that represents the separation of each bin.
    
    Returns:
    --------
    list
        Bins as a list of strings.         

    """
    num_range = [*range(lower, upper, step)]
    change = [*map(lambda x: x-1, num_range[1:])]
    num_range_2 = change + [upper]
    return [f'{i}-{n}' for i, n in zip(num_range, num_range_2)]

print(get_bins(lower, upper, step))


# A class to select categories based on a threshold and relative frequencies
class MainCategories:
    """
    A class for identifying and analyzing the most representative categories in a categorical variable
    based on a cumulative proportion threshold.

    Attributes:
    -----------
    array : pandas.Series or pandas.DataFrame
        The categorical variable (as a Series or single-column DataFrame).
    threshold : float
        A proportion value between 0 and 1 used to determine the main categories.
    prop_table : pandas.Series
        Relative frequencies of each category.
    prop_numbers : numpy.ndarray
        Array of relative frequencies used for cumulative calculations.
    limit : int or None
        Number of top categories that together make up less than or equal to the threshold.
    categories : list or None
        List of the top categories under the threshold.
    cum_freq : float
        The cumulative proportion of the top categories.

    Methods:
    --------
    plot_cats(subset=True):
        Plots the frequency of the main categories (or all categories if subset=False).
    """

    def __init__(self, array, threshold):
        """
        Initializes the MainCategories object and computes relevant properties.

        Parameters:
        -----------
        array : pandas.Series or pandas.DataFrame
            The categorical data to analyze.
        threshold : float
            A value between 0 and 1 representing the cumulative proportion threshold.
        """
        if not isinstance(array, (pd.Series, pd.DataFrame)):
            raise TypeError('The array must be a pandas Series or a pandas DataFrame object.')

        if not (0 <= threshold <= 1):
            raise ValueError('The threshold must be a proportion between 0 and 1.')

        if isinstance(array, pd.DataFrame) and array.shape[1] != 1:
            raise ValueError('DataFrame must contain only one column.')

        self.array = array
        self.threshold = threshold
        self.prop_table = array.value_counts(normalize=True).round(4)
        self.prop_numbers = self.prop_table.values
        self.limit = self._get_limit()
        self.categories = self._get_top()
        self.cum_freq = self._cum_freq()

    def _get_limit(self):
        """
        Determines how many top categories fit within the defined threshold.

        Returns:
        --------
        int or None
            Number of categories or None if threshold is 0.
        """
        if self.threshold == 0:
            return None
        return sum(np.cumsum(self.prop_numbers) <= self.threshold)

    def _get_top(self):
        """
        Retrieves the most frequent categories under the threshold.

        Returns:
        --------
        list or None
            Top categories or None if threshold is 0.
        """
        if self.limit is None or self.limit == 0:
            return None
        return self.prop_table[:self.limit].index.tolist()

    def _cum_freq(self):
        """
        Calculates the cumulative proportion of the selected top categories.

        Returns:
        --------
        float
            The cumulative relative frequency.
        """
        if self.limit is None or self.limit == 0:
            return 0
        return np.cumsum(self.prop_numbers)[self.limit - 1]

    def plot_cats(self, subset=True):
        """
        Plots a bar chart of category frequencies.

        Parameters:
        -----------
        subset : bool, default=True
            If True, plots only the top categories under the threshold.
            If False, plots all categories.
        """
        if self.categories is None:
            print("No categories available for plotting.")
            return
        if subset:
            self.prop_table[:self.limit].plot(kind='bar', title=f'Top {self.limit} most frequent', figsize=(10, 4))
        else:
            self.prop_table.plot(kind='bar', title='Category frequency', figsize=(10, 4))
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
