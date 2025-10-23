

#Create a dictionary
#Iterate through the nft_collection
#Check the name of the creator
# Key-value = Creator name : Value of creator occurence
# IF occurence of creator  > 1 , add to popular creator list and return it

#Edge Case : If nft_collection list happens to have a single element/dicitionary have a singlwe key value pair return an empty list
    
    # if len(nft_collection) ==1:
    #     return []

def identify_popular_creators(nft_collection):

    count_of_creator={}

    for nft in nft_collection:
        count_of_creator[nft["creator"]] = count_of_creator.get(nft["creator"],0) + 1

    popular_creator=[]
    for i,v in count_of_creator.items():
        if v>1:
            popular_creator.append(i)
    return popular_creator
    

    


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
# Example Output:

# ['ArtByAlex']
# ['SpaceArt']
# []