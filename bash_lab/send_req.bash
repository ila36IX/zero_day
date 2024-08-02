#!/bin/env bash
# Send HEAD request method

printf "open getalien.tech 80 \nHEAD getalien.tech HTTP/1.0\n" | telnet
