// grayscale
image = new SimpleImage("liberty-red.jpg");

// fix the red image by copying the red value to green and blue values
for (pixel: image) {
  pixel.setGreen(pixel.getRed());
  pixel.setBlue(pixel.getRed());
}

print(image);



image = new SimpleImage("flowers.jpg");

// covert a regular color image to grayscale
for (pixel: image) {
  avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue())/3;
  pixel.setRed(avg);
  pixel.setGreen(avg);
  pixel.setBlue(avg);
}

print(image);
