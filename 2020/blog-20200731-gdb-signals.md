# GDB signals

When debugging with `gdb`, not all signals are important enough to warrant
stopping the program. For example, the X server establishes a pipe with a
client, and when that client dies, the pipe may break before the X server got
notice of the death of the client. In that case the X server receives a
`SIGPIPE` signal, which should just be ignored.

What exactly `gdb` should do with such a signal can be set with the `handle`
command, e.g.,

	gdb> handle SIGPIPE nostop

That will tell `gdb` not to stop the program just because a client quit, and
you can focus your attention on real problems.
