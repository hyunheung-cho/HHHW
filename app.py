from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

images = [
    {'url': 'static/red_fish_looks_delicious.jpg', 'name': 'Red Fish'},
    {'url': 'static/BJs_favorite_food_is_bbq.jpg', 'name': 'BBQ'},
    {'url': 'static/Typical_American_Burger_Meal.jpg', 'name': 'American Burger Meal'},
    {'url': 'static/Something_colorful_and_healthy.jpg', 'name': 'Healthy Food'},
    {'url': 'static/Some_fresh_fruits.jpg', 'name': 'Fruits and Vegetables'},
    # ... Add more local images and food names here ...
    {'url': 'https://picsum.photos/id/237/200/300', 'name': 'Random Image'},
    {'url': 'https://picsum.photos/seed/picsum/200/300', 'name': 'Random Image'},
    {'url': 'https://picsum.photos/200/300?grayscale', 'name': 'Random Image'},
    {'url': 'https://picsum.photos/200/300/?blur', 'name': 'Random Image'},
    {'url': 'https://picsum.photos/200/300/?blur=9', 'name': 'Random Image'},
    # ... Add more external image URLs and food names here ...
]

with open('/Users/H2/Library/CloudStorage/GoogleDrive-hcho226@umd.edu/My Drive/HHHW/get urls of images/food_images.txt', 'r') as f:
    urls = f.read().splitlines()

for url in urls:
    images.append({'url': url, 'name': 'New Image'})

@app.route('/')
def index():
    random_image = random.choice(images)
    return render_template('index.html', image=random_image)

@app.route('/get_random_image')
def get_random_image():
    random_image = random.choice(images)
    return jsonify(random_image)

if __name__ == "__main__":
    app.run(debug=True)
