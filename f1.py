"""F1 Analysis Routines"""
# Imports
import pickle
import pandas as pd
import numpy as np
from dataclasses import dataclass


#Open the pickeled model file
with open('logregmodel.sav', 'rb') as file:
    model = pickle.load(file)

c = ['race_year','start_position','race_Italian Grand Prix', 'race_United States Grand Prix',
    'country_Azerbaijan', 'country_Bahrain', 'country_Belgium', 'country_Brazil',
    'country_Canada', 'country_France', 'country_Hungary', 'country_Italy',
    'country_Japan', 'country_Mexico', 'country_Monaco','country_Netherlands',
    'country_Qatar', 'country_Saudi Arabia', 'country_Singapore',
    'country_Spain', 'country_UAE', 'country_UK', 'country_USA',
    'country_United States', 'dn_Australian', 'dn_Canadian', 'dn_Danish',
    'dn_Dutch', 'dn_Finnish', 'dn_French', 'dn_German', 'dn_Japanese',
    'dn_Mexican', 'dn_Monegasque', 'dn_New Zealander', 'dn_Spanish',
    'dn_Thai', 'constructor_Ferrari', 'constructor_McLaren',
    'constructor_RB F1 Team', 'constructor_Sauber', 'constructor_Williams',
    'cn_French', 'cn_German']

def driver_input(year):
  """ """
  if year == 2022:
      print("\n1: albon, 2: alonso, 3: bottas, 5: gasly, 6: hamilton, 7: hulkenberg,\n8: latifi, 9: leclerc, 10: kevin_magnussen, 11: norris, 12: ocon, 13: perez,\n14: ricciardo, 15: russell, 16: sainz, 17: mick_schumacher, 18: stroll,\n19: tsunoda, 20: max_verstappen, 21: vettel, 22: zhou")
  elif year == 2023:
    print("\n1: albon, 2: alonso, 3: bottas, 4: de_vries, 5: gasly, 6: hamilton,\n7: hulkenberg, 9: leclerc, 10: kevin_magnussen, 11: norris, 12: ocon,\n13: perez, 14: ricciardo, 15: russell, 16: sainz,  18: stroll, 19: tsunoda,\n20: max_verstappen, 22: zhou, 23: lawson, 24: piastri, 25: sargeant")
  elif year == 2024:
    print("\n1: albon, 2: alonso, 3: bottas, 5: gasly, 6: hamilton, 7: hulkenberg,\n9: leclerc, 10: kevin_magnussen, 11: norris, 12: ocon, 13: perez, \n14: ricciardo, 15: russell, 16: sainz,  18: stroll, 19: tsunoda, 20: max_verstappen, \n22: zhou, 24: piastri, 25: sargeant")
  else:
    return('Error! Invalid year please restart to try again')

  driver = int(input("\nPlease enter your chosen driver number: "))
  if driver < 1 or driver > 25:
    return("Error! Invalid driver please restart to try again")

  # Set all values to 0
  dn_Australian = 0
  dn_Canadian = 0
  dn_Danish = 0
  dn_Dutch = 0
  dn_Finnish = 0
  dn_French = 0
  dn_German = 0
  dn_Japanese = 0
  dn_Mexican = 0
  dn_Monegasque = 0
  dn_New_Zealander = 0
  dn_Spanish = 0
  dn_Thai = 0

  constructor_Ferrari = 0
  constructor_McLaren = 0
  constructor_RB = 0
  constructor_Sauber = 0
  constructor_Williams = 0

  cn_French = 0 # Alpine
  cn_German = 0 # Mercedes

  @dataclass
  class Driver:
    """Dataclass for driver information"""
    id: int
    name: str
    nationality: str
    cconstructor: str



  driver_data = [Driver(1, 'Albon', 'Thai', 'Williams'), 
        Driver(2,'Alonso', 'Spanish', 'Alpine'), 
        Driver(3, 'Bottas', 'Finnish', 'Sauber'), 
        Driver(4, 'DeVries', 'Dutch', 'Red Bull'),
        Driver(5, 'Gasly', 'French', 'AlphaTauri'), 
        Driver(6, 'Hamilton', 'German', 'Mercedes'), 
        Driver(7, 'Hulkenberg', 'German', 'Mercedes'),
        Driver(8, 'Latifi', 'Canadian', 'Williams'),
        Driver(9, 'Leclerc', 'Monegasque', 'Ferrari'),
        Driver(10, "Kevin Magnussen", "Danish", "Haas"),
        Driver(11, 'Norris', 'British', 'McLaren'),
        Driver(12, 'Ocon', 'French', 'Alpine'),
        Driver(13, 'Perez', 'Mexican', 'Red Bull'),
        Driver(14, 'Ricciardo', 'Australian', 'McLaren'),
        Driver(15, 'Russell', 'British', 'Mercedes'),
        Driver(16, 'Sainz', 'Spanish', 'Ferrari'),
        Driver(17, 'Mick Schumacher', 'German', 'Haas'),
        Driver(18, 'Stroll', 'Canadian', 'Aston Martin'),
        Driver(19, 'Tsunoda', 'Japanese', 'Red Bull'),
        Driver(20, 'Max Verstappen', 'Dutch', 'Red Bull'),
        Driver(21, 'Vettel', 'German', 'Aston Martin'),
        Driver(22, 'Zhou', 'Chinese', 'Alfa Romeo'),
        Driver(23, 'Lawson', 'New Zealander', 'Red Bull'),
        Driver(24, 'Piastri', 'Australian', 'McLaren'),
        Driver(25, 'Sargeant', 'American', 'Williams')]


  # Converts driver into true
  if driver == 1:
      driver = 'Albon'
      dn_Thai = 1
      constructor_Williams = 1
  elif driver == 2:
      driver = 'Alonso'
      dn_Spanish = 1
      if year == 2022:
        cn_French = 1
      else:
        cn_French = 0
  elif driver == 3:
      driver = 'Bottas'
      dn_Finnish = 1
      constructor_Sauber = 1
  elif driver == 4:
      driver = 'DeVries'
      dn_Dutch = 1
      constructor_RB = 1
  elif driver == 5:
      driver = 'Gasly'
      dn_French = 1
      cn_French = 1
  elif driver == 6:
      driver = 'Hamilton'
      cn_German = 1
  elif driver == 7:
      driver = 'Hulkenberg'
      dn_German = 1
  elif driver == 8:
      driver = 'Latifi'
      constructor_Williams = 1
      dn_Canadian = 1
  elif driver == 9:
      driver = 'Leclerc'
      dn_Monegasque = 1
      constructor_Ferrari = 1
  elif driver == 10:
      driver = 'Kevin Magnussen'
      dn_Danish = 1
  elif driver == 11:
      driver = 'Norris'
      constructor_McLaren = 1
  elif driver == 12:
      driver = 'Ocon'
      dn_French = 1
      cn_French = 1
  elif driver == 13:
      driver = 'Perez'
      dn_Mexican = 1
  elif driver == 14:
      driver = 'Ricciardo'
      dn_Australian = 1
      if year == 2022:
        constructor_McLaren = 1
      else:
        constructor_RB = 1
  elif driver == 15:
      driver = 'Russell'
      cn_German = 1
  elif driver == 16:
      driver = 'Sainz'
      dn_Spanish = 1
      constructor_Ferrari = 1
  elif driver == 17:
      driver = 'Mick Schumacher'
      dn_German = 1
  elif driver == 18:
      driver = 'Stroll'
  elif driver == 19:
      driver = 'Tsunoda'
      dn_Japanese = 1
      constructor_RB = 1
  elif driver == 20:
      driver = 'Max Verstappen'
      dn_Dutch = 0
  elif driver == 21:
      driver = 'Vettel'
      dn_German = 1
  elif driver == 22:
      driver = 'Zhou'
      constructor_Sauber = 1
  elif driver == 23:
      driver = 'Lawson'
      dn_New_Zealander = 1
      constructor_RB = 1
  elif driver == 24:
      driver = 'Piastri'
      constructor_McLaren = 1
      dn_Australian = 1
  elif driver == 25:
      driver = 'Sargeant'
      constructor_Williams = 1
  else:
      return('Error! Invalid Driver code please restart to try again')


  return [driver, dn_Australian, dn_Canadian, dn_Danish, dn_Dutch, dn_Finnish,
          dn_French, dn_German, dn_Japanese, dn_Mexican, dn_Monegasque,
          dn_New_Zealander, dn_Spanish, dn_Thai, constructor_Ferrari,
          constructor_McLaren, constructor_RB, constructor_Sauber, constructor_Williams,
          cn_French, cn_German]
  
