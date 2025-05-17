import os
import requests
import json
from dotenv import load_dotenv

def main():
    # Load .env file
    load_dotenv()
    
    # Get GitHub API token from .env
    github_token = os.getenv("GITHUB_TOKEN")
    
    if not github_token:
        print("Error: GitHub token not found in .env file")
        print("Please create a .env file with a GITHUB_TOKEN variable")
        return
    
    # Set up API endpoint and headers
    # The correct URL for GitHub Models API
    url = "https://models.github.ai/catalog/models"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {github_token}"
    }
    
    try:
        # Make API request
        print(f"Making request to {url}")
        print(f"Using token: {github_token[:5]}...{github_token[-5:] if len(github_token) > 10 else ''}")
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response as JSON
            models_data = response.json()
            
            # Check if the data is a list (array) of models
            if isinstance(models_data, list):
                print(f"Found {len(models_data)} GitHub models:\n")
                
                for i, model in enumerate(models_data, 1):
                    print(f"Model #{i}:")
                    # Print model attributes safely with better error handling
                    model_id = model.get('id', 'Unknown ID')
                    model_name = model.get('name', 'Unknown Name')
                    
                    # Handle publisher info safely
                    publisher = model.get('publisher', {})
                    publisher_name = 'Unknown Publisher'
                    if isinstance(publisher, dict):
                        publisher_name = publisher.get('name', 'Unknown Publisher')
                    
                    # Handle modalities safely
                    modalities = model.get('modalities', [])
                    modalities_str = ', '.join(modalities) if isinstance(modalities, list) else 'None'
                    
                    # Handle description safely
                    description = model.get('description', 'No description')
                    if description and isinstance(description, str):
                        # Truncate long descriptions
                        description = description[:100] + "..." if len(description) > 100 else description
                    else:
                        description = 'No description'
                    
                    # Print the model information
                    print(f"  ID: {model_id}")
                    print(f"  Name: {model_name}")
                    print(f"  Publisher: {publisher_name}")
                    print(f"  Modalities: {modalities_str}")
                    print(f"  Description: {description}")
                    print()
                
                # Save full response to a JSON file for further inspection
                with open("github_models.json", "w") as f:
                    json.dump(models_data, f, indent=2)
                print(f"Full model details saved to github_models.json")
            else:
                # Handle unexpected response format
                print("Unexpected response format. Saving raw response to github_models.json for inspection.")
                with open("github_models.json", "w") as f:
                    json.dump(models_data, f, indent=2)
                
        elif response.status_code == 401:
            print("Authentication Error: Your GitHub token doesn't have the required permissions.")
            print("Make sure your token has the 'models:read' permission.")
            print(f"API Response: {response.text}")
        elif response.status_code == 404:
            print(f"Error 404: Resource not found at {url}")
            print("This could indicate that the API endpoint URL is incorrect.")
            print(f"Response: {response.text}")
            print("\nAdditional troubleshooting:")
            print("1. Check if your GitHub token has access to GitHub Models")
            print("2. The GitHub Models API was just released on May 15, 2025, so it might still be rolling out")
        else:
            print(f"API Request Failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # Print more details for debugging
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
