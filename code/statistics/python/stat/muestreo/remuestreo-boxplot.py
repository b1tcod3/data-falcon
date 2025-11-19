import pandas as pd
import numpy as np
import matplotlib.pylab as plt

WEB_PAGE_DATA_CSV = '/home/data/Documentos/practical-statistics-for-data-scientists-master/data/web_page_data.csv'

session_times = pd.read_csv(WEB_PAGE_DATA_CSV)
session_times.Time = 100 * session_times.Time

ax = session_times.boxplot(by='Page', column='Time',
                           figsize=(4, 4))
ax.set_xlabel('')
ax.set_ylabel('Time (in seconds)')
plt.suptitle('')

plt.tight_layout()
plt.show()