import requests
import pprint
import pandas

api_key = ""

# movie_id = 550
# api_version = 3
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
# print(endpoint)

# r = requests.get(endpoint)
# #,json={"api_key":api_key})
# print(r.status_code)
# print(r.text)

#api_key_v4 =""

# movie_id = 550
# api_version = 4
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}"
# headers = {
#     'Authorization': f'Bearer {api_key_v4}',
#     'Content-Type': 'application/json;charset=utf-8'
# }

# r = requests.get(endpoint,headers=headers)
# print(r.status_code)
# print(r.text)



movie_id = 550
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "The Matrix"

endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"


r = requests.get(endpoint)


if r.status_code in range(200,299):
    data= r.json()
    results = data['results']
    movie_ids =set()
    if len(results) > 0:
        #print(results[0].keys())
        for result in results:
            _id = result['id']
            movie_ids.add(_id)
            #print(result['title'],_id)


output = 'movies.csv'
movie_data =[]

for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200,299):
        movie_data.append(r.json())

df =pandas.DataFrame(movie_data)
print(df.head())
df.to_csv(output,index=False)
