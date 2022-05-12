import pandas as pd
import qwak
from qwak.model.base import QwakModelInterface


class TestModel(QwakModelInterface):

    def __init__(self):
        print('Model Created!')

    def build(self):
        print('Running the build')

    @qwak.api()
    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        print('Prediction')
        return pd.DataFrame([])
