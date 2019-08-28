# ASCIIT
## Convert a given image to ASCII Art
![](https://github.com/smitgajjar/asciit/blob/master/command_line.png)

### About Asciit
**_Asciit_** is nothing but a python code which reads an image file (.jpg, .png or any other)
and generates a .txt file containing ascii characters which looks like original file.

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
- First, clone the repository at some *location*.
- To directly get the output on the console, use the following command:
        
```
username@PC:~/location/asciit$ python3 asciit.py image_filename
```

where, ```image_filename``` specifies relative or full path to the original image

- To get output in a separate file, use the following command:
   
```
username@PC:~/location/asciit$ $python3 asciit.py image_filename output_filename 
```
	
where, ```image_filename``` specifies relative or full path to the original image and
	   ```output_filename``` specifies relative or full path of the .txt file which is to be created

- Refer to the comments for more information on how to use various methods defined in *ImageToAscii* class

### Core logic behind the code:
- PIL Image object is passed to convert() method.
- Converts our image to specified width.
- Transforms RGB to grayscale form.
- Converts the grayscale matrix to ascii string according to the intensity.

Image source: [Link to the google_logo image](https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjK37ev16bkAhVUeysKHSIUB6wQMwiGASgOMA4&url=https%3A%2F%2Fwww.dynamicevents.ie%2Fthe-best-off-site-event-ever-google-event-at-palmerstown-house%2Fgoogle-logo-2%2F&psig=AOvVaw1i2Fh2FAbybUtO_yA5weOh&ust=1567120081612632&ictx=3&uact=3)