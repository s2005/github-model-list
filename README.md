# GitHub Models API Examples

A Python application to interact with the GitHub Models API, demonstrating how to list available models.

## About GitHub Models API

GitHub Models is a recent service (announced in May 2025) that allows developers to access and experiment with AI models. The official GitHub Models API endpoints use the domain `models.github.ai`.

## Official API Endpoints

According to the official documentation and our working implementation, the GitHub Models API uses these endpoints:

- List all models: `https://models.github.ai/catalog/models`

## Official References

This implementation is based on the following official GitHub documentation and announcements:

1. [GitHub REST API: Models Catalog documentation](https://docs.github.com/en/rest/models/catalog?apiVersion=2022-11-28#list-all-models) - Official API reference for listing models
2. [GitHub Models API now available](https://github.blog/changelog/2025-05-15-github-models-api-now-available/) - Announcement of the GitHub Models API (May 15, 2025)
3. [Fine-grained PATs and GitHub Apps need updates to access GitHub Models Playground](https://github.blog/changelog/2025-03-18-as-of-march-29-fine-grained-pats-and-github-apps-need-updates-to-access-github-models-playground/) - Information about the required `models:read` permission

## Requirements

- Python 3.6+
- A GitHub Personal Access Token with the `models:read` permission

## Setup

1. Clone or download this repository
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Edit the `.env` file and replace `your_github_token_here` with your actual GitHub Personal Access Token

## Creating a GitHub Token with models:read Permission

To use this application, you need a GitHub token with the `models:read` permission:

1. Go to your GitHub account settings
2. Navigate to Developer settings → Personal access tokens
3. Select "Fine-grained tokens"
4. Click "Generate new token"
5. Set a name and expiration for your token
6. Under "Repository access", select "Public repositories (read-only)"
7. Under "Permissions", find the "Models" section and set "Read-only" access
8. Click "Generate token"
9. Copy the generated token and paste it in the `.env` file

## Usage

Run the script with:

```bash
python main.py
```

The application will:

1. Load your GitHub token from the `.env` file
2. Make an API request to retrieve the list of GitHub models from `https://models.github.ai/catalog/models`
3. Display the models in the terminal
4. Save the complete response to a `github_models.json` file

## Troubleshooting

If you receive a 401 Unauthorized error, make sure:

- Your GitHub token is correctly entered in the `.env` file
- Your token has the required `models:read` permission (as announced in the [March 2025 changelog](https://github.blog/changelog/2025-03-18-as-of-march-29-fine-grained-pats-and-github-apps-need-updates-to-access-github-models-playground/))
- Your token has not expired

## Note

This application is based on the GitHub Models API which was announced on May 15, 2025. Since this is a very recent API, there might be changes to how it works or its endpoint structure.
