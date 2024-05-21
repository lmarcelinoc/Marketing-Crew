import requests

HEYGEN_API_KEY = 'YOUR_HEYGEN_API_KEY'

def create_video(script):
    url = 'https://api.heygen.com/v1/video'
    headers = {'Authorization': f'Bearer {HEYGEN_API_KEY}'}
    data = {
        'script': script,
        'voice': 'en_us_male1',
        'avatar': 'default_avatar'
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    script = "Welcome to our marketing agency. We use AI to improve your marketing strategies."
    print(create_video(script))
