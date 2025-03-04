import requests


def retrieve_and_print_grid(url):
    # Fetch the content from the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print(f"Error: Unable to retrieve data. Status code: {response.status_code}")
        return

    # Print the raw response to see what is returned
    print("Raw Response:", response.text)

    try:
        # Try to parse the data as JSON
        data = response.json()
    except ValueError:
        print("Error: The response is not valid JSON.")
        return

    # Process and print the grid as before
    max_x = max([item['x'] for item in data])
    max_y = max([item['y'] for item in data])

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for item in data:
        x, y, char = item['x'], item['y'], item['char']
        grid[y][x] = char

    for row in grid:
        print(''.join(row))


# Example usage
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
retrieve_and_print_grid(url)