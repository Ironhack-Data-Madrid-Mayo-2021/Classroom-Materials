import pickle
import pandas as pd

model = pickle.load(open("./my_logistic.pkl", "rb"))

columns = ['mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area',
       'mean_smoothness', 'mean_compactness', 'mean_concavity',
       'mean_concave_points', 'mean_symmetry', 'mean_fractal_dimension',
       'radius_error', 'texture_error', 'perimeter_error', 'area_error',
       'smoothness_error', 'compactness_error', 'concavity_error',
       'concave_points_error', 'symmetry_error', 'fractal_dimension_error',
       'worst_radius', 'worst_texture', 'worst_perimeter', 'worst_area',
       'worst_smoothness', 'worst_compactness', 'worst_concavity',
       'worst_concave_points', 'worst_symmetry', 'worst_fractal_dimension']


def predict_entry(info_dict):
    # pass to pandas series
    s = pd.Series(info_dict)
    s = s.reindex(columns).fillna(0)
    print(s.shape)
    s = s.values.reshape(1, -1)
    print(s.shape)

    pred = model.predict_proba(s)[:, 1]
    return pred[0]
