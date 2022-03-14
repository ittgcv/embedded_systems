import pandas as pd
import numpy as np
def color_negative_values(val):
  color = 'red' if val < 0 else 'black'
  return 'color: %s' % color
def color_max(s):
    is_max = s == s.max()
    return ['background-color: lightblue' if v else '' for v in    is_max]
df = pd.DataFrame({'A':np.linspace(1,8,8),
                   'B':np.random.random(8),
                   'C':np.random.randn(8),
                   'D':np.random.randn(8),
                   'E':np.random.randint(-5,5,8)})
df.iloc[[1,5],[1,3]] = np.nan
df.style.applymap(color_negative_values)
print(df)
