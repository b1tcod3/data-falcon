import pandas as pd
import numpy as np
import matplotlib.pylab as plt

WEB_PAGE_DATA_CSV = '/home/data/Documentos/practical-statistics-for-data-scientists-master/data/web_page_data.csv'

session_times = pd.read_csv(WEB_PAGE_DATA_CSV)
session_times.Time = 100 * session_times.Time

mean_a = session_times[session_times.Page == 'Page A'].Time.mean()
mean_b = session_times[session_times.Page == 'Page B'].Time.mean()
print(mean_b - mean_a)                           