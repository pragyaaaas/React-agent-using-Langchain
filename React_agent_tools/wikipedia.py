import wikipedia
from langchain.agents import tool

@tool

def search_wikipedia(query):
    """
    Search Wikipedia for a given query and return a summary of the page.

    Args:
        query (str): The search query to look up on Wikipedia.

    Returns:
        str: A summary of the Wikipedia page related to the query, or an error message if no page is found or an error occurs.

    This function uses the `wikipedia` library to search for a Wikipedia page based on the given query.
    It attempts to retrieve a summary of the page (up to 2 sentences) and returns it as a string.
    If the query is ambiguous and multiple pages are found, it returns a disambiguation error message.
    If no page is found, it returns a "Wikipedia page not found" message.
    If any other exception occurs, it returns an error message with the exception details.

    Example:
        >>> search_wikipedia("Paris")
        "Wikipedia summary: Paris is the capital and most populous city of France, with an estimated population of 2,165,423 residents as of 2020, in an area of 105 square kilometers (41 square miles)."

        >>> search_wikipedia("Python programming language")
        "Wikipedia summary: Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation."

        >>> search_wikipedia("Nonexistent topic")
        "Wikipedia page not found."
    """
    try:
        result = wikipedia.summary(query, sentences=2)
        return f"Wikipedia summary: {result}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e}"
    except wikipedia.exceptions.PageError:
        return "Wikipedia page not found."
    except Exception as e:
        return f"An error occurred: {e}"
