from PIL import Image, ImageDraw, ImageFont
import os
from tqdm import tqdm
data_dir = r"D:\alvin\yolotrain\self_unavail"

# Directories
train_dir = os.path.join(data_dir, "")
test_dir = os.path.join(data_dir, "")
image_dir = "images"
label_dir = "labels"
output_dir = os.path.join(data_dir, "viz")

os.makedirs(output_dir, exist_ok=True)

# Get the list of image files in the train/test directory
train_image_files = os.listdir(os.path.join(train_dir, image_dir))
test_image_files = os.listdir(os.path.join(test_dir, image_dir))

# Optional: Load a font for drawing text
try:
    # Load a truetype or opentype font file, with a larger size
    font = ImageFont.truetype("arial.ttf", 14)
except IOError:
    # If loading font fails, use the default PIL font
    font = ImageFont.load_default()

for image_file in tqdm(train_image_files):
    # Image path
    image_path = os.path.join(train_dir, image_dir, image_file)

    # Label path
    label_file = os.path.splitext(image_file)[0] + ".txt"
    label_path = os.path.join(train_dir, label_dir, label_file)

    image = Image.open(image_path)
    w, h = image.size

    # Create an RGBA image for transparency
    overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    # Create a separate drawing object for the text
    text_overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw_text = ImageDraw.Draw(text_overlay)

    # Process each line in the label file
    with open(label_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        # Split the line into occupancy and coordinates
        occupancy, coordinates = line.strip().split(' ', 1)

        values = coordinates.strip().split()

        # Extract the vertices coordinates as pairs
        vertices = [(float(values[i]) * w, float(values[i + 1]) * h) for i in range(0, len(values), 2)]

        # Set the color with an alpha value for transparency (0-255)
        if occupancy == "0":
            color = (255, 0, 0, 100)  # Red with 100 alpha for transparency (Occupied)
            text = "Occupied"
        elif occupancy == '1':
            color = (0, 255, 0, 100)  # Green with 100 alpha for transparency (Vacant)
            text = "Vacant"
        else:
            color = (0, 0, 255, 100)  # Blue with 100 alpha for transparency (Unavailable)
            text = "Unavailable"

        # Draw the polygon with transparency
        draw.polygon(vertices, fill=color)

        # Find the top-right vertex
        top_right = max(vertices, key=lambda v: (v[0] - v[1]))  # Custom rule to find the top-right point

        # Get text bounding box to draw background
        text_bbox = draw_text.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Calculate the background rectangle coordinates with some padding
        padding = 5
        background_coords = [(top_right[0] - text_width - padding, top_right[1] - text_height - padding),
                             (top_right[0] + padding, top_right[1] + padding)]

        # Draw a black rectangle as background for the text
        draw_text.rectangle(background_coords, fill=(0, 0, 0, 150))  # Black with some transparency

        # Draw the text on the text overlay
        draw_text.text((top_right[0] - text_width, top_right[1] - text_height), text, fill=(255, 255, 255, 255), font=font)

    # Combine the original image, mask, and text overlay
    combined = Image.alpha_composite(image.convert('RGBA'), overlay)
    combined = Image.alpha_composite(combined, text_overlay)

    # Show the image
    # combined.show()

    # Save the image as PNG instead of JPEG
    output_path = os.path.join(output_dir, "ground_" + os.path.splitext(image_file)[0] + ".png")
    combined.save(output_path, format="PNG")
