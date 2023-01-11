grep -o -a "sshd"  /var/log/auth.log | uniq > Service.txt
grep -o -a "HTTP" /var/log/apache2/access.log | uniq >> Service.txt
grep -a "Accepted password" /var/log/auth.log | grep -oE '[-1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | sort | uniq -c > Accepted_ipies.txt
grep -a sshd  /var/log/auth.log | grep -a "(sshd:auth)" | grep -oE -a '[-1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | sort | uniq -c > Rejected_ipies.txt
