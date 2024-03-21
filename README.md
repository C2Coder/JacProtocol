# JacProtocol

Python implementation of the comunication protocol used in Jaculus (https://jaculus.org)

## Installing



## Example code

```py
from jacprotocol import jp

jp.put(97) # ascii code for "a"
# or jp.put(ord("a"))
channel = 16 # mux channel - 16 is monitor/terminal

for b in jp.serialize(channel):
    out += f"{hex(b)}  "
print(out)
```

```py
from jacprotocol import jp
import serial # pip install pyserial

port = "/dev/ttyACM0"
baud = 921600

jp.put(97) # ascii code for "a"
# or jp.put(ord("a"))
channel = 16 # mux channel - 16 is monitor/terminal

# or if you want to send it over serial
with serial.Serial(port, baud, timeout=0) as ser:
    ser.write(jp.serialize(16))
```
