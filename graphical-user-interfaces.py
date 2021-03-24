# GUI Programs are event driven.

------------------------------------------------------------------------------------------
##################################### TKINTER WIDGETS ####################################
------------------------------------------------------------------------------------------
##################################### widgets summary ####################################
    button - # a button that can cause an action to occur when clicked
    canvas - # a rectangular area that can be used to display graphics
    checkbutton - # a button that may be in either the "on" or "off" position 
    entry - # an area in which the user may type a single line of input from the keyboard
    frame - # a container that can hold other widgets. Usefule for organizing and arranging
        # groups of widgets in a window
    label - # an area that displays one line of text or an image
    listbox - # a list from which the user may select an item
    menu - # a list of menu choices that are displayed when the user clicks a menubutton
    menubutton - # a menu that is displayed on the screen and may be clicked by the user
    message - # displays multiple lines of text
    radiobutton - # a widget that can be either selected or deselected. Radiobutton widgets 
    # usually appear in groups and allow the user to select one of several options.
    scale - # a widget that allows the user to select a value by moving a slider along a track
    scrollbar - # can be used with some other types of widgets to provide scrolling ability
    text - # a widget that allows the user to enter multiple lines of text input
    toplevel - # a container, like a frame, but displayed in its own window.

##################################### WIDGETS IN USE ####################################
Pack Arguments:
    side - # changes layout by specifying an argument to the pack method
        arguments - # side='top', side='bottom', side='left', side='right'
        label1_name.pack(side='left') # these labels will appear side-by-side
        label2_name.pack(side='left')

Frames:
    # Frames are a container that can hold other widgets. (A widget that holds other widgets).
        top_frame = tkinter.Frame(root_widget_name) # create frame
        label1 = tkinter.Label(top_frame, text='This is the H1') # create label
        label1.pack(side='top') # determine where widget should be positioned in frame (pack)
        top_frame.pack() # pack the frame

Buttons:
    IMPORT - import tkinter - # must be used on all examples below in addition to messagebox etc
    SHOWINFO FUNCTION - # tkinter.messagebox.showinfo(title, message) <- general format
        import tkinter.messagebox # the function showinfo is in the tkinter.messagebox module
        button_name = tkinter.Button(root_widget_name, text='Click Here!', command=do_something)
        do_something = tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button')
    
    ENTRY WIDGET - # you can use entry widget's get method to retrieve input data from the user.
        import tkinter.messagebox
        label_name = tkinter.Label(root_widget_name, text='What is your name?')
        name_entry = tkinter.Entry(label_name, width=50)
        name = name_entry.get()
        tkinter.messagebox.showinfo('The name entered is,', name)
        # see kilo_converter.py for full code example

    RADIOBUTTONS: # the round buttons that allow a user to select an option. Appear in groups.
                    # Only one can be selected at a time (mutually exclusive).
        IntVar: # Associate radiobutton group with IntVar object, when Radiobutton widet is selected, 
                # stores its unique integer value in the IntVar object.
        
        # See radiobutton_demo.py for full code
        self.radio_var = tkinter.IntVar() # IntVar() class to store value in objects
        self.radio_var.set(1) # Set the intVar object to 1.
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Option 1', variable=self.radio_var, value=1) # Create a Radiobutton widgets
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Option 2', variable=self.radio_var, value=2) # Create a Radiobutton widgets
        tkinter.messagebox.showinfo('Selection', 'You selected option ' + str(self.radio_var.get())) # callback function

    RADIOBUTTONS using Callback Function: # using callback func when radiobutton is selected, the method is executed immediately
        self.rb1 = tkinter.Radiobutton(self.top_frame,text='Option 1',variable=self.radio_var,value=1,command=self.my_method_)
        # The code uses the argument command=self.my_method to specify that my_method is the callback function.

    CHECK BUTTONS: # may be selected or deselected.
        IntVar: # associate a different IntVar object with each Checkbutton (unlike radiobuttons). 
        # create IntVar objects
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()

        # Set the intVar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text'Option 1', variable=self.cb_var1) # create widgets in frame
        self.cb2 = tkinter.Checkbutton(self.top_frame, text'Option 2', variable=self.cb_var2)
        # See checkbutton_demo.py for full code.

