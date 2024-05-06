from guizero import App, Text, PushButton, Box
from gpiozero import CPUTemperature

SEC = 60

timer_running = False
should_count = True

def update_temp():
    cpu_temp = str(CPUTemperature().temperature);
    temp_text.value =  cpu_temp + "'C"

def reset_counter():
    counter_text.value = 0

def stop_timer():
    global timer_running
    global should_count
    
    timer_text.cancel(reduce_time)
    timer_running = False
    timer_text.value = 0
    
    if(should_count):
        counter_text.value = int(counter_text.value) + 1
        should_count = False

cpu = CPUTemperature()

def reduce_time():
    val = int(timer_text.value)
    if(val > 0):
        timer_text.value = val - 1
    else:
        stop_timer()

def timer(mins):
    global timer_running
    global should_count
    
    if(timer_running):
        should_count = False
        stop_timer()
        return
    
    timer_running = True
    timer_text.value = mins
    timer_text.repeat(1000*SEC, reduce_time)

def timer25():
    global should_count

    should_count = True
    timer(25)

def timer5():
    timer(5)

def timer15():
    timer(15)

app = App(title="Timer", width=300, height=150)

temp_box = Box(app, width="fill", align="top")
temp_text = Text(temp_box, align="right", text=str(cpu.temperature) + "'C", size=20)
temp_text.repeat(5* 60 *1000, update_temp)

timer_box = Box(app, width="fill", align="top")
timer_text = Text(timer_box, align="left", text="0", size=40)

counter_box = Box(timer_box, align="right")
counter_text = Text(counter_box, align="left", text="0", size=30)
rst_btn = PushButton(counter_box, align="right", text="RST", command=reset_counter)

control_box = Box(app, layout="grid", align="bottom")
timer25_btn = PushButton(control_box, grid=[0,0], text="25", padx=30, pady=20, command=timer25)
timer5_btn = PushButton(control_box, grid=[1,0], text="5", padx=30, pady=20, command=timer5)
timer15_btn = PushButton(control_box, grid=[2,0], text="15", padx=30, pady=20, command=timer15)

app.display()