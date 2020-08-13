#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import pprint

def sort_key(user):
    return user[1]

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts").json().get("all")
    

    # display the methods available to our new object
    pprint.pprint(f"Most upvoted quote: {r[0].get('text')}")
    # get user with most quotes
    user_dict = {}
    for q in r:
        if 'user' in q:
            user_id = q["user"]["_id"]
            full_name = q["user"]["name"]["first"] + ' ' + q["user"]["name"]["last"]
            if user_dict.get(user_id) == None:
                user_dict[user_id] = [full_name, 1]
            else:
                user_dict[user_id][1] += 1
    user_list = []
    for u in user_dict:
        user_list.append(user_dict[u])
    user_list.sort(reverse=True, key=sort_key)
    pprint.pprint(f"user with most quotes: {str(user_list[0][0])} with {str(user_list[0][1])} quotes")

main()

