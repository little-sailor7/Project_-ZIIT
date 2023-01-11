#!/bin/bash

grep -a "HTTP" /var/log/apache2/access.log | awk '{print $1}' | sort | uniq -c > HTTP_IPIES.txt