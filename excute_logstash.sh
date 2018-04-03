#!/bin/sh
nohup /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/iot_test.conf &
