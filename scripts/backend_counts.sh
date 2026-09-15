#!/bin/bash

LOG="/var/log/nginx/day3_access.log"

echo "Requests per backend:"
echo "---------------------"

awk '
{
    for (i = 1; i <= NF; i++) {
        if ($i ~ /^upstream_addr=/) {
            split($i, a, "=")

            if (a[2] != "-" && a[2] != "") {
                count[a[2]]++
            }
        }
    }
}
END {
    for (backend in count) {
        print backend, count[backend]
    }
}
' "$LOG" | sort
