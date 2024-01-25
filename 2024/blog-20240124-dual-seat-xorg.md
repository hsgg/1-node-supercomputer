# Dual-Seat Xorg

With Wayland just around the corner, you may not want to hear about a cool
[Xorg](https://www.x.org/) feature. But it is so cool, hear me out. It needs
the `XI2` extension, which you probably already have.

On `X` you can create create two mouse pointers and two input keyboards, and
these act independently from each other. Here is how: First, you create a
virtual pair of *master* devices. Let's call that pair "Virtual second":

    $ xinput --create-master "Virtual second"

Then, you need to give it devices that will make those inputs move. Run
`xinput` to find out the IDs of the devices, then *reattach* the slaves to the
*masters*. In my case the new master pointer is id=15 and the master keyboard
is 16. The devices I want to attach are id=20 and id=22. So reattach them:

    $ xinput --reattach 20 15
    $ xinput --reattach 22 16

Viola! Enjoy the double-editing!

To tear it all down, remove the new masters:

    $ xinput --remove-master 15 AttachToMaster 2 3

where we explicitly asked to reattach the devices to the old master pointer
id=2 and master keyboard id=3.
