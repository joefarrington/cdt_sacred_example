import os
import json
import pandas as pd

basedir = os.path.abspath(os.path.dirname(__file__))


def load_json(filename):
    """ Load file with json. """
    with open(filename) as file:
        obj = json.load(file)
    return obj


def unlist_series(s: pd.Series) -> pd.Series:
    return s.apply(lambda x: x[0])


def get_results_df(name, number, metrics: list) -> pd.DataFrame:
    """
    Gets a dataframe from the run.json
    :param name: name of experiment folder at experiments/.
    :param number: number of experiment in folder
    :param metrics: the metrics you want to extract
    :return: a dataframe with each run and the results
    """
    experiment_path = os.path.join(basedir, name, str(number), 'run.json')
    results = load_json(experiment_path)
    if results['result'] is None:
        raise ValueError('No results for this experiment')

    hyperparameter_space_df = pd.DataFrame(results['result']['params'])
    splits = pd.DataFrame({k: v['values'] for k, v in results['result'].items() if k in metrics})

    return pd.concat([hyperparameter_space_df, splits], axis=1)


if __name__ == "__main__":
    results_df = get_results_df('my_runs', 1, metrics=['mean_test_score', 'std_test_score'])
    print(results_df)
