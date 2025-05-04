from smbus2 import SMBus

with SMBus(1) as bus:
    # Read a block of 16 bytes from address 80, offset 0
    block = bus.read_i2c_block_data(0x53, 0, 32)
    # Returned value is a list of 16 bytes
    print(' '.join(f'{x:02x}' for x in block))
    block = bus.read_i2c_block_data(0x53, 31, 32)
    print(' '.join(f'{x:02x}' for x in block))
    block = bus.read_i2c_block_data(0x53, 63, 32)
    print(' '.join(f'{x:02x}' for x in block))
    block = bus.read_i2c_block_data(0x53, 95, 32)
    print(' '.join(f'{x:02x}' for x in block))
    block = bus.read_i2c_block_data(0x53, 127, 32)
    print(' '.join(f'{x:02x}' for x in block))
    block = bus.read_i2c_block_data(0x53, 159, 32)
    print(' '.join(f'{x:02x}' for x in block))
    block = bus.read_i2c_block_data(0x53, 191, 32)
    print(' '.join(f'{x:02x}' for x in block))
    block = bus.read_i2c_block_data(0x53, 223, 32)
    print(' '.join(f'{x:02x}' for x in block))