Labels:
    StringVar - # when StringVar is associated with Label widget,# Any value stored in the object
        # will automatically be displayed in the label.
        str_object_name = tkinter.StringVar() # strvar object        
        label2_name = tkinter.Label(top_frame, textvariable=str_object_name) # label associated with object
        value.set(label2_name) # use StringVar objects set() method to call 
        # see program kilo_converter2.py for full code example


------------------------------------------------------------------------------------------
########################### TKINTER STEPS & EXPLANATIONS #################################
------------------------------------------------------------------------------------------
# In tkinter, everything is a widget. When you use tkinter, you make widgets out of widgets
1) IMPORT: # import the tkinter module
        import tkinter
        # or
        from tkinter import *

2) ROOT WIDGET: # Tk() - The first thing you must always do is create the root widget. Example:
    # class root widget:
        def __init__(self):
            self.root_widget_name = tkinter.Tk()
    # no class root widget:
        root_widget_name = Tk()

3) FRAMES: # IF applicable - Create the frames to group your label widgets.
    top_frame = tkinter.Frame()
    mid_frame = tkinter.Frame()
    bottom_frame = tkinter.Frame()

4) LABEL WIDGET: # Secondly, create the label widget and pass the root widget as an argument. 
        # This specifies that we want the Label widget to belong to the root widget.
        # THIS CODE IS DIFFERENT IF YOU USED FRAMES - see kilo_converter2.py

    # class label widget:
        self.label_name = tkinter.Label(self.root_widget_name, text='Hello World!')
    # no class label widget:
        label_name = Label(root_widget_name, text='Hello world!')

5) PACK METHOD: # Next we call the label's pack method. The pack method determines where a widget
        # should be positioned, and makes the widget visible with the main window is displayed.
        # You should call the pack method for each widget in a window.

    # class pack method:
        self.label_name.pack()
    # no class pack method:
        label_name.pack()

6) MAINLOOP METHOD: # Next we call the mainloop method, which triggers a loop event.
    # This is how we get our program to display on the screen. mainloop() is case sensitive.

    # class mainloop method - calls the tkinter module's mainloop method: 
        tkinter.mainloop() 
    # no class mainloop method - calls the tkinter module's mainloop method from the root widget: 
        root_widget_name.mainloop() 

7) INSTANCE: # if using a class, made sure to create an instance of the Class
    new_gui = ClassName()

------------------------------------------------------------------------------------------
############################# EXAMPLES FOR ABOVE STEPS ###################################
------------------------------------------------------------------------------------------
        hello_world2.py # code taken from this file.
        import tkinter 
        class MyGUI:
            # builds the GUI when an instance of the class is created.
            def __init__(self):

                # creates a root widget and assigns it to self.main_window
                self.main_window = tkinter.Tk() # .Tk() root widget

                # Creates a Label widget and assigns it to self.label.
                # The first argument is self.main_window, which is a reference to the root widget -
                # - this specifies that we want the Label widget to belong to the root widget
                # The second argument is text='Hello World!', this specifies the text we want
                # displayed in the label
                self.label = tkinter.Label(self.main_window,
                                        text='Hello World!')

                # Call the Label widget's pack method. The pack method determines where a widget
                # should be positioned and makes the widget visible when the main window is displayed
                # (You call the pack method for each widget in a window)
                self.label.pack()

                # Enter the tkinter main loop.
                # This calls the tkinter module's mainloop method, which displays the programs 
                # main widown.
                tkinter.mainloop()

        # Create an instance of the MyGUI class.
        my_gui = MyGUI()

        ########################## tkinter online tutorial #############################
        -------------------------------GUI wPython----------------------------
        Codemy.com tutorial https://youtu.be/yQSEXcf6s2I

        ### CREATE A WIDGET ###
            from tkinter import * # imports everything
            # in tkinter everything is a widget. First thing you do is create the root widget.
            root = Tk() # this needs to happen first - root widget

            # creates label widget, add root as an argument because label goes into root widget
            myLabel = Label(root, text='Hello world!') # 1 create label widget
            myLabel.pack() # 2 shoves it into the screen ("pack" shoves it in)

            # event that loops
            root.mainloop()





-------------------------------empty window-------------------------------------
import tkinter
class MyGUI:
    def __init__(self):
        self.main_window = tkinker.Tk() # create main window widget
        tkinter.mainloop() # enter the tkinter main loop

my_gui = MyGUI()
-------------------------------keyboard event binding----------------------------
https://youtu.be/GLnNPjL1U2g
