import requests

def check_updates(repo_owner, repo_name):
    try:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        release_info = response.json()
        latest_version = release_info["tag_name"]
        print("Latest version:", latest_version)
        
    except requests.exceptions.RequestException as e:
        print("Error connecting to GitHub:", e)
    except KeyError:
        print("No releases found for the repository.")

def main():
    print("GitHub Update Checker")
    print("====================")
    
    repo_owner = input("Enter the repository owner (username/organization): ")
    repo_name = input("Enter the repository name: ")
    
    check_updates(repo_owner, repo_name)

if __name__ == "__main__":
    main()
