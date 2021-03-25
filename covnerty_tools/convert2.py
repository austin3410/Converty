import os
from PIL import Image
import pdf2image
import shutil

class Convert2:

    def __init__(self, image, convert_to, convert_flags, output_path, greyscale):
        # image sends the full path of the image.
        # Convert_to send a str of the convert flag example: 'JPG'
        # convert_flags is a dict of dicts of acceptable conversion types.
        # output_path is a str of the out_put selected by the user.
              
        self.image = image
        self.convert_to = convert_to
        self.convert_flags = convert_flags
        self.output_path = output_path
        self.isGreyscale = greyscale

        self.current_path = os.path.dirname(image)

        filename = os.path.basename(image)
        self.filename, self.current_ext = os.path.splitext(filename)

        if self.convert_flags[convert_to]["EXT"] == "CURRENT":
            self.new_ext = self.current_ext
        else:
            self.new_ext = convert_flags[convert_to]["EXT"]
        
        if convert_to == "JPG":
            if self.current_ext == ".pdf":
                pil_images = self.pdftopil(self.image, ".jpg")

                for i in pil_images:
                    i.save(self.output_path + f"/{filename}.jpg")  
            else:
                self.convert_to_jpg(self.image, self.filename, self.convert_flags, self.convert_to, self.output_path, self.new_ext, self.isGreyscale)
        
        elif convert_to == "PNG":
            print(convert_to)
        
        elif convert_to == "PDF":
            self.convert_to_pdf(self.image, self.filename, self.convert_flags, self.convert_to, self.output_path, self.new_ext, self.current_ext, self.isGreyscale)
    
    def pdftopil(self, image, fmt):
        pil_images = pdf2image.convert_from_path(image, dpi=400, output_folder=None, first_page=None, last_page=None, fmt=fmt, thread_count=1, userpw=None, use_cropbox=False, strict=False, poppler_path="poppler-0.68.0_x86//bin")
        return pil_images
    
    def copy_image(image, output_path):
        shutil.copy(image, output_path)
    
    def convert_to_jpg(self, image, filename, convert_flags, convert_to, output_path, new_ext, isGreyscale):
        if isGreyscale:
            new_image = Image.open(rf"{image}").convert("L")
        else:
            new_image = Image.open(rf"{image}").convert(convert_flags[convert_to]["PIL_FLAG"])
        new_image.save(output_path + f"/{filename}{new_ext}")
    
    def convert_to_pdf(self, image, filename, convert_flags, convert_to, output_path, new_ext, current_ext, isGreyscale):
        if current_ext != ".pdf":
            new_image = Image.open(rf"{image}").convert(convert_flags[convert_to]["PIL_FLAG"])
            new_image.save(output_path + f"/{filename}{new_ext}")
        else:
            self.copy_image(image, output_path)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """if convert_to == "Greyscale":
            self.convert2grey(image, convert_to, current_extension, convert_flags, output_path, filename, new_ext)


        if current_extension == new_ext:
            if current_path == output_path:
                pass
            else:
                self.copy2(image, output_path)
        elif convert_to in ("PNG", "JPG", "PDF"):
            self.convert2png(image, convert_to, current_extension, convert_flags, output_path, filename, new_ext)
        elif convert_to == "Greyscale":
            if current_extension == ".pdf":
                pass
            else:
                self.convert2png(image, convert_to, current_extension, convert_flags, output_path, filename, new_ext)       

    def convert2png(self, image, convert_to, current_extension, convert_flags, output_path, filename, new_ext):
        if current_extension == ".pdf":
            pil_images = self.pdftopil(image, convert_flags[convert_to]["EXT"])
        
        if "pil_images" not in locals():
            new_image = Image.open(rf"{image}").convert(convert_flags[convert_to]["PIL_FLAG"])
            new_image.save(output_path + f"/{filename}{new_ext}")
        else:
            for i in pil_images:
                i.save(output_path + f"/{filename}.jpg")
    
    def convert2grey(self, image, convert_to, current_extension, convert_flags, output_path, filename, new_ext):
        if current_extension == ".pdf":
            pil_images = self.pdftopil(image, ".jpg")

            for i in pil_images:
                i.save(output_path + f"/temp_{filename}.jpg")
                new_image = Image.open(rf"{output_path}/temp_{filename}.jpg").convert(".pdf")
                new_image.save(output_path + f"/{filename}.pdf")

    
    def pdftopil(self, image, fmt):
        pil_images = pdf2image.convert_from_path(image, dpi=200, output_folder=None, first_page=None, last_page=None, fmt=fmt, thread_count=1, userpw=None, use_cropbox=False, strict=False)
        return pil_images

    def copy2(self, image, output_path):
        shutil.copy(image, output_path)"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    """def convert_image(self, image, convert_to, convert_flags, output_path):
        new_image = Image.open(rf"{image}").convert(convert_flags[convert_to]["PIL_FLAG"])
        new_path = os.path.dirname(output_path)
        filename = os.path.basename(image)
        new_filename, current_extension = os.path.splitext(filename)

        if convert_flags[convert_to]["EXT"] == "CURRENT":
            new_ext = current_extension
        else:
            new_ext = convert_flags[convert_to]["EXT"]
        
        new_image.save(output_path + f"/{new_filename}{new_ext}")"""