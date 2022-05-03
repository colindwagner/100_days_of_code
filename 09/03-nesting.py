# imagine dicts and lists as being a folder that we can add even more folders to

# {
#     Key: [List],
#     Key2: Value,
#     Key3: {Dict}
# }

##Nesting
capitals = {
    "France": "Paris",
    "Germany": "Frankfurt",
}

#nesting a list

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
        },
    "Germany": ["Berlin", "Hamburg"],
}
print(travel_log)

#nesting a dict in a list
travel_log = [
    {
        "country":"France",
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
        },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Frankfurt"],
         "total_visits": 7
    },
]


