import sys
import struct

b = sys.stdin.buffer.read()
L = len(b)

Size = struct.unpack("i", b[4:8])[0]
Type = struct.unpack("h", b[20:22])[0]
Channels = struct.unpack("h", b[22:24])[0]
Rate = struct.unpack("i", b[24:28])[0]
Bits = struct.unpack("h", b[34:36])[0]
Data_size = struct.unpack("i", b[40:44])[0]

if L < 44 or b[:4] != b"RIFF" or Size != L - 8 or b[8:12] != b"WAVE" or b[12:16] != b"fmt " \
    or struct.unpack("i", b[16:20])[0] != 16 or (Rate != 44100 and Rate != 48000) or \
    struct.unpack("i", b[28:32])[0] != (Rate * Bits * Channels) / 8 or struct.unpack("h", b[32:34])[0] != \
    (Bits * Channels) / 8 or struct.unpack("h", b[32:34])[0] not in {1, 2, 4} or b[36:40] != b"data" or \
    Data_size != Size - 36:
    print("NO")
else:
    print(f"Size={Size}, Type={Type}, Channels={Channels}, Rate={Rate}, Bits={Bits}, Data size={Data_size}")
