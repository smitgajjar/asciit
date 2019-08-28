# ASCIIT
## Convert a given image to ASCII Art

![](https://github.com/smitgajjar/asciit/blob/master/asciified_file_image.png)

### About Asciit
Asciit is nothing but a python code which reads an image file (.jpg, .png or any other)
and writes a .txt file which looks like original file.

#### Input file:
![](https://github.com/smitgajjar/asciit/blob/master/google_logo.png)

#### Output file:
![](https://github.com/smitgajjar/asciit/blob/master/asciified_file_image.png)

### Prerequisites:

- PIL (Python Imaging Library)
```
pip3 install pillow
```

### Usage:

- To directly get the output on the console, use the following command on terminal on Linux or command line on Windows
        
```
username@PC:~/location/asciit$ python3 asciit.py image_filename
```
where, image_filename specifies relative or full path to the original image

- To get output in a separate file, use the following command:
   
```
username@PC:~/location/asciit$ $python3 asciit.py image_filename output_filename 
```
where, image_filename specifies relative or full path to the original image and
	   output_filename specifies relative or full path of the .txt file which is to be created

- Refer to the comments for more information on how to use various methods defined in ImageToAscii class

### Core logic behind the code:

- PIL Image object is passed to our code
- Code first converts our image to specified width
- Transforms RGB to grayscale form
- Converts the grayscale matrix to ascii string according to the intensity

