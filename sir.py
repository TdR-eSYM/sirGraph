import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import time

start_time = time.time()

fig, ax = plt.subplots()

plt.subplots_adjust(left=0.25, bottom=0.25)
ax.margins(x=0)

axamp = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor='lightgoldenrodyellow')
amp_slider = Slider(
    ax=axamp,
    label="Infection factor",
    valmin=0,
    valmax=1,
    valinit=0.75,
    orientation="vertical"
)
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
freq_slider = Slider(
    ax=axfreq,
    label='Recovery factor',
    valmin=0,
    valmax=1,
    valinit=1/3,
)

def simulate(val):

    k = freq_slider.val
    a = amp_slider.val
    
    s = []
    i = []
    r = []

    s.append(1)
    i.append(0.00001)
    r.append(0)

    timeStep = 1

    ran = 150

    for t in range(ran):
        sDt = -a * s[t] * i[t]
        sChange = sDt * timeStep
        s.append(s[t]+sChange)

        rDt = i[t] * k
        rChange = rDt * timeStep
        r.append(r[t]+rChange)

        iChange = -sChange - rChange
        i.append(i[t]+iChange)
    # I'm sorry
    ax.clear()
    ax.plot(s, label = "Susceptible")
    ax.plot(i, label = "Infected")
    ax.plot(r, label = "Removed")
    ax.legend()
#k = 1/3
#a = 0.75

print("Simulating...")
simulate(0)

amp_slider.on_changed(simulate)
freq_slider.on_changed(simulate)

ax.legend()
plt.show()
print("Done in " + str(round((time.time() - start_time)*1000, 2)) + " ms!")
