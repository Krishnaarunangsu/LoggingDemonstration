import numpy as np
import pandas as pd
data = pd.Series(np.random.randn(10),index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                                            [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(f'Multi-index Series:\n{data}')
print(f'*****************************************')
test=pd.DataFrame(data)
check=test.reset_index(inplace=True)
print(f'Dataframe from Multi-index Series:{check}')
