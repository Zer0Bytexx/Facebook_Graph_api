import requests

def get_facebook_user_info(user_id, access_token):
    url = f"https://graph.facebook.com/v12.0/{user_id}"
    params = {
        'access_token': access_token,
        'fields': 'id,name,posts{message,created_time},friends{name}'
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    user_id = input("Enter Facebook user ID or username: ")
    access_token = input("Enter your Facebook access token: ")

    user_info = get_facebook_user_info(user_id, access_token)

    if 'error' in user_info:
        print(f"Error: {user_info['error']['message']}")
    else:
        print(f"User ID: {user_info['id']}")
        print(f"Name: {user_info['name']}")
        
        print("\nPosts:")
        for post in user_info.get('posts', {}).get('data', []):
            print(f"Message: {post.get('message', 'No message')}")
            print(f"Created Time: {post['created_time']}")
            print("-" * 40)
        
        print("\nFriends:")
        for friend in user_info.get('friends', {}).get('data', []):
            print(f"Name: {friend['name']}")

if __name__ == "__main__":
    main()