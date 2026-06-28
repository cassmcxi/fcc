# Secret Message Decoder

A Python script that decodes a hidden message from a published Google Doc. The
doc is secretly an HTML page holding a table of characters and their x/y grid
coordinates. The script downloads it, reads the table, and plots each character
onto a grid so the blocks line up into a picture of uppercase letters.

## How it works

**Download the document and confirm it loaded.**

```python
response = requests.get(url)
if response.status_code != 200:
    print("Failed to fetch document.")
    return
```

`requests.get` fetches the page. A status code of `200` means "OK" — anything
else means the download failed, so the script stops early instead of working
with bad data.

**Parse the HTML and pull out the table cells.**

```python
soup = BeautifulSoup(response.text, 'html.parser')
lines = soup.find_all('td')
```

A published Google Doc isn't plain text — it's a full HTML page. BeautifulSoup
reads that HTML, and `find_all('td')` grabs every table cell (`<td>`), which is
where the real data lives.

**Clean the cells down to just the values.**

```python
clean_lines = []
for line in lines:
    line = line.get_text(strip=True)
    if line.lower() in ['x-coordinate', 'y-coordinate', 'character', '']:
        continue
    clean_lines.append(line)
```

Each cell still has its HTML wrapper, so `.get_text(strip=True)` pulls out just
the text inside (like `"87"`). The three header labels and any empty cells are
skipped so only real values remain.

**Group the values into (character, x, y) sets.**

```python
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
        i += 1
```

The values come in repeating sets of three: x, character, y. The loop walks
through them three at a time and stores each set as a tuple. If a chunk isn't
valid (e.g. a number won't convert), it nudges forward one and tries again.

**Build the grid and place each character.**

```python
max_x = max(p[1] for p in positions)
max_y = max(p[2] for p in positions)

grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for char, x, y in positions:
    grid[max_y - y][x] = char
```

The largest x and y set the grid's width and height. The grid starts full of
spaces, then each character is dropped into its spot. The puzzle counts `y` from
the **bottom** (like a math graph), but a list counts rows from the **top**, so
`max_y - y` flips it — otherwise the whole picture prints upside down.

**Print the message.**

```python
for row in grid:
    print("".join(row))
```

Each row is joined into a single string and printed, drawing the message line by
line.

## Running it

```bash
python3 decode-example.py
```

Requires `requests` and `beautifulsoup4`:

```bash
pip install requests beautifulsoup4
```
