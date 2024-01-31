# downloading image file in python
# we get request from pip
import requests

# getting info 
r = requests.get("url")
print(r)
print(r .content)


# posting info
r = requests.post("url")
print(r)
print(r.json())


# delete some resources
r = requests.delete("url")
print(r)
print(r.json())

# it is used to update data not whole resourse post
r = requests.put("url")
print(r)
print(r .content)

# simillar of get but without the response body
r = requests.head("url")
print(r)

# small changes in resources
r = requests.patch("url")
print(r)
print(r .content)

# gettin an img
r = requests.get("url")
with open("python_logo.png",'wb') as f:
    f.write(r.content)

    
# advantages of requests
# Simplicity and Ease of Use
# Error Handling
# Streamlined Binary Handling
# Community Support    