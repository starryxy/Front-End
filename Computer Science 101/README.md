## Computer Science 101

Course and exercises code for Nick Parlante's Stanford CS101 course.

#### Topics
- The nature of computers and code, what they can and cannot do
- How computer hardware works: chips, cpu, memory, disk
- Necessary jargon: bits, bytes, megabytes, gigabytes
- How software works: what is a program, what is "running"
- How digital images work
- Computer code: loops and logic
- Big ideas: abstraction, logic, bugs
- How structured data works
- How the internet works: ip address, routing, ethernet, wi-fi
- Computer security: viruses, trojans, and passwords
- Analog vs. digital
- Digital media, images, sounds, video, compression

#### Course Specific JavaScript Functions
| Function  | Description |
| ------------- | ------------- |
| `image = new SimpleImage("flowers.jpg");` | Set the variable image to hold `flowers.jpg` image |
| `image.setZoom(5);` | Set the image to print at 5x size on screen. Useful to make changes on very small images such as `x.png` visible |
| `print(image);` | Print the image to the screen |
| `pixel = image.getPixel(0, 0);` | Retrieve the pixel at x,y (0, 0) (i.e. the upper left pixel) and store it in a variable named pixel. Changes on that pixel, e.g. pixel.setRed(255);, change the pixel in the original image |
| `print(pixel);` | Print the RGB values for one pixel, in the format `r:200 g:12 b:166` |
| `pixel.setRed(255);` | Change the pixel's red value to be 255 (can specify any value between 0-255 within the parenthesis). There are analogous functions `pixel.setGreen(number);` and `pixel.setBlue(number);` for the other two colors. If the number is outside the range 0-255, it is automatically limited to 0 or 255 |
| `red = pixel.getRed();` | Retrieve the red value from a pixel (a number in the range 0-255), and store it in a variable named red. There are analogous functions `pixel.getGreen();` and `pixel.getBlue();` |
| `image.getWidth()`, `image.getHeight()` | Retrieve the width and height of an image |
| `image.setSize(width, height);` | Scale an image up or down in size so it has the given width and height |
| `image.setSameSize(other_image);` | Scale an image up or down in size, keeping its proportions, so it is at least as big as the other_image specified |
