// zoom in image 20x
image = new SimpleImage("x.png");
image.setZoom(20);

// set pixel (0, 0) red value to 255, pixel is at upper left corner of image
pixel0 = image.getPixel(0, 0);
pixel0.setRed(255);

// set pixel (1, 0) to be yellow, pixel is on the right of (0, 0)
pixel1 = image.getPixel(1, 0);
pixel1.setRed(255);
pixel1.setGreen(255);

// set pixel (0, 1) to be white, pixel is under (0, 0)
pixel2 = image.getPixel(0, 1);
pixel2.setRed(255);
pixel2.setGreen(255);
pixel2.setBlue(255);

// set pixel (1, 1) to be light red
pixel3 = image.getPixel(1, 1);
pixel3.setRed(255);
pixel3.setGreen(200);
pixel3.setBlue(200);

print(image);
