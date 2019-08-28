import sys
from PIL import Image

class ImageToAscii():

    '''
    Class to convert an Image to Ascii Art using PIL
    '''
    
    def __init__(self):

        '''
        Default constructor to initialize ImageToAscii object without specifying the image path
        -Note: If this constructor is used, call the setImagePath() method to provide the path
        '''

        self.ascii_char_list=[ ' ', '.' , ',' ':', ';', 'i', 'r', 's', 'X', 'A', '2', '5', '3', 'h', 'M', 'H', 'G', 'S', '#', '9', 'B', '&', '@']
        self.path = None
        self.new_width = 100
        
    def __init__(self, path):

        '''
        Constructor to initialize ImageToAscii object with the image path
        '''
        
        self.ascii_char_list=[' ', '.' , ',' ':', ';', 'i', 'r', 's', 'X', 'A', '2', '5', '3', 'h', 'M', 'H', 'G', 'S', '#', '9', 'B', '&', '@']
        self.path = path
        self.new_width = 100

        try:
            self.initial_img = Image.open(path)
        except Exception as e:
            print("Image not found, check your path again!")
        
            
    def setImagePath(self, path):

        '''
        Changes the current path of the input image
        '''
        
        try:
            self.initial_img = Image.open(path)
        except Exception as e:
            print("Image not found, check your path again!")
            
    def getImagePath(self, path):

        '''
        Returns the currently specified image path
        '''

        return self.path
    
    def setNewWidth(self, width):

        '''
        Sets the width of the output image
        '''

        self.new_width = width

    def getNewWidth(self):

        '''
        Returns the currently set width of output image
        '''

        return self.new_width
    
    def getOriginalWidth(self, image):

        '''
        Returns the original width of input image
        '''
        
        return image.size[0]

    def getOriginalHeight(self, image):

        '''
        Returns the original height of input image
        '''
        
        return image.size[1]

    def pixelToAsciiString(self, image):

        '''
        Returns the corresponding ascii string according to intensity of the grayscaled image
        '''

        return ''.join([self.ascii_char_list[px_val//25] for px_val in list(image.getdata())])


    def convert(self):

        '''
        The core method of the class which carries out the conversion
        '''
        
        #Resize the image according to specified width
        orig_width = self.getOriginalWidth(self.initial_img)
        orig_height = self.getOriginalHeight(self.initial_img)
        
        ratio = orig_height/orig_width

        new_wd = self.getNewWidth()
        new_ht = int(ratio * new_wd)

        final_img = self.initial_img.resize([new_wd, new_ht])

        #Convert to grayscale
        final_img = final_img.convert('L')

        #Convert pixels to ascii string
        ascii_str = self.pixelToAsciiString(final_img)

        ascii_list = [ascii_str[i:i+new_wd] for i in range(0, len(ascii_str), new_wd)]
        ascii_img = '\n'.join(ascii_list)   

        return ascii_img
        
    def toAsciiNow(self):

        '''
        To print the output on the terminal
        '''
        
        if self.path == None:
            print('Specify the path of image using setImagePath() method')
            return
        asciified_str = self.convert()
        print(asciified_str)
        

    def toAsciiFile(self, output_filename):

        '''
        To save the output to a file
        '''

        if self.path == None:
            print('Specify the path of image using setImagePath() method')
            return

        try:
            fp=open(output_filename, 'w')
        except Exception as e:
            print('Specified output file location does not exist!')
            return
        
        asciified_str = self.convert()
        fp.write(asciified_str)

if __name__=='__main__':
    

    '''
    Usage:
        -To directly get the output on terminal:
            $python3 asciit.py image_filename
        -To get output in a separate file:
            $python3 asciit.py image_filename output_filename
    '''
    
    if len(sys.argv) == 1:
        print('Few number of arguments \nRequired 2 or 3, Passed ', len(sys.argv))
        sys.exit()

    elif len(sys.argv) > 3:
        print('Too many arguments \nRequired 2 or 3, Passed ', len(sys.argv))
        sys.exit()

    elif len(sys.argv) == 2:
        my_image = ImageToAscii(sys.argv[1])
        my_image.toAsciiNow()

    elif len(sys.argv) == 3:
        my_image = ImageToAscii(sys.argv[1])
        my_image.toAsciiFile(sys.argv[2])
