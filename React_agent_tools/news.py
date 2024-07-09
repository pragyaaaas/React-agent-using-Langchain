from newsapi import NewsApiClient
from langchain.agents import tool

@tool

def get_latest_news(query):
    """
    Search for the latest news articles related to a given query using the NewsAPI.

    Args:
        query (str): The search query to look for news articles.

    Returns:
        dict: A dictionary containing the latest news articles related to the query.
              The dictionary has the following structure:
              {
                  "articles": [
                      {
                          "title": str,
                          "description": str,
                          "url": str
                      },
                      ...
                  ]
              }
              If an error occurs or no articles are found, the dictionary will contain an "error" key with an error message.

    This function uses the NewsAPI (https://newsapi.org/) to search for the latest news articles related to the given query.
    It requires an API key, which should be stored in an environment variable named "NEWS_API_KEY".

    The function makes a GET request to the NewsAPI's "everything" endpoint, passing the query and other parameters
    such as language and sort order. It then processes the response data and returns a dictionary containing the
    article titles, descriptions, and URLs for the top 5 articles related to the query.

    If the API request is successful and articles are found, the function returns a dictionary with a list of article
    dictionaries under the "articles" key. If no articles are found or an error occurs, the function returns a dictionary
    with an "error" key containing an appropriate error message.

    Example:
        >>> get_latest_news("Apple")
        {
            "articles": [
                {
                    "title": "Apple Unveils New M2 Chip for MacBooks",
                    "description": "Apple announced the new M2 chip, which will power the latest MacBook Air and 13-inch MacBook Pro models.",
                    "url": "https://example.com/apple-m2-chip"
                },
                ...
            ]
        }

        >>> get_latest_news("Invalid Query")
        {"error": "No articles found for the given query."}
    """
    api_key = 'sk-proj-mD04a3mBhMHVoxLxF7mmT3BlbkFJ98XR86inj890MqOftFeL'
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(q=query, language='en', sort_by='publishedAt')
    
    if articles['status'] == 'ok':
        news_list = []
        for article in articles['articles'][:5]: 
            news_list.append({
                'title': article['title'],
                'description': article['description'],
                'url': article['url']
            })
        return {"articles": news_list}
    else:
        return {"error": "Unable to fetch news"}


if __name__ == "__main__":
    print(get_latest_news("Apple"))
