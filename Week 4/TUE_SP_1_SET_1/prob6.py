def process_nft_queue(nft_queue):
    
    nft_q=[]
    for nft in nft_queue:
        nft_q.append(nft["name"])
    return nft_q

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))
# Example Output:

# ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']
# ['Golden Hour', 'Sunset Serenade', 'Ocean Waves']
# ['Crypto Kitty', 'Galactic Voyage']