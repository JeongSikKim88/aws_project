#!/bin/sh
nohup ./ffmpeg -re -stream_loop -1 -i /home/jack/boxing_cornor.mp4  -r 30 -g 60 -force_key_frames "expr:gte(t,n_forced*2.0)" -c:v copy -c:a libfdk_aac -b:a 128k -ar 44100 -f mpegts "udp://localhost:12345?pkt_size=1316" &
