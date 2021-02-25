// if statement in for loop
image = new SimpleImage("stop.jpg");

// change the red stop sign to blue (this way some white area also is changed to blue)
for (pixel: image) {
  if (pixel.getRed() > 233) {
    pixel.setRed(0);
    pixel.setGreen(0);
    pixel.setBlue(255);
  }
}

print(image);



image = new SimpleImage("stop.jpg");

// a better way to select red areas of the stop sign
// red > avg can tell if red is high relative to other two colors
for (pixel: image) {
  avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue())/3;
  if (pixel.getRed() > avg * 1.5) {
    pixel.setRed(0);
    pixel.setGreen(0);
    pixel.setBlue(255);
  }
}

print(image);



image = new SimpleImage("curb.jpg");

// change the red curb to gray
for (pixel: image) {
  avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue())/3;
  if (pixel.getRed() > avg * 1.2) {
    pixel.setRed(120);
    pixel.setGreen(120);
    pixel.setBlue(120);
  }
}

print(image);



image = new SimpleImage("curb.jpg");

// a better way to change the red curb to gray
// set red/green/blue to avg instead of a fix number can show the light and dark pattern in original image
for (pixel: image) {
  avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue())/3;
  if (pixel.getRed() > avg * 1.2) {
    pixel.setRed(avg);
    pixel.setGreen(avg);
    pixel.setBlue(avg);
  }
}

print(image);
