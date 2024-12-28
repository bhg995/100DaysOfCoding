
capitals = {
    "AFGHANISTAN" : "KABUL",
    "ALBANIA": "TIRANA",
    "ALGERIA": "ALGIERS",
    "ANDORRA": "ANDORRA LA VELLA",
    "ANGOLA": "LUANDA",
    "ANTIGUA & BARBUDA": "SAINT JOHN'S",
    "ARGENTINA": "BUENOS AIRES",
    "ARMENIA": "YEREVAN",
    "AUSTRALIA": "CANBERRA",
    "AUSTRIA": "VIENNA",
    "AZERBAIJAN": "BAKU",
    "The Bahamas": "NASSAU",
    "BAHRAIN": "MANAMA",
    "BANGLADESH": "DHAKA",
    "BARBADOS": "BRIDGETOWN",
    "BELARUS": "MINSK",
    "BELGIUM": "BRUSSELS",
    "BELIZE": "BELMOPAN",
    "BENIN": "PORTO-NOVO",
    "BHUTAN": "THIMPHU",
    "BOLIVIA": "SUCRE, LA PAZ",
    "BOSNIA & HERZEGOVINA": "SARAJEVO",
    "France" : "Paris",
    "Germany" : "Berlin",
}

# Nested list

#travel_log = {
#    "France" : ["Paris", "Lille", "Dijon", "Marseille", "Lyon"],
#    "Germany" : ["Stuttgart", "Frankfurt", "Düsseldorf", "Berlin", "Munich"],
#}

# Print Lille
#print(travel_log["France"][1])

nested = ["A", "B", ["C", "D"]]

# Print letter D
print(nested[2][1])

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

# Print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])