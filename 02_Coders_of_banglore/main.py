with open("final_datadump.txt", encoding="utf-8") as f:
    data = f.read()

chunks = data.split("\n\n")
chunks = [c for c in chunks if len(c) > 3]

def parsed_chunk(chunk):
    parsed_chunked = chunk.strip()
    seprated_parsed_chunk = parsed_chunked.split("\n")

    user_name = seprated_parsed_chunk[0]
    no_of_post = int(seprated_parsed_chunk[1].split(" post")[0].replace(",", ""))

    no_of_follower = float(
        seprated_parsed_chunk[2]
        .split(" follower")[0]
        .replace(",", "")
        .replace("K", "")
        .replace("M", "")
    )

    if "K" in seprated_parsed_chunk[2]:
        no_of_follower = int(no_of_follower * 1000)
    elif "M" in seprated_parsed_chunk[2]:
        no_of_follower = int(no_of_follower * 1_000_000)
    else:
        no_of_follower = int(no_of_follower)

    no_of_following = float(
        seprated_parsed_chunk[3]
        .split(" following")[0]
        .replace(",", "")
        .replace("K", "")
        .replace("M", "")
    )

    if "K" in seprated_parsed_chunk[3]:
        no_of_following = int(no_of_following * 1000)
    elif "M" in seprated_parsed_chunk[3]:
        no_of_following = int(no_of_following * 1_000_000)
    else:
        no_of_following = int(no_of_following)

    name = seprated_parsed_chunk[4]

    if len(seprated_parsed_chunk) > 5:
        type_of_page = seprated_parsed_chunk[5]
        bio = "\n".join(seprated_parsed_chunk[6:])
    else:
        type_of_page = "unknown"
        bio = ""

    return {
        "user_name": user_name,
        "no_of_posts": no_of_post,
        "no_of_followers": no_of_follower,
        "no_of_following": no_of_following,
        "name": name,
        "type_of_page": type_of_page,
        "bio": bio,
    }


allchunks = []

for chunk in chunks:
    parsed_chunked_variable = parsed_chunk(chunk)
    allchunks.append(parsed_chunked_variable)

print(f"the total chunks are : {allchunks} ")


import json
s=json.dumps(allchunks , indent=4)
print(s)
with open('final_datadump.json' ,'w') as f :
    f.write(s)
    

max  = 0 
for chunk in allchunks:
    if ( max < chunk['no_of_posts']) :
        max = chunk['no_of_posts']
        chunk_with_max_post = chunk   

print(f"the user with the highest post is  : {chunk_with_max_post['user_name']}")     


max_followers = 0 
for chunk in allchunks:
    if (max_followers < chunk["no_of_followers"]):
        max_followers =chunk["no_of_followers"]
        max_followers_chunk = chunk

print(f"the user with the highest number of followers  : {max_followers_chunk['user_name']}")    


max_following = 0 
for chunk in allchunks:
    if (max_following < chunk["no_of_following"]):
        max_following =chunk["no_of_following"]
        max_following_chunk = chunk

print(f" the user with the highset numbers follwoing : {max_following_chunk['user_name']}")    


categories = set()
for chunk in allchunks:
    categories.add(chunk['type_of_page'])
print("The total categories and number of total categories are :")
print(categories , len(categories))
