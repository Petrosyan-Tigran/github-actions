import os

import time
import requests



def ping_url(url, delay, max_trials):
    """
    Pings a URL until a successful response (HTTP 200) or max_trials is reached.

    Parameters:
    - url (str): The URL to ping.
    - delay (int): Delay in seconds between trials.
    - max_trials (int): Maximum number of attempts.

    Returns:
    - bool: True if a successful response (HTTP 200) is received, otherwise False.
    """
    trials = 0
    while trials < max_trials:
        try:
            response = requests.get(url, timeout=10)  # 10 seconds timeout
            if response.status_code == 200:
                print(f"Website {url} is reachable")
                return True
            else:
                print(f"Trial {trials + 1}: Received status code {response.status_code}")
        except requests.RequestException as e:
            print(f"Trial {trials + 1}: Request failed - {e}")
        
        trials += 1
        time.sleep(delay)
    
    return False


def run():
    website_url = os.getenv("INPUT_URL")
    delay = int(os.getenv("INPUT_DELAY"))
    max_trials = int(os.getenv("INPUT_MAX_TRIALS"))

    website_reachable = ping_url(website_url, delay, max_trials)

    if not website_reachable:
        raise Exception(f"Website {website_url} is malfirmed or unreachable." )
    
    print(f"Website {website_url} is reachable")

    print("Hellow world")



if __name__ == "__main__":
    run()