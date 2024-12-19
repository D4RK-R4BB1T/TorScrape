import os
import time
import pyautogui
import urllib.parse

BASE_DIRECTORY = "PATH\TO\YOUR\DOWNLOAD\DIRCTORY"
TEXT_FILE = "PATH\TO\YOUR\TEXT\FILE.TXT"
BASE_URL = input("Enter the base URL (e.g., http://example.onion/): ").strip()


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def navigate_to_url(url):
    pyautogui.hotkey('ctrl', 'l')  
    time.sleep(1)
    pyautogui.typewrite(url)
    time.sleep(1)
    pyautogui.press('enter')

def save_page(file_path):
    pyautogui.hotkey('ctrl', 's')  
    time.sleep(2)
    pyautogui.typewrite(file_path)
    time.sleep(1)
    pyautogui.press('enter')

def process_url(url):
    parsed_url = urllib.parse.urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')

    subfolder_path = os.path.join(BASE_DIRECTORY, *path_parts[:-1])
    create_folder_if_not_exists(subfolder_path)

    # Determine file name
    file_name = f"{path_parts[-1] or 'index'}.html"
    return subfolder_path, file_name

def main():
    with open(TEXT_FILE, 'r') as file:
        links = [line.strip() for line in file if line.strip()]

    if not links:
        print("No links found in the text file.")
        return

    # Navigate to the first link immediately
    first_url = links[0]
    if not first_url.startswith(BASE_URL):
        first_url = urllib.parse.urljoin(BASE_URL, first_url)

    print(f"Navigating to: {first_url}")
    navigate_to_url(first_url)
    time.sleep(5)  

    for index, url in enumerate(links):
        if not url.startswith(BASE_URL):
            url = urllib.parse.urljoin(BASE_URL, url)

        print(f"Processing: {url}")
        subfolder_path, file_name = process_url(url)
        file_path = os.path.join(subfolder_path, file_name)

        if index == 0:
            print("Skipping save for the initial navigation to ensure proper workflow.")
            continue  

        navigate_to_url(url)
        time.sleep(15)  

        save_page(file_path)
        print(f"Saved: {file_path}")

if __name__ == "__main__":
    main()
