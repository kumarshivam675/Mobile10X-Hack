from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
import test

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read',   	messageProtocolEntity.getParticipant())
            
            inputMessage = messageProtocolEntity.getBody()
            
            x = messageProtocolEntity.isGroupMessage()
            print x
            if x is True:
                message = "Invalid Request"

                if inputMessage == "cab":
		            inputId = messageProtocolEntity.getParticipant()[2:12]
		            message = test.cabDetail(inputId) 

                outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    message,
                    to = messageProtocolEntity.getFrom())

                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
