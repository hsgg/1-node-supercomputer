# `inotifywait`

Sometimes you want to wait on a file change, and then do something.

For example, you modify a source code file, and whenever you save, you want to
compile.

`inotifywait` from the
[`inotify-tools`](https://github.com/inotify-tools/inotify-tools/wiki) package
to the rescue!

However, it only outputs that something changed, so pipe the output to clear
the terminal and call `make`:

    inotifywait -m -e close_write *.ly *.ily |
    while read line; do clear; make; done

The `-m` option says to keep monitoring, `-e close_write` monitors for programs
closing a file that had been opened for writing, and `*.ly *.ily` are the file
patterns to monitor.

There is also `fsnotifywait` and `fsnotifywatch` and `inotifywatch`. One day I
will find out the difference.
