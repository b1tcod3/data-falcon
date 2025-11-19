import pandas as pd

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'

nutri = pd.read_excel(xls)

DICT = { 1:'Male', 2:'Female' }
nutri['gender'] = nutri['gender'].replace(DICT).astype('category')
nutri['height'] = nutri['height'].astype('float')

nutri.to_csv('nutri.csv',index=False)