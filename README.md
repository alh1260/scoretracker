# Score tracker
## A dumb little utility to calculate balanced PAF scores

### About
This is a thing that I wrote back in 2017 because I was tired of balancing
peer-assessment factor (PAF) scores in my head, and at that time I was
pretty much doing a group project every semester, so you can see why I
wrote something like this.

The concept is simple: specify your teammates (including yourself), then
enter a maximum score. After that you can update individual scores and
the utility will automatically adjust the others so that all scores still
add up to the maximum.

I've decided to finally upload this because I felt like this needed to be 
shared.

### Requirements

Python 3.4+

### Usage

Invocation: `./tracker.py <member1> <member2> [<member3> [...]]`
Where each member is the name of a particular teammate (no spaces)

Commands:
`update <member> <value>`
Update a particular member's score.

`quit`
Exit the program

### Limitations

The returned scores are floating point numbers rather than straight
integers, so some manual rounding is still required.
