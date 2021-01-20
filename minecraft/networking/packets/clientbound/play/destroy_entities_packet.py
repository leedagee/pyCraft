from minecraft.networking.packets import Packet
from minecraft.networking.types import VarInt

class DestroyEntitiesPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x36 if context.protocol_later_eq(753) else \
               0x38 if context.protocol_later_eq(550) else \
               0x37 if context.protocol_later_eq(471) else \
               0x36 if context.protocol_later_eq(451) else \
               0x35 if context.protocol_later_eq(389) else \
               0x34 if context.protocol_later_eq(352) else \
               0x33 if context.protocol_later_eq(345) else \
               0x32 if context.protocol_later_eq(336) else \
               0x31 if context.protocol_later_eq(332) else \
               0x32 if context.protocol_later_eq(318) else \
               0x30 if context.protocol_later_eq(86) else \
               0x31 if context.protocol_later_eq(80) else \
               0x30 if context.protocol_later_eq(67) else \
               0x13

    packet_name = 'destroy entities'
    fields = ('length', "entities")

    def read(self, file_object):
        self.length = VarInt.read(file_object)
        self.entities = []
        for i in range(self.length):
            self.entities.append(VarInt.read(file_object))

    def write_fields(self, packet_buffer):
        VarInt.send(self.length, packet_buffer)
        for i in self.entities:
            VarInt.send(self.entities, packet_buffer)
