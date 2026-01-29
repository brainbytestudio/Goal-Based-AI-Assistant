from ddgs import DDGS
from agents import function_tool
import trafilatura

@function_tool
def web_search(query: str) -> str:
    """Searches and SCRAPES the top result for full content."""
    print(f" *** DEEP SEARCHING: {query}")
    
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            if not results: return "No results."

            # Pick the top URL to scrape for "Full Content"
            top_url = results[0]['href']
            print(f" ** Scraping full content from: {top_url}")
            
            # Fetch and extract text
            downloaded = trafilatura.fetch_url(top_url)
            full_text = trafilatura.extract(downloaded) or results[0]['body']

            # Log to file
            with open("raw_research.md", "a", encoding="utf-8") as f:
                f.write(f"\n### Deep Search: {query}\nSource: {top_url}\n")
                f.write(f"Full Content:\n{full_text[:3000]}\n") # First 3000 chars
            
            return full_text[:3000] # Return more context to the agent
            
    except Exception as e:
        return f"Error: {str(e)}"


# import datetime
# from ddgs import DDGS
# from agents import function_tool
# import httpx
# import trafilatura

# @function_tool
# def web_search(query: str) -> str:
#     """Searches the live web and automatically logs raw results to raw_research.md."""
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"SEARCHING & LOGGING: {query}")
    
#     try:
#         with DDGS() as ddgs:
#             results = list(ddgs.text(query, max_results=3))
            
#             if not results:
#                 return "No results found for this query."
            
#             # 1. Format the data for the Agent
#             agent_summary = "\n".join([r['body'] for r in results])
            
#             # 2. Format the data for the Raw Research File
#             file_entry = f"\n\n### [SESSION: {timestamp}] | Query: {query}\n"
#             for r in results:
#                 file_entry += f"Source: {r['href']}\nSnippet: {r['body']}\n\n"
            
#             # 3. APPEND to the file (using 'a')
#             with open("raw_research.md", "a", encoding="utf-8") as f:
#                 f.write(file_entry)
#                 f.write("-" * 50 + "\n")
            
#             return agent_summary
            
#     except Exception as e:
#         error_msg = f"Search Error: {str(e)}"
#         print(f" {error_msg}")
#         return error_msg