# api_client.py
import requests
import json # Built-in, good for pretty printing if not using rich

def fetch_product_data(product_id):
    """Fetches product data from a mock API."""
    # Using JSONPlaceholder as a free, simple API
    url = f"fhdgdfkjhgskdfjghdfkgjh"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raises an HTTPError for bad responses (4XX or 5XX)
        product = response.json()
        # For more readable output of the JSON:
        print("--- Raw Product Data (JSON) ---")
        print(json.dumps(product, indent=2)) # Pretty print
        return product
    except requests.exceptions.InvalidURL as e:
        print("Invalid URL!")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching product data: {e}")
        return None

# Only run this if this file was run directly by the Python interpreter.
if __name__ == "__main__":
    print("Fetching data for product ID 1...")
    data = fetch_product_data(1)
    if data:
        # print(type(data)) # dict
        print(f"\nFetched Title: {data.get('title', 'N/A')}") # N/A is default

    print("\nFetching data for product ID 5 (example)...")
    data2 = fetch_product_data(5)
    if data2:
            print(f"\nFetched Title: {data2.get('title', 'N/A')}")

    print("\nFetching data for product ID 20 (example)...")
    data3 = fetch_product_data(20)
    if data3:
            print(f"\nFetched User ID: {data3.get('userId', 'N/A')}")
            print(f"\nFetched Completed: {data3.get('completed', 'N/A')}")
