import pandas as pd
from zenml import step

@step
def dynamic_importer() -> str:

    data ={
        'Order': [1, 2],
        'PID': [526301100, 526301101],
        'MS SubClass': [60, 20],
        'Lot Frontage': [65.0, 80.0],
        'Lot Area': [8450, 9600],
        'Overall Qual': [7, 6]
    }

    df = pd.DataFrame(data)

    Jason_data = df.to_json(df)

    return Jason_data