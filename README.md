# dailyprogrammer
A collection of solutions to challenges posted on https://reddit.com/r/dailyprogrammer

* [321 [Easy] Talking Clock](#321-easy-talking-clock)
* [333 [Easy] Packet Assembler](#333-easy-packet-assembler)

## 321 [Easy] Talking Clock

### Description
[Challenge Thread](https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/)

No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're never late again. A talking clock takes a 24-hour time and translates it into words. 

### Solution notes
Uses the [inflect](https://pypi.python.org/pypi/inflect/0.2.5) package to convert numbers to words.

## 333 [Easy] Packet Assembler

### Description
[Challenge Thread](https://www.reddit.com/r/dailyprogrammer/comments/72ivih/20170926_challenge_333_easy_packet_assembler/)

When a message is transmitted over the internet, it is split into multiple packets, each packet is transferred individually, and the packets are reassembled into the original message by the receiver. Because the internet exists in the real world, and because the real world can be messy, packets do not always arrive in the order in which they are sent. For today's challenge, your program must collect packets from stdin, assemble them in the correct order, and print the completed messages to stdout.

The point of reading from stdin is to simulate incoming packets. For the purposes of this challenge, assume there is a potentially unlimited number of packets. Your program should not depend on knowing how many packets there are in total. Simply sorting the input in its entirety would technically work, but defeats the purpose of this exercise.

### Solution Notes
This is my first attempt at a dailyprogrammer challenge. I based it on a help comment posted in the thread.


