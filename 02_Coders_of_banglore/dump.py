with open("data.txt") as f:
    data = f.read()

chunks = data.strip().split("\n\n")


def parse_chunks(text):
    lines = text.strip().split("\n")

    if len(lines) < 4:
        raise ValueError(f"Invalid chunk: {lines}")

    return {
        "username": lines[0],
        "followers": int(lines[1]),
        "following": int(lines[2]),
        "bio": lines[3]
    }


all_chunks = []
for c in chunks:
    all_chunks.append(parse_chunks(c))

print(all_chunks)
