import requests
import json

url = "https://hyijso7cij.execute-api.us-east-1.amazonaws.com/default/getTemplates"

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Test Case 1: Music Event
event1 = ["music",
          "light",
          "concert",
          ""]

response1 = requests.post(url, data=json.dumps(event1), headers=headers)
print("Test Case 1: Music Event\n", response1.text)

# Test Case 2: Sports Event
event2 = ["sports",
          "bright",
          "soccer",
          ""]

response2 = requests.post(url, data=json.dumps(event2), headers=headers)
print("Test Case 2: Sports Event\n", response2.text)

# Test Case 3: Business Event
event3 = ["business",
          "professional",
          "conference",
          ""]

response3 = requests.post(url, data=json.dumps(event3), headers=headers)
print("Test Case 3: Business Event\n", response3.text)

# Test Case 4: Travel Event
event4 = ["travel",
          "adventure",
          "road trip",
          ""]

response4 = requests.post(url, data=json.dumps(event4), headers=headers)
print("Test Case 4: Travel Event\n", response4.text)


# Test Case 5: Art Event
event5 = ["art",
          "colorful",
          "exhibition",
          ""]

response5 = requests.post(url, data=json.dumps(event5), headers=headers)
print("Test Case 5: Art Event\n", response5.text)

# Test Case 6: Technology Event
event6 = ["technology",
          "modern",
          "conference",
          ""]

response6 = requests.post(url, data=json.dumps(event6), headers=headers)
print("Test Case 6: Technology Event\n", response6.text)

# Test Case 7: Food and Drink Event
event7 = ["food and drink",
          "tasty",
          "wine tasting",
          ""]

response7 = requests.post(url, data=json.dumps(event7), headers=headers)
print("Test Case 7: Food and Drink Event\n", response7.text)

