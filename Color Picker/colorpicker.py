# Color Picker Software
# Develop By: Ivan Brix Olaguir

# Tkinter library
from tkinter import*
from tkinter import colorchooser
from tkinter import messagebox
from PIL import ImageColor
import pyperclip

# Window Screen
root = Tk()
root.title("Color Picker")
width = 350
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.resizable(0,0);
root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

# Window background color and cursor
root.configure(bg="#ffff80", cursor="arrow")

# Window Icon
root.iconbitmap("C:\\Users\\Administrator\\Desktop\\Projects\\Projects\\Python\\Color Picker\\colorpickericon.ico")



# Function of Select Color
def color_chooser():

	# Color Picker
	color = colorchooser.askcolor(title="Color Picker")[1]

	# Convert Hex to RGB
	hex = color.strip('#')
	insert_rgb = str(tuple(int(hex[i:i+2], 16)for i in (0,2,4)))[1:-1]
	
	# Insert the color code to rgb entry box
	rgb_entry.delete(0, END)
	rgb_entry.insert(END, insert_rgb)
	

	# Insert color code to hex entry box
	hex_entry.delete(0, END)
	hex_entry.insert(END, color)

	# Configure the background color 
	color_label.config(bg=color)

# Function of Slider Color
def color_slider(event):

	# Get the value of slider
	red = red_slider.get()
	green = green_slider.get()
	blue = blue_slider.get()

	# RGB Color
	rgb_color = f'{red},{green},{blue}'

	# Convert RGB Color to Hex
	hex_color = "#%02x%02x%02x" % (red, green, blue)
	
	# Configure the color background
	color_label.config(bg=hex_color)
	
	#Insert color code to hex entry box
	hex_entry.delete(0, END)
	hex_entry.insert(END, hex_color)

	# Insert color code to rgb entry box
	rgb_entry.delete(0, END)
	rgb_entry.insert(END, rgb_color)

# Copy Hex code from hex entry box
def hex_copy():
	pyperclip.copy(hex_entry.get())

# Copy RGB code from rgb entry box
def rgb_copy():
	pyperclip.copy(rgb_entry.get())
	

# Color Label
color_label = Label(root, bg="white", width=39, height=12, relief="groove")
color_label.pack(pady=5)

# Color Button
color_button = Button(root, text="Select Color", font=("Normal", 15), bg="#3f0066", fg="white", relief="groove", command=color_chooser)
color_button.pack(pady=5)

# Slider Frame
slider_frame = Frame(root, bd=2, relief="sunken")
slider_frame.pack(pady=3)

# Red Label
red_label = Label(slider_frame, bd=0, text="R", fg="red", font=('arial', 10, "bold"))
red_label.grid(column=0, row=0)

# Red Slider
red_slider = Scale(slider_frame, from_=0, to=255, length=210, fg="red", orient=HORIZONTAL, command=color_slider)
red_slider.grid(column=1, row=0)

# Green Label
green_label = Label(slider_frame, bd=0, text="G", fg="green", font=('arial', 0, 'bold'))
green_label.grid(column=0, row=1)

# Green Slider
green_slider = Scale(slider_frame, from_=0, to=255, length=210, fg="green", orient=HORIZONTAL, command=color_slider)
green_slider.grid(column=1, row=1)

# Blue Label
blue_label = Label(slider_frame, text="B", bd=0, fg="blue", font=('arial', 0, 'bold'))
blue_label.grid(column=0, row=2)

# Blue Slider
blue_slider = Scale(slider_frame, from_=0, to=255, length=210, fg="blue", orient=HORIZONTAL, command=color_slider)
blue_slider.grid(row=2, column=1)

# Frame of hex and rgb
text_frame = Frame(root, bd=2, relief="groove", bg="#f4fa43")
text_frame.pack(pady=3)

# Hex Label 
hex_label = Label(text_frame, text="HEX: ", bg="#f4fa43", font=('arial', 10, 'normal'))
hex_label.grid(column=0, row=0)

# Hex Entry Box
hex_entry = Entry(text_frame, width=12, font=('arial', 10, 'normal'))
hex_entry.grid(column=1, row=0, padx=3)

# Hex Copy Button
hex_copy_button = Button(text_frame, text="Copy", bd=2, relief="groove", font=('arial', 10, 'normal'), bg="red", fg="white", command=hex_copy)
hex_copy_button.grid(column=2, row=0, padx=5)

# RGB Label
rgb_label = Label(text_frame, text="RGB: ", bg="#f4fa43", font=('arial', 10, 'normal'))
rgb_label.grid(column=0, row=1)

# RGB Entry
rgb_entry = Entry(text_frame, width=12, font=('arial', 10, 'normal'))
rgb_entry.grid(column=1, row=1, padx=3)

# RGB Copyt Button
rgb_copy_button = Button(text_frame, text="Copy", bd=2, relief="groove", font=('arial', 10, 'normal'), bg="red", fg="white", command=rgb_copy)
rgb_copy_button.grid(column=2, row=1, padx=5)

# About Label
about_label = Label(root, text="", font=("Helvetica", 10), bg="#202422", fg="white", bd=0, relief="groove")
about_label.pack()


# About Button
about_button = Button(root, bitmap="question", bg="cyan", fg="black", command=lambda : messagebox.showinfo("About", "Develop By: Ivan Brix Olaguir"))
about_button.pack(anchor=E)


# Hover Effects
color_button.bind("<Enter>", lambda x: [color_button.config(bg="grey"), about_label.config(text="Select Color")])
color_button.bind("<Leave>", lambda x: [color_button.config(bg="#3f0066"), about_label.config(text="")])

about_button.bind("<Enter>", lambda x: [about_button.config(bg="white"), about_label.config(text="About")])
about_button.bind("<Leave>", lambda x: [about_button.config(bg="cyan"), about_label.config(text="")])

hex_copy_button.bind("<Enter>", lambda x: [hex_copy_button.config(bg="cyan"), about_label.config(text="Copy HEX Code")])
hex_copy_button.bind("<Leave>", lambda x: [hex_copy_button.config(bg="red"), about_label.config(text="")])

rgb_copy_button.bind("<Enter>", lambda x: [rgb_copy_button.config(bg="cyan"), about_label.config(text="Copy RGB Code")])
rgb_copy_button.bind("<Leave>", lambda x: [rgb_copy_button.config(bg="red"), about_label.config(text="")])

# Binding Exit
root.bind("<Control-q>", lambda x: root.destroy())

# Run the tkinter event loop
root.mainloop()


