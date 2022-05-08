import time
import rtmidi

compensation = .0002
tempo = 180
beat_length = 15/tempo + compensation
ideal_time = 15 / tempo
#beat_length = 15/tempo
next_beat = time.time() + beat_length
timeList = []
c = 0
average_list = []
difference_list = []


midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")


while True:
# Poll the time in 1ms increments until enough time has elapsed
    time1 = time.time()
    while time.time() < next_beat:
        time.sleep(.00001)

    next_beat += beat_length

    c += 1

    time2 = time.time() - time1
    timeList.append(time2)
    #print(time2)

    average = c * (ideal_time - (sum(timeList) / len(timeList)))
    # print(c *(15/tempo))
    #print(average)
    # print(sum(timeList))
    if len(timeList) % 10 == 0:
        if average < 0:
            time.sleep(-1 * average)

    #print(time.time())
    average_list.append(ideal_time - time2)
    #print(average_list)
    actual_time = (sum(average_list) / len(average_list))
    print(sum(average_list))



