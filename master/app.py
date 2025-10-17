from customtkinter import *
import data_func as df
import sound as s
from PIL import Image


class ToplevelWindow(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transient(root)
        self.resizable(False, False)

        self.confirm_label = CTkLabel(
            self, text='u sure?', font=('impact', 40))
        self.deny_button = CTkButton(self, text='Na', font=('impact', 20), width=100,
                                     height=60, corner_radius=0, border_width=2,
                                     border_color="#490000", fg_color="#B90E0E",
                                     hover_color="#490000", command=self.destroy)
        self.conf_button = CTkButton(self, text='Yuh', font=('impact', 20), width=100, height=60,
                                     corner_radius=0, border_width=2,
                                     border_color="#004e2a", fg_color="#00b661",
                                     hover_color="#004e2a",
                                     command=lambda: (df.clear_data(), display_update(), self.destroy()))

        self.confirm_label.grid(
            column=0, row=0, columnspan=2, padx=100, pady=30)
        self.deny_button.grid(column=0, row=1)
        self.conf_button.grid(column=1, row=1)


class SpookWindow(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transient(root)
        self.geometry('200x300')
        self.resizable(False, False)

        if DoubleVar.get(current) < 80:
            spooky = CTkImage(light_image=Image.open(
                '.\\spook.png'), size=(200, 300))
        else:
            spooky = CTkImage(light_image=Image.open(
                '.\\spook2.png'), size=(200, 300))

        self.spook_label = CTkLabel(
            self, text='', image=spooky).place(relx=0.5, rely=0.5, anchor='center')

        self.spook_button = CTkButton(self, text='i\'m shook', font=(
            'Impact', 20), text_color="#000000", corner_radius=0, border_width=3, hover_color="#9B9B9B",
            border_color="#9B9B9B", fg_color="#D6D6D6", command=self.destroy)
        self.spook_button.place(relx=0.5, rely=0.9, anchor='center')


def spookie():
    global spook_window
    if spook_window is None or not spook_window.winfo_exists():
        spook_window = SpookWindow(root)
        spook_window.focus()
    else:
        spook_window.focus()


def open_confirmbox():
    global toplevel_window
    if toplevel_window is None or not toplevel_window.winfo_exists():
        toplevel_window = ToplevelWindow(root)
        toplevel_window.focus()
    else:
        toplevel_window.focus()


def display_update():
    DoubleVar.set(current, df.current_weight_avg())
    current_display.configure(text=DoubleVar.get(current))
    DoubleVar.set(weight, 0.0)
    DoubleVar.set(
        weight_change, round((df.current_weight_avg() - df.last_week_avg()), 2))
    weight_change_display.configure(text=DoubleVar.get(weight_change), border_color=wc_color2(),
                                    fg_color=wc_color1(), hover_color=wc_color2())


# root setup
root = CTk()
root.title('weight tracker')
set_appearance_mode("dark")
root.resizable(False, False)

# var setup
weight = DoubleVar()
weight_change = DoubleVar()
current = DoubleVar()
last_week = DoubleVar()
week_before = DoubleVar()
toplevel_window = None
spook_window = None

DoubleVar.set(current, df.current_weight_avg())
DoubleVar.set(last_week, df.last_week_avg())
DoubleVar.set(week_before, df.week_before_avg())
DoubleVar.set(weight_change, round(
    (df.current_weight_avg() - df.last_week_avg()), 2))

# week before display setup
wbd_color1 = "#B90E0E"
wbd_color2 = "#490000"
week_before_display = CTkButton(root, text=DoubleVar.get(week_before),
                                font=('impact', 40), width=150, height=150, corner_radius=0,
                                border_width=2, border_color=wbd_color2, fg_color=wbd_color1,
                                hover_color=wbd_color2, command=lambda: (s.playsound(), spookie()))
week_before_label = CTkLabel(root, text='Week before avg', font=('impact', 20))


# last week display setup
lwd_color1 = "#ca5203"
lwd_color2 = "#6E2800"
last_week_display = CTkButton(root, text=DoubleVar.get(last_week),
                              font=('impact', 40), width=150, height=150, corner_radius=0,
                              border_width=2, border_color=lwd_color2, fg_color=lwd_color1,
                              hover_color=lwd_color2, command=lambda: (s.playsound(), spookie()))
last_week_label = CTkLabel(root, text='Last week avg', font=('impact', 20))


# current weight display setup
cd_color1 = "#D1B200"
cd_color2 = "#664e00"
current_display = CTkButton(
    root, text=DoubleVar.get(current), font=('impact', 40), width=150,
    height=150, corner_radius=0, border_width=2, border_color=cd_color2,
    fg_color=cd_color1, hover_color=cd_color2, command=lambda: (s.playsound(), spookie()))
current_label = CTkLabel(root, text='Current avg', font=('impact', 20))


# weight change setup
def wc_color1():
    if (0.5 >= DoubleVar.get(weight_change) >= -0.5):
        return "#00b661"
    else:
        return "#b80028"


def wc_color2():
    if (0.5 >= DoubleVar.get(weight_change) >= -0.5):
        return "#004e2a"
    else:
        return "#630015"


weight_change_display = CTkButton(root, text=DoubleVar.get(weight_change),
                                  font=('impact', 40), width=100, height=100, corner_radius=0,
                                  border_width=2, border_color=wc_color2(), fg_color=wc_color1(),
                                  hover_color=wc_color2(), command=lambda: (s.playsound(), spookie()))
weight_change_label = CTkLabel(
    root, text='weekly weight change \n ( red bad )', font=('impact', 20))


# input setup
bt_color1 = "#E6E6E6"
bt_color2 = "#9B9B9B"
insert_button = CTkButton(root, text='Input weight', text_color="#000000", font=('impact', 20),
                          corner_radius=0, border_width=2, hover_color=bt_color2,
                          border_color=bt_color2, fg_color=bt_color1,
                          command=lambda: (df.insert(DoubleVar.get(weight)), display_update()))

weight_in = CTkEntry(root, textvariable=weight, font=('impact', 20))


# clear database box
cbt_color1 = "#D6D6D6"
cbt_color2 = "#9B9B9B"
cleardata_bt = CTkButton(root, text='Clear data', text_color="#000000", font=('impact', 20),
                         corner_radius=0, border_width=2, hover_color=cbt_color2,
                         border_color=cbt_color2, fg_color=cbt_color1,
                         command=open_confirmbox)


# grid setup
week_before_display.grid(column=0, row=0)
last_week_display.grid(column=1, row=0)
current_display.grid(column=2, row=0)
week_before_label.grid(column=0, row=1)
last_week_label.grid(column=1, row=1)
current_label.grid(column=2, row=1)
weight_change_display.grid(column=0, row=2, columnspan=3, pady=(40, 0))
weight_change_label.grid(column=0, row=3, columnspan=3)
insert_button.grid(column=0, row=4, columnspan=2, pady=40)
weight_in.grid(column=1, row=4, columnspan=2)
cleardata_bt.grid(column=0, row=5, columnspan=3, pady=(40, 10))

root.mainloop()
