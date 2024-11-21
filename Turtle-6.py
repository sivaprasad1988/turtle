import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg',20)

color_list = []
for color in colors:
    rgb = color.rgb  # This is an Rgb named tuple
    rgb_tuple = tuple(rgb)  # Convert to a tuple
    color_list.append(rgb_tuple)

print(color_list)