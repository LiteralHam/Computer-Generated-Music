# Computer-Generated-Music
A program to generates a single line of musical notes within limiting parameters designed to mimic european classical style melodies  
I'm new to programming and this was an idea I had while learning about loops and lists  

## Current parameters  
+ Randomly chooses note-lengths to assemble self-contained measures of notes and rests in 4/4 time signature
  - Note lengths are whole, half, quarter, eighth and 16th
+ Randomly chooses notes within C major scale with octave range A4 to G5 (2 octaves)
  - Intervals between adjacent notes are limited to no more than 3.5 steps
    - This is consistent between measures
    - This is consistent between notes separated by one or more rest
  - Intervals of exactly 3 steps (a tritone) are filtered out
    - Note: tritones are uncommon in classical western music melodies except in specific circumstances and parts of chords. It's considered by western music theory to be dissonant and unpleasant. 
+ Outputs text in a list of tuples. Format: [(A5, 0.5), (B5, 0.0625), (rest, 0.125]
  - Output is a single list with no marker for where measures begin and end
  - Output is always 4 measures worth of melody

## Features I want to create
+ Allow user to specify how many measures of music
+ Take into account frequency/probability of different notes appearing in a sampling of real classical music
+ In current generated music 16th notes and rests are over-represented
+ Could also take into account frequency of notes appearing based on solfege (do, re, mi...)
+ Include possibility for repeats
+ Highly favor last note of 4th or 16th measures to be Do to resolve melody

## Features I don't know where to begin to create
+ Allow user to specify key, time signature
+ Write in a format that can be read or export directly as an XML, MIDI, or other file that can go directly into a DAW
+ Use dotted note lengths  
+ Use counterpoint to create 4-part music
+ Use whole musical scale
+ Mimic more specific styles
