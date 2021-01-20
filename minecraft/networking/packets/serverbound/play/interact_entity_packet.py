from minecraft.networking.packets import Packet
from minecraft.networking.types import (
    VarInt, Boolean, Float
)
from enum import IntEnum


class InteractEntityPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x0E

    class Type(IntEnum):
        INTERACT = 0
        ATTACK = 1
        INTERACT_AT = 2

    packet_name = 'interact entity'
    fields = ('entity_id', 'type', 'x', 'y', 'z', 'hand', 'sneaking')

    def read(self, file_object):
        self.entity_id = VarInt.read(file_object)
        self.type = Type(VarInt.read(file_object))
        if self.type == Type.INTERACT_AT:
            self.x = Float.read(file_object)
            self.y = Float.read(file_object)
            self.z = Float.read(file_object)
        if self.type == Type.INTERACT or self.type == Type.INTERACT_AT:
            self.hand = VarInt.read(file_object)
        self.sneaking = Boolean.read(file_object)

    def write_fields(self, packet_buffer):
        VarInt.send(self.entity_id, packet_buffer)
        VarInt.send(int(self.type), packet_buffer)
        if self.type == self.Type.INTERACT_AT:
            Float.send(x, packet_buffer)
            Float.send(y, packet_buffer)
            Float.send(z, packet_buffer)
        if self.type == self.Type.INTERACT or self.type == self.Type.INTERACT_AT:
            VarInt.send(self.hand, packet_buffer)
        Boolean.send(self.sneaking, packet_buffer)
