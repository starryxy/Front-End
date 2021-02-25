// bluescreen
image = new SimpleImage("stop.jpg");
back = new SimpleImage("leaves.jpg");
// set leaves image to be at least the same size of stop image
back.setSameSize(image);

// replace the red stop sign to leaves: for each red pixel, copy over the pixel at the position from leaves image to stop image
for (pixel: image) {
  avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue())/3;
  if (pixel.getRed() > avg * 1.5) {
    x = pixel.getX();
    y = pixel.getY();
    pixel2 = back.getPixel(x, y);
    pixel.setRed(pixel2.getRed());
    pixel.setGreen(pixel2.getGreen());
    pixel.setBlue(pixel2.getBlue());
  }
}

print(image);



image = new SimpleImage("monkey.jpg");
back = new SimpleImage("moon.jpg");
back.setSameSize(image);

// replace the blue blanket background of monkey image to moon image
for (pixel: image) {
  avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue())/3;
  if (pixel.getBlue() > avg * 0.9) {
    pixel2 = back.getPixel(pixel.getX(), pixel.getY());
    pixel.setRed(pixel2.getRed());
    pixel.setGreen(pixel2.getGreen());
    pixel.setBlue(pixel2.getBlue());
  }
}

print(image);
