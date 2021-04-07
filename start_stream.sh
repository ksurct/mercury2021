#!/bin/bash

raspivid -o - -t 0 -rot 180 -w 1920 -h 1080 -fps 30 -b 2000000 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream}' :demux=h264
