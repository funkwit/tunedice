tunedice
========

Tools for managing person-specific music dirs.

Used for building directories for a single person's 'slice' of a master shared music directory, suitable for
uploading to a music locker service (Amazon or Google Music, for example).

Works by creating a '.dice' file specifying whether an individual cares about the music in a given directory (or
subdirectory). '.dice' can contain either a user's name, if they want that music uploaded to their locker, or !name,
if they don't.

For example, given:
```
   .
   ./Allo Darlin
   ./Allo Darlin/.dice
   ./Allo Darlin/Allo Darlin
   ./Allo Darlin/Europe
   ./Los Campesinos
   ./Los Campesinos/Romance is Boring
   ./Los Campesinos/Romance is Boring/.dice
   ./Los Campesinos/Sticking Fingers Into Sockets
   ./Sin Fang
   ./Sin Fang/.dice
   ./Sin Fang/Flowers
   ./Sin Fang/Summer Echoes
   ./Widowspeak
   ./Widowspeak/Almanac
   ./Widowspeak/Widowspeak
$ cat ./Allo\ Darlin/.dice
john
$ cat ./Los\ Campesinos/Romance\ is\ Boring/.dice
john
$ cat ./Sin\ Fang/.dice
!john
```

Then it is assumed:
* john wants ALL of Allo Darlin/ uploaded to his locker
* john wants NONE of Sin Fang uploaded to his locker
* john has NOT YET DECIDED about any albums of Widowspeak.
* john wants the 'Romance is Boring' album ONLY of Los Campesinos uploaded to his locker; he has not yet decided about the 'Sticking Fingers Into Sockets' album.

For john to check what music he has not yet decided about:
```
$ tunedice/checker.py --user=john /music
Missing: /music/Los Campesinos/Sticking Fingers Into Sockets
Missing: /music/Widowspeak/Almanac
Missing: /music/Widowspeak/Widowspeak
```

John should create new .dice files in each folder specified (or the level up, if he wants to make a bulk decision about
an artist).
