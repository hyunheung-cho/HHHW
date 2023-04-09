async function getRandomImage() {
    try {
        const response = await fetch('/get_random_image');
        const image = await response.json();
        console.log(image.url); // log the image URL to the console
        document.getElementById('randomImage').src = image.url;
        document.getElementById('foodName').textContent = image.name;
    } catch (error) {
        console.error(error);
    }
}

// Load initial image
getRandomImage();
