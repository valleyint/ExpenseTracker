import tkinter as tk
from PIL import Image, ImageTk

class ImageSwitcher:
    def __init__(self, root):
        self.root = root
        self.count = 0
        
        # Load images
        self.images = [
            Image.open('Image1.jpeg').convert("RGBA"),
            Image.open('Image2.jpeg').convert("RGBA"),
            Image.open('Image3.jpeg').convert("RGBA")
        ]
        
        # Create a label to display the images
        self.picture = tk.Label(root)
        self.picture.pack()
        
        # Start the image switching
        self.fade_in()

    def change_opacity(self, image, opacity):
        """Change the opacity of the image."""
        # Create a new image with the same size and mode
        new_image = Image.new("RGBA", image.size)
        for x in range(image.width):
            for y in range(image.height):
                r, g, b, a = image.getpixel((x, y))
                new_image.putpixel((x, y), (r, g, b, int(a * opacity)))
        return new_image

    def fade_in(self):
        if self.count >= len(self.images):
            self.count = 0
        
        # Set the image with full opacity
        self.current_image = self.images[self.count]
        self.display_image(self.current_image, 0)  # Start with 0 opacity

    def display_image(self, image, opacity):
        """Display the image with the specified opacity."""
        # Change the opacity of the image
        faded_image = self.change_opacity(image, opacity)
        self.tk_image = ImageTk.PhotoImage(faded_image)
        self.picture.config(image=self.tk_image)
        
        if opacity < 1:
            # Increase opacity gradually
            self.root.after(100, lambda: self.display_image(image, opacity + 0.1))
        else:
            # After fade-in, wait and then fade out
            self.root.after(2000, self.fade_out)

    def fade_out(self):
        # Fade out the current image
        self.display_image(self.current_image, 1)  # Start with full opacity

        # Decrease opacity gradually
        self.root.after(50, lambda: self.fade_out_opacity(1))

    def fade_out_opacity(self, opacity):
        if opacity > 0:
            self.display_image(self.current_image, opacity)
            self.root.after(100, lambda: self.fade_out_opacity(opacity - 0.1))
        else:
            # Move to the next image
            self.count += 1
            self.fade_in()

# Create the main window
root = tk.Tk()
app = ImageSwitcher(root)
root.mainloop()