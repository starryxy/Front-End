// expressions
// Doubles the pixel's red value
old = pixel.getRed();
pixel.setRed(old * 2);
// reduce to one line
pixel.setRed(pixel.getRed() * 2);



// for loop with expressions
image = new SimpleImage("flowers.jpg");

// change the yellow flowers to look orange
for (pixel: image) {
  pixel.setGreen(pixel.getGreen() * 0.75);
}

print(image);



image = new SimpleImage("flowers.jpg");

// make the image darker
for (pixel: image) {
  pixel.setRed(pixel.getGreen() * 0.5);
  pixel.setGreen(pixel.getGreen() * 0.5);
  pixel.setBlue(pixel.getGreen() * 0.5);
}

print(image);



image = new SimpleImage("flowers.jpg");

// change the yellow flowers to light orange
for (pixel: image) {
  pixel.setRed(pixel.getRed() * 1.3);
  pixel.setGreen(pixel.getGreen() * 0.75);
}

print(image);



// Image red, green, blue divided by 5, 10, 20; don't know which number goes with which color
// Experiment to figure it out, and scale them back up by * 5, * 10, * 20 to recover the original image
image = new SimpleImage("51020-banana.png");

for (pixel: image) {
  pixel.setRed(pixel.getRed() * 20);
  pixel.setGreen(pixel.getGreen() * 5);
  pixel.setBlue(pixel.getBlue() * 10);
}

print(image);
