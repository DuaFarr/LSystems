from curses import window
from tkinter import *
import turtle

root = Tk()
root.geometry("1920x1080")


        
# dictionary that will store all your production rules
DICT_OF_RULES = {} 


def create_pen(initial_angle):

    # Create your pen
    pen = turtle.Turtle() 
    # Adjust your pen's width
    pen.pensize(1)
    # Adjust your pen's color
    pen.pencolor('green')
    # Adjust how fast you want to draw (fastest = 0)
    pen.speed(0)
    # Specify a title for your window
    pen.screen.title('L-System')
    # Specify initial direction you want to draw in
    pen.setheading(initial_angle) 

    return pen


def production_rule(sequence):

    # if predecessor string is in the dictionary
    if sequence in DICT_OF_RULES:
        # return the new successor string
        return DICT_OF_RULES[sequence]
    # else if it is not present, just return 
    # the predecessor string mapped to itself
    return sequence


def apply_production_rules(axiom, iterations):

    # turn axiom string into a list of substrings
    # in our case, each of these substrings are 
    # an element of our list and each starts out
    # being a single character like F, +, -, etc
    list_of_substrings = [axiom]
    # for each iteration
    for _ in range(iterations):
        # start from the last substring in your list of substrings
        current_substring = list_of_substrings[-1]
        # for each character in that current substring, apply the production rule to it
        new_axiom = [production_rule(char) for char in current_substring]
        # add the new string to the list of substrings
        list_of_substrings.append(''.join(new_axiom))
    return list_of_substrings


def draw_L_system(our_pen, DICT_OF_RULES, segment_length, angle):
    # initialize your stack to push and pop your current L-system states 
    stack = []
    # for each symbol in your given string
    for command in DICT_OF_RULES:
        # begin drawing
        our_pen.pendown()
        if command in ['F', 'R', 'L']:
            # draw one line segment length forward
            our_pen.forward(segment_length)
        elif command == 'f':
            # lift pen up / stop drawing
            our_pen.penup()  
            our_pen.forward(segment_length)
        elif command == "+":
            # turn left
            our_pen.left(angle)
        elif command == "-":
            # turn right
            our_pen.right(angle)
        elif command == "[":
            # push string / state to the memory stack
            stack.append((our_pen.position(), our_pen.heading()))
        elif command == "]":
            # lift pen up / stop drawing
            our_pen.penup()
            # pop string / state off the memory stack
            position, heading = stack.pop()
            our_pen.goto(position)
            our_pen.setheading(heading)


def get_model():

	axiom1 = axiom.get()
	p_rule1=p_rule.get()
	p_rule_0=p_rule0.get()
	iterations1 = no_of_itr.get()
	segment_length1 = segment_length.get()
	Initial_angle1 = Initial_angle.get()
	drawing_angle1 = drawing_angle.get()
	if p_rule_0 == "":
		return
	elif p_rule_0 == '0':
		key, value = p_rule1.split('->')
		# Represents our dictionary of rules
		DICT_OF_RULES[key] = value
	else:
		key, value = p_rule1.split('->')
		key1, value1 = p_rule_0.split('->')
		# Represents our dictionary of rules
		DICT_OF_RULES[key] = value
		# Represents our dictionary of rules
		DICT_OF_RULES[key1] = value1
	# Create the whole L-System by applying all the rules the starting axiom
	list_of_entire_L_system = apply_production_rules(axiom1, int(iterations1))  # axiom (initial string), nth iterations

	# Initialize Turtle object
	recursive_pen = create_pen(float(Initial_angle1))
	# Initialize the background paper or window you'll be drawing on
	window = turtle.Screen()  # create graphics window
	# Set the color of that background
	window.bgcolor('black')
	# Set the size of that background
	window.screensize(2500, 2500)

	# Turn the list representing the entire L-system
	# into an actual geometric drawing
	draw_L_system(recursive_pen, list_of_entire_L_system[-1], int(segment_length1), float(drawing_angle1))  # draw list_of_entire_L_system
	# Ensures that the window that you are drawing in 
	# doesn't immediately close after execution
	window.exitonclick()
    




Label(root, text="L-System App", bg="#000000", fg="white", width=20, height=2).place(x=870)

axiom_lbl = LabelFrame(root)
axiom_lbl.pack(pady=50)

axiom_lbl = LabelFrame(root, text="Starting axiom (w):")
axiom_lbl.pack(pady=10)

axiom = Entry(axiom_lbl, font=("Helvetica", 15))
axiom.pack(pady=10, padx=20)

p_rule_lbl = LabelFrame(root, text="Production rule:")
p_rule_lbl.pack(pady=10)

p_rule = Entry(p_rule_lbl, font=("Helvetica", 15))
p_rule.pack(pady=10, padx=20)

p_rule_lbl1 = LabelFrame(root, text="Production rule: (0 if no rule)")
p_rule_lbl1.pack(pady=10)

p_rule0 = Entry(p_rule_lbl1, font=("Helvetica", 15))
p_rule0.pack(pady=10, padx=20)


no_of_itr_lbl = LabelFrame(root, text="Number of iterations n:")
no_of_itr_lbl.pack(pady=10)

no_of_itr = Entry(no_of_itr_lbl, font=("Helvetica", 15))
no_of_itr.pack(pady=10, padx=20)


segment_length_lbl = LabelFrame(root, text="Segment length:")
segment_length_lbl.pack(pady=10)

segment_length = Entry(segment_length_lbl, font=("Helvetica", 15))
segment_length.pack(pady=10, padx=20)


Initial_angle_lbl = LabelFrame(root, text="Initial angle:")
Initial_angle_lbl.pack(pady=10)

Initial_angle = Entry(Initial_angle_lbl, font=("Helvetica", 15))
Initial_angle.pack(pady=10, padx=20)

drawing_angle_lbl = LabelFrame(root, text="Drawing angle:")
drawing_angle_lbl.pack(pady=10)

drawing_angle = Entry(drawing_angle_lbl, font=("Helvetica", 15))
drawing_angle.pack(pady=10, padx=20)



my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Model", command=get_model)
my_button.grid(row=0, column=0, padx=10)



root.mainloop()




