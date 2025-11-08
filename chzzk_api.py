import requests
from typing import Dict

def get_channel_info(id: str) -> Dict:
    endpoint = "https://api.chzzk.naver.com/service/v1/channels/"
    request = endpoint + id
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ChzzkRecorder/1.0)",
        "Accept": "application/json"
    }   
    response = requests.get(request, headers=headers, timeout=10)
    
    if response.status_code is not 200:
        raise RuntimeError(f"Unable to request channel information, status code {response.status_code}")

    return response.json()['content']

if __name__ == "__main__":
    ci = get_channel_info("e9c11510c1c6097a20b92ebcb289b26a")
    print(ci)
    