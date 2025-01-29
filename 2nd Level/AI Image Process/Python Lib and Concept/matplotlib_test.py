import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "x":range(1,11),
    "y":[1,2,3,4,11,7,22,8,9,2]
})

data.plot(x = 'x', y = 'y', kind = 'scatter')
plt.show()
