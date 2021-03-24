------------------------------------------------------------------------------------------------------
##################################### CANVAS WIDGETS ################################################
------------------------------------------------------------------------------------------------------

################################ Screen Coordinate System ################################
Coordinate system # Used to identify the position of each pixel in an application's window.
    # each pixel has an X coordinate and a Y coordinate. Usually written in the form
    # (X,Y). DIFFERS FROM CARTESIAN COORD SYSTEM used in Turtle graphics.
    X Coordinate: # identifies the pixels horizontal position. Increases from left to right.
    Y Coordinate: # identifies the pixels vertical position. Increases top to bottom.
    Center: # coordinates are (319,239)

    # Tkinter Canvas Widget Options: https://www.studytonight.com/tkinter/python-tkinter-canvas-widget#

------------------------------------------------------------------------------------------------------
########################### Drawing Lines: create_line Method ########################################
------------------------------------------------------------------------------------------------------
General Format: canvas_name.create_line(x1, y1, x2, y2, options...)
starting point: x1, y1
ending point: x2, y2

    ####### create_line method features #######
        # You can pass multiple sets of coordinates as arguments. See draw_multi_lines.py
        # You can pass a list or a tuple containing the coordinates as an argument.
            
            #### Tuple Example ####
            self.canvas.create_line(10, 10, 189, 10, 100, 189, 10, 10)
            # this code produces same result:
                points = [10, 10, 189, 10, 100, 189, 10, 10]
                self.canvas.create_line(points)

################################ create_line arguments ###########################################
    arrow=value: # causes the line to have arrowhead at one or both ends.
        arrow=tk.FIRST # draws an arrowhead at begining of the line
        arrow=tk.LAST # draws an arrowhead at the end of the line
        arrow=tk.BOTH # draws an arrowhead at both ends of the line

    dash=value: # uses tuple consisting of integers (that specify pattern) to changes line to a dashed line.
        dash=(5,2)  # first integer (5) specifies number of pixels to draw. 
                    # Second integer (2) specifies the number of pixels to skip.

    fill=value: # specifies color of the line, value = name of color as a string. Common colors are
                # 'red', 'green', 'blue', 'yellow', and 'cyan'. Default is black.

    smooth=value: # default is false, if you specify smooth=True, lines are drawn as curved splines.

    width=value: # specifies the width of the line, in pixels. Example: width=5. Default is 1 pixel.

------------------------------------------------------------------------------------------------------
########################### Drawing Rectangles: create_rectangle Method ##############################
------------------------------------------------------------------------------------------------------
General Format: canvas_name.create_rectangle(x1, y1, x2, y2, options...)
x1, y1: coords of upper-left corner.
x2, y2: coords of lower-right corner.

################################ create_rectangle arguments ###########################################
        dash=value: # uses tuple consisting of integers (that specify pattern) to changes line to a dashed line.
            dash=(5,2)  # first integer (5) specifies number of pixels to draw. 
                        # Second integer (2) specifies the number of pixels to skip.

        fill=value: # specifies color to fill the rectangle, value = name of color as a string. Common colors are
                    # 'red', 'green', 'blue', 'yellow', and 'cyan'. Default is no fill.

        outline=value: # Specifies the rectangle's outline. value = name of color as a string. Common colors are
                    # 'red', 'green', 'blue', 'yellow', and 'cyan'. Default is black.

        width=value: # specifies the width of the line, in pixels. Example: width=5. Default is 1 pixel.

    # Example: drawn_square.py
        # updated with arguments: self.canvas.create_rectangle(20, 20, 180, 180, dash=(5, 2), width=3)

------------------------------------------------------------------------------------------------------
############################### Drawing Ovals: create_oval Method ####################################
------------------------------------------------------------------------------------------------------
General Format: canvas_name.create_oval(x1, y1, x2, y2, options...)
    # the method draws an oval that fits just inside a bounding rectangle defined by argument coordinates.
x1, y1: coords of rectangles upper-left corner.
x2, y2: coords of rectangles lower-right corner.

Circle: # to draw a circle make all sides the same length

################################ create_oval arguments ###########################################
        dash=value: # uses tuple consisting of integers (that specify pattern) to changes line to a dashed line.
            dash=(5,2)  # first integer (5) specifies number of pixels to draw. 
                        # Second integer (2) specifies the number of pixels to skip.

        fill=value: # specifies color to fill the oval, value = name of color as a string. Common colors are
                    # 'red', 'green', 'blue', 'yellow', and 'cyan'. Default is no fill.

        outline=value: # Specifies the oval's outline. value = name of color as a string. Common colors are
                    # 'red', 'green', 'blue', 'yellow', and 'cyan'. Default is black.

        width=value: # specifies the width of the outline, in pixels. Example: width=5. Default is 1 pixel.

------------------------------------------------------------------------------------------------------
############################### Drawing Arcs: create_arc Method #####################################
------------------------------------------------------------------------------------------------------
General Format: canvas_name.create_arc(x1, y1, x2, y2, start=angle, extent=width, options...)
x1, y1: coords of rectangles upper-left corner.
x2, y2: coords of rectangles lower-right corner.
start=angle: specifies the starting angle.
extent=width: specifies the counterclockwise extent of the arc as an angle.

# Example: arc starts at 90 degrees and extends counterclockwise for 45 degrees.
   canvas_name.create_arc(10, 10, 190, 190, start=90, extent=45)

# Examples:
# draw_arc.py
# draw_piechart.py

################################ create_arc arguments ###########################################
        dash=value: # uses tuple consisting of integers (that specify pattern) to changes line to a dashed line.
            dash=(5,2)  # first integer (5) specifies number of pixels to draw. 
                        # Second integer (2) specifies the number of pixels to skip.

        fill=value: # specifies color to fill the arc, value = name of color as a string. Common colors are
                    # 'red', 'green', 'blue', 'yellow', and 'cyan'. Default is no fill.

        outline=value: # Specifies the arc's outline. value = name of color as a string. Common colors are
                    # 'red', 'green', 'blue', 'yellow', and 'cyan'. Default is black.

        width=value: # specifies the width of the outline, in pixels. Example: width=5. Default is 1 pixel.

        style=value: # specifies the style of the arc. There are three styles of arch you can draw.
            style=tkinter.PIESLICE # default arc type. Straight lines will be drawn from each endpoint
                                   # to the arc's center point. Arc will be shaped like a pie slice.
            style=tkinter.ARC # No lines will connect the endpoints. Only the arc will be drawn.
            style=tkinter.CHORD # straight line will be drawn from one endpoint of the arch to the other.

------------------------------------------------------------------------------------------------------
############################ Drawing Polygons: create_polygon Method #################################
------------------------------------------------------------------------------------------------------
General Format: canvas_name.create_polygon(x1, y1, x2, y2, ..., options...)
    # constructed of multiple line segments that are connected.
    # Point where two line segments are connected is called the Vertex.
x1, y1: coords of the first vertex (this is the first point)
x2, y2: coords of the second vertex (this is the second point)

##### Example - Points of Each Vertex in Polygon #####
# 1st Point (60, 20), 2nd Point (100, 20), 3rd Point (140, 60), 4th Point (140, 100) .... (method auto closes polygon)
canvas_name.create_polygon(60, 20, 100, 20, 140, 60, 140, 100, 100, 140, 60, 140, 20, 100, 20, 60)

################################ create_polygon arguments ###########################################
        dash=value: # uses tuple consisting of integers (that specify pattern) to changes line to a dashed line.
            dash=(5,2)  # first integer (5) specifies number of pixels to draw. 
                        # Second integer (2) specifies the number of pixels to skip.

        fill=value: # specifies color to fill the polygon, value = name of color as a string. Common colors are
                    # 'red', 'green', 'blue', 'yellow', and 'cyan'. Default is no fill.

        outline=value: # Specifies the polygon's outline. value = name of color as a string. Common colors are
                    # 'red', 'green', 'blue', 'yellow', and 'cyan'. Default is black.

        smooth=value: # default is false, if you specify smooth=True, lines are drawn as curved splines.

        width=value: # specifies the width of the outline, in pixels. Example: width=5. Default is 1 pixel.

------------------------------------------------------------------------------------------------------
################################ Drawing Text: create_text Method ####################################
------------------------------------------------------------------------------------------------------
General Format: canvas_name.create_text(x, y, text=text, options...)
(x,y): coords of text insertion point. 
text=text: specifies text to display.

# see draw_text.py
################################ create_text arguments ###########################################
        anchor=value: # this argument specifies how the text is positioned relative to its insertion point.
                      # by default anchor is set to tkinter.CENTER. See values below.

        fill=value: # specifies text color, value = name of color as a string. Common colors are
                    # 'red', 'green', 'blue', 'yellow', and 'cyan'. Default is black.

        font=value: # change default font. 
                tkinter.font.FONT # create a object and pass as value of font argument.
        
        justify=value: # if multiple lines of text are displayed, argument specifies how the lines justified.
            justify=tk.LEFT # default
            justify=tk.CENTER
            justify=tk.RIGHT

################################ create_text anchor values ###########################################
    anchor=tkinter.CENTER # text vertically and horizontally centered around insertion point. Default
    anchor=tkinter.NW # text position so insertion point is at the upper-left corner (northwest)
    anchor=tkinter.N # text position so insertion point is along the top edge of the text (north)
    anchor=tkinter.NE # text position so insertion point is at the upper-right corner (northeast)
    anchor=tkinter.W # text position so insertion point is at the text's left edge (west)
    anchor=tkinter.E # text position so insertion point is at the text's right edge (east)
    anchor=tkinter.SW # text position so insertion point is at the lower-left corner (southwest)
    anchor=tkinter.S # text position so insertion point is at the bottom edge of text (south)
    anchor=tkinter.SE # text position so insertion point is at the lower-right corner (southeast)

################################ create_text setting the font ########################################
# You can set the fornt that is used with the method by created a Font object and passing it as the font=argument.
# Font class is in the tkinter.font module, so you must include import statement.
import tkinter.font
myfont=tkinter.font.Font(family='Helvetica', size='12')

    ################################ font arguments ########################################
        family=value # Argument is a string that specifies font 'Arial', 'Courier', 'Helvetica', 'Times New Roman'
        size=value # integer that specifies font size in points
        weight=value # specifies weight of the font, values are 'bold' and 'normal'
        slant=value # specifies 'italic' or unslanted: 'roman'
        underline=value # underlined, specify 1, otherwise specify 0
        overstrike=value # crossed-out, specify 1, otherwise specify 0