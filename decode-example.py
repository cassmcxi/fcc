import requests

def decode_secret_message(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch document.")
        return

    lines = response.text.strip().splitlines()

    print("RAW LINES FROM DOCUMENT:")
    print(lines[:30])  # Show first 30 lines of content for debugging

    # Clean lines: remove blank lines and header labels
    clean_lines = []
    for line in lines:
        line = line.strip()
        if line.lower() in ['x-coordinate', 'y-coordinate', 'character', '']:
            continue
        clean_lines.append(line)

    # Now parse every 3 lines as: x, char, y
    positions = []
    i = 0
    while i + 2 < len(clean_lines):
        try:
            x = int(clean_lines[i])
            char = clean_lines[i + 1]
            y = int(clean_lines[i + 2])
            positions.append((char, x, y))
            i += 3
        except (ValueError, IndexError):
            i += 1  # Skip bad chunks

    if not positions:
        print("No valid data found.")
        return

    max_x = max(p[1] for p in positions)
    max_y = max(p[2] for p in positions)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for char, x, y in positions:
        grid[y][x] = char

    for row in grid:
        print("".join(row))

code_url = 'https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub'

print(decode_secret_message(code_url))
