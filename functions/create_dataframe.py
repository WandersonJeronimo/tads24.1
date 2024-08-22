import pandas as pd
import numpy as np

def create_dataframe_example(
        size: int = 20,
        seed: int = 42
) -> pd.DataFrame:
    """
    Creates a sample DataFrame with fictional student data.

    This function generates a DataFrame with a specified number of rows and four columns:
    'Name', 'Score_1', 'Score_2', and 'Shift'. The names are taken from a predefined list,
    while the scores are randomly generated in the range of 50 to 100, and the shifts are randomly 
    selected from 'Morning', 'Afternoon', and 'Evening'.

    Parameters:
    ----------
    size : int, optional
        The number of rows (students) in the DataFrame. Default is 20.
    seed : int, optional
        The seed for the random number generator to ensure reproducibility of the data. Default is 42.

    Returns:
    -------
    pd.DataFrame
        A DataFrame with the following columns:
        - 'Name': Names of the students.
        - 'Score_1': Score of the first exam, ranging from 50 to 100.
        - 'Score_2': Score of the second exam, ranging from 50 to 100.
        - 'Shift': Shift the student is enrolled in, which can be 'Morning', 'Afternoon', or 'Evening'.
    """
    # Generating sample data
    np.random.seed(seed)  # For reproducibility

    names = ['Alice', 'Bruno', 'Carla', 'Diego', 'Eva', 'Felipe', 'Gabi', 'Hugo', 'Iara', 'Jorge', 
             'Karen', 'Luis', 'Marina', 'Nina', 'Otávio', 'Paula', 'Quico', 'Rafa', 'Silvia', 'Thiago']
    names = names[:size]

    score1 = np.random.randint(50, 100, size=size)
    score2 = np.random.randint(50, 100, size=size)
    shift = np.random.choice(['Morning', 'Afternoon', 'Evening'], size=size)

    # Creating DataFrame
    df = pd.DataFrame({
        'Name': names,
        'Score_1': score1,
        'Score_2': score2,
        'Shift': shift
    })

    return df