# Install Rosetta2 Manually

I've had a hard time finding this info, but finally I found a [video tutorial](https://www.youtube.com/watch?v=hlG_6Qz1nTw) that tells me how to install Rosetta2 manually on MacOS:

    $ softwareupdate --install-rosetta

Then, accept the licence agreement, and you are basically done.

Then, to launch programs like Mangle on the command line with Rosetta2,

    $ arch -x86_64 ./your-program
    
does NOT work. What gives?

As [this article](https://medium.com/@jithmisha/fix-for-macbook-air-m1-m2-bad-cpu-type-in-executable-error-3719a0a1cb6#:~:text=As%20it%20turns%20out%2C%20there,bit%20will%20cause%20this%20error.) explains, MacOS no longer supports 32-bit apps. 64-bit apps should work. So find a way to compile Mangle for 64-bit Intel, and you should be fine.
