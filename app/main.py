import utils
import read_csv
import charts
import pandas as pd
#from utils import get_world_percentages

def run():
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  df = pd.read_csv("data.csv")  # Nos ahorramos el método creado read_csv.py
  df = df[df['Continent'] == 'Africa'] 

  countries = df['Country/Territory'].values
  # Equivalente a -> countries = list(map(lambda x: x['Country'], data))
  percentages = df['World Population Percentage'].values
  # Equivalente a -> percentages = list(map(lambda x: x['World Population Percentage'], data))

  
  charts.generate_pie_chart(countries, percentages)

  
  
  data = pd.read_csv("data.csv")
  #data = read_csv.read_csv('data.csv')
  print(type(data))
  country = input('Type Country => ')
  print(country)

  
  def to_dict_list(data):
    if isinstance(data, pd.DataFrame):
        return data.to_dict('records')
    else:
        return data
    
  data = to_dict_list(data)
    
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    #country = to_dict_list(result)[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
 
  
  


'''
  #solucion simplificada
  countries, percentages = utils.get_world_percentages(data)
  charts.generate_pie_chart(countries, percentages)
'''

if __name__ == '__main__':
  run()

