import numpy as np
import pandas as pd
import matplotlib as plt
x = pd.period_range(pd.datetime.now(), periods=200, freq='d')
x = x.to_timestamp().to_pydatetime()
# 產生三組，每組 200 個隨機常態分布元素
y = np.random.randn(200, 3).cumsum(0)
plt.plot(x, y)
plt.show()