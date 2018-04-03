#!/bin/sh
nohup ./ffmpeg -re -stream_loop -1 -i /home/centos/boxing_cornor.mp4  -r 30 -g 60 -force_key_frames "expr:gte(t,n_forced*2.0)" -c:v copy -c:a copy -f flv "rtmp://localhost:1935/app01/hecas" &
