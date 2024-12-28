import requests

GITHUB_TOKEN = "github_pat_XXXXXXXXXXXX"  # Replace with your token
REPO_NAME = "MOHAMMED-SAEED-OMER/E-operation-app"
BRANCH = "main"

def upload_to_github(file_path, commit_message):
    with open(file_path, "r") as file:
        content = file.read()
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{file_path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {
        "message": commit_message,
        "content": content.encode("utf-8").decode("latin1"),
        "branch": BRANCH
    }
    response = requests.put(url, json=data, headers=headers)
    return response.status_code, response.json()
