from guizero import App, Text, PushButton, Box

def reset():
    print("reset")

def timer25():
    print("25")

def timer5():
    print("5")    

def timer15():
    print("15")

app = App(title="Timer", width=300, height=150)

timer_box = Box(app, width="fill", align="top", )
timer_text = Text(timer_box, align="left", text="00:00", size=40)

counter_box = Box(timer_box, align="right")
counter_text = Text(counter_box, align="left", text="0", size=30)
rst_btn = PushButton(counter_box, align="right", text="RST")

control_box = Box(app, layout="grid", align="bottom")
timer25_btn = PushButton(control_box, grid=[0,0], text="25", padx=30, pady=20)
timer5_btn = PushButton(control_box, grid=[1,0], text="5", padx=30, pady=20, command=timer5)
timer15_btn = PushButton(control_box, grid=[2,0], text="15", padx=30, pady=20)

app.display()