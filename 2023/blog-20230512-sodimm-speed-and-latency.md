# How to check SO-DIMM speed and latency on linux

Speed is reported all over the place, but latency is harder to find. The tool
that worked for me was `decode-dimms` from the `i2c-tools` package.

    $ sudo decode-dimms

One memory bank was detected immediately. The other one was not detected until
I loaded the `eeprom` module (or was it the `ee1004` module?),

    $ sudo modprobe eeprom

There are a few more modules one might want to
[try](https://superuser.com/a/1499521/724366):

    $ sudo modprobe eeprom
    $ sudo modprobe at24
    $ sudo modprobe i2c-i801
    $ sudo modprobe i2c-amd-mp2-pci
    $ sudo modprobe ee1004

Oh, and CAS latency is usually reported in clock cycles.

Good luck!
