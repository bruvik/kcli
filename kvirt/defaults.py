NETS = ['default']
POOL = 'default'
NUMCPUS = 2
MEMORY = 512
DISKINTERFACE = 'virtio'
DISKTHIN = True
DISKSIZE = 10
DISKS = [{'size': DISKSIZE}]
GUESTID = 'guestrhel764'
VNC = False
CLOUDINIT = True
RESERVEIP = False
START = True
EMULATOR = '/usr/bin/qemu-kvm'
IMAGES = ['http://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2']
