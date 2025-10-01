def most_endangered(species_list):
    
    if len(species_list)==0:
        return None
    
    else:
        end_name = species_list[0]["name"]
        end_population = species_list[0]["population"]

        for i in range(len(species_list)):
            cur_pop = species_list[i]["population"]
            cur_name = species_list[i]["name"]
            if cur_pop < end_population:
                end_population = cur_pop
                end_name= cur_name
        return end_name


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))