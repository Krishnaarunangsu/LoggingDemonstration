from typing import Optional, Union, Tuple

import numpy as np
from numpy.core._multiarray_umath import ndarray

x = np.linspace(10, 20, 15, endpoint=True)
print(x)

y = np.linspace (10, 20, 5, endpoint=False)
print(y)


z: Union[ndarray, Tuple[ndarray, Optional[float]]] = np.linspace(1,2,5, retstep = True)
print(z)

# default base is 10
a = np.logspace(1.0, 2.0, num = 10)
print(a)

b = np.logspace(1,10,num = 10, base = 2)
print(b)
