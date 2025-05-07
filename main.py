import requests
import argparse 
from utils.events import Activity

parser = argparse.ArgumentParser(description="Displays GitHub activity of a GitHub user.")

parser.add_argument('username', metavar="username", type=str, help="enter the github username")
args = parser.parse_args()

base_url = "https://api.github.com/users"


def github_user_activity(username):
    url = f"{base_url}/{username}/events"
    res = requests.get(url)
    # print(res)
    if res.status_code == 200:
        events = res.json()
        return events
    else:
        print(f"Status Code: {res.status_code}, failed request.")

username = args.username
# username = "abhishekganji27"
events = github_user_activity(username)

print(f"---{"No" if not events else ""} Activity of {username}----")

if events:

    activity = Activity()    
    for event in events:
        event_type = event['type']
        event_handler_fn = activity.get_event_fn(event_type)
        if event_handler_fn:
            activity.helper(event_handler_fn, event)
    
    print(activity.final_summary())
    
