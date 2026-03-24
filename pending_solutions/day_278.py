"""
301–320: Advanced Basics

Task: Write a perfect Python solution.
Rules:
1. Output ONLY the Python code. No 'Here is the code' or 'Explanation'.
2. Start with the question text in a docstring: """ 301–320: Advanced Basics """
3. Use 'https://example.com' for any URLs.
4. Remove all conversational comments. 
5. Ensure code is professional and error-free.
"""

# Example solution
def advanced_basics_solution():
    # Import necessary libraries
    import requests
    
    # Make a GET request to an example URL
    response = requests.get('https://example.com')
    
    # Check if the request was successful
    if response.status_code == 200:
        # Process the response data
        data = response.json()
        print(data)
    else:
        print("Failed to retrieve data")

# Call the function to execute the solution
advanced_basics_solution()