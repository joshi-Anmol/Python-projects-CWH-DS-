with open("data.txt" , encoding= 'utf-8') as f :
    data = f.read()

chunk = data.strip().split("\n\n")

print(chunk[1])

def parsed_chunk(chunk):
    try :
        parsed_chunked = chunk.strip( ) 
        seprated_parsed_chunk = parsed_chunked.split("\n")
        user_name = seprated_parsed_chunk[0]
        no_of_post = seprated_parsed_chunk[1]
        no_of_follower = seprated_parsed_chunk[2]
        no_of_following = seprated_parsed_chunk[3]
        name = seprated_parsed_chunk[4]
        if len(seprated_parsed_chunk)>=5:
            type_of_page = seprated_parsed_chunk[5]
            bio ="\n".join(seprated_parsed_chunk[6:])
        else :
            type_of_page="unknown"    
            bio =""

        return {
            "user_name": user_name, 
            "no_of_posts": no_of_post,
            "no_of_followers": no_of_follower, 
            "no_of_following": no_of_following, 
            "name": name, 
            "type_of_page": type_of_page, 
            "bio": bio
        }
    except Exception as e :
        print(e ,  chunk)

        


all_chunk = []
for chunked in chunk :
    parsed_chunked = parsed_chunk(chunked)
    all_chunk.append(parsed_chunk)
print(all_chunk,"\n")
