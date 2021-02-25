// for loops
image = new SimpleImage("flowers.jpg");

// loop thru all pixels and set them to be black
for (pixel: image) {
  pixel.setRed(0);
  pixel.setGreen(0);
  pixel.setBlue(0);
}

print(image);



image = new SimpleImage("flowers.jpg");

// set all pixels red value 0, turn yellow flowers to greenish flowers
for (pixel: image) {
  pixel.setRed(0);
}

print(image);



image = new SimpleImage("flowers.jpg");

// only leave red light in image, aka red channel of image
for (pixel: image) {
  pixel.setGreen(0);
  pixel.setBlue(0);
}

print(image);
