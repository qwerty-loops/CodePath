#If nft_collection is empty return 0
#If nft_collection has a single element return its value
# Iterate through nft_collection and add value to a new variable total
#Average = total / Number of elements and return it



def average_nft_value(nft_collection):
    
    if len(nft_collection) ==0:
        return 0
    
    elif len(nft_collection) ==1:
        return nft_collection["value"]

    else:
        total=0
        for nft in nft_collection:
            total+=nft["value"]

    avg=total/len(nft_collection)
    return avg

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))
# Example Output:

# 5.7
# 9.15
# 0