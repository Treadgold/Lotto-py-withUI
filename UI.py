import customtkinter as ctk
import newlotto


class App:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.configure(fg_color=('light grey', 'blue'))
        self.master.geometry("680x600")
        self.master.resizable(False, False)
        self.master.wm_title("Lotto Number Generator")
        self.row_number: str = '10'
        self.balls_drawn: str = '6'
        self.max_ball_number: str = '40'
        self.powerball: str = '10'
        slider_pos = .3
        label_font = ("Arial", 14, "bold")

        # create the rows number label
        self.rows_label = ctk.CTkLabel(
            self.master,
            text=f"number of rows {self.row_number}",
            font=label_font)
        self.rows_label.place(relx=slider_pos, rely=0.1, anchor="e")
        # Create the rows slider
        slider_rows = ctk.CTkSlider(self.master,
                                    from_=1,
                                    to=30,
                                    number_of_steps=29,
                                    command=self.slider_rows_event)
        slider_rows.place(relx=slider_pos, rely=0.2, anchor="e")
        slider_rows.set(int(self.row_number))

        # create the number of balls drawn label
        self.balls_drawn_label = ctk.CTkLabel(
            self.master,
            text=f"balls to draw {self.balls_drawn}",
            font=label_font)
        self.balls_drawn_label.place(relx=slider_pos, rely=0.3, anchor="e")
        # Create the number of balls drawn slider
        slider_balls_drawn = ctk.CTkSlider(
            self.master,
            from_=4,
            to=9,
            number_of_steps=5,
            command=self.slider_balls_drawn_event)
        slider_balls_drawn.place(relx=slider_pos, rely=0.4, anchor="e")
        slider_balls_drawn.set(int(self.balls_drawn))

        # create the max ball number label
        self.max_ball_number_label = ctk.CTkLabel(
            self.master,
            text=f"max ball number {self.max_ball_number}",
            font=label_font)
        self.max_ball_number_label.place(relx=slider_pos, rely=0.5, anchor="e")
        # Create the max ball number slider
        slider_max_ball_number = ctk.CTkSlider(
            self.master,
            from_=12,
            to=99,
            number_of_steps=87,
            command=self.slider_max_ball_number_event)
        slider_max_ball_number.place(relx=slider_pos, rely=0.6, anchor="e")
        slider_max_ball_number.set(int(self.max_ball_number))

        # create the powerball label
        self.powerball_label = ctk.CTkLabel(
            self.master,
            text=f"powerball max {self.powerball}",
            font=label_font)
        self.powerball_label.place(relx=slider_pos, rely=0.7, anchor="e")
        # Create the powerball slider
        slider_powerball = ctk.CTkSlider(self.master,
                                         from_=0,
                                         to=99,
                                         number_of_steps=100,
                                         command=self.slider_powerball_event)
        slider_powerball.place(relx=slider_pos, rely=0.8, anchor="e")
        slider_powerball.set(int(self.powerball))

        # Create the button
        self.button = ctk.CTkButton(self.master,
                                    text="Generate Numbers",
                                    command=self.populate_box,
                                    corner_radius=10,
                                    font=label_font)
        self.button.place(relx=slider_pos, rely=0.9, anchor="e")

        # create the text box
        self.text_box = ctk.CTkTextbox(self.master,
                                       border_spacing=25,
                                       width=450,
                                       height=500,
                                       font=("Courier bold", 23),
                                       text_color='Black',
                                       corner_radius=10,
                                       fg_color='grey')
        self.text_box.place(relx=0.98, rely=0.5, anchor="e")

    def slider_rows_event(self, value):
        self.row_number = str(int(value))
        self.rows_label.configure(text=f"number of rows {self.row_number}")

    def slider_balls_drawn_event(self, value):
        self.balls_drawn = str(int(value))
        self.balls_drawn_label.configure(
            text=f"balls to draw {self.balls_drawn}")

    def slider_max_ball_number_event(self, value):
        self.max_ball_number = str(int(value))
        self.max_ball_number_label.configure(
            text=f"max ball number {self.max_ball_number}")

    def slider_powerball_event(self, value):
        self.powerball = str(int(value))
        self.powerball_label.configure(text=f"powerball max {self.powerball}")

    def populate_box(self):
        self.text_box.delete("1.0", "100.0")

        # Get the figures from the sliders
        final_lines = newlotto.get_lines(int(self.row_number),
                                         int(self.max_ball_number),
                                         int(self.balls_drawn),
                                         int(self.powerball))

        # loop through the lines and add them to the text box

        for y, line in enumerate(final_lines):
            # check result as tuple will have powerball, else just normal line

            if type(line) is tuple:

                final_line = ""
                j = ", "
                # loop through the list and add the comma

                for item in line[0]:
                    if item == line[0][-1]:
                        j = ""
                    final_line += item + j
                # add the powerball to the end of the line
                final_line += ", (" + line[1] + ")"

                # add the line to the text box
                self.text_box.insert("0.0", final_line + "\n")

            else:
                # same as above, just no powerball so no tuple
                final_line = ""
                j = ", "
                for item in line:
                    if item == line[-1]:
                        j = ""
                    final_line += item + j
                self.text_box.insert("0.0", final_line + "\n")
        pass


if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()
