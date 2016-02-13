from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity
import test
import nearbypubs
import nearbyhospitals
import complaint


class EchoLayer(YowInterfaceLayer):
    status = "continue"
    url = ""
    caption = ""
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        # send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(),
                                                    'read', messageProtocolEntity.getParticipant())

            x = messageProtocolEntity.isGroupMessage()
            print x
            if x is True:
                if messageProtocolEntity.getType() == "text":
                    message = "Invalid Request"
                    input = messageProtocolEntity.getBody()
                    inputList = input.split(' ')
                    print inputList, len(inputList)
                    inputMessage = inputList[0]

                    message = "Invalid Format"

                    if inputMessage == "@cab":
                        inputId = messageProtocolEntity.getParticipant()[2:12]
                        message = test.cabDetail(inputId)

                    elif inputMessage == "@help":
                        message = "@cab: to get cab details \n@hospital: to get hospitals nearby \n@hotels: to get pubs nearby \n"


                    elif inputMessage == "@hotels" and len(inputList) == 1:
                        self.status = "hotels_origin"
                        message = "Please send your location"

                    elif inputMessage == "@hospital" and len(inputList) == 1:
                        self.status = "hospital_origin"
                        message = "Please send your location"

                    elif inputMessage == "@complaint":
                        self.status = "complaint_image"
                        message = "Please Upload the image"

                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                        message,
                        to=messageProtocolEntity.getFrom())

                    self.toLower(receipt)
                    self.toLower(outgoingMessageProtocolEntity)
                elif messageProtocolEntity.getType() == "media":
                    message = ""
                    if messageProtocolEntity.getMediaType() == "location":
                        if self.status == "distance_destination":
                            message = "Distance to majestic is 20.8 km.\n Expected Commute time is 55 mins"
                            self.status == "waiting"
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()

                        elif self.status == "hotels_origin":
                            ans = nearbypubs.waypoints([messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()])
                            print len(ans)
                            k = 1
                            for i in ans:
                                message += str(k) + ". " +i[0] + ", Rating: " + str(i[1]) + "\n"
                                k += 1
                            self.status = "continue"
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()

                        elif self.status == "hospital_origin":
                            ans = nearbyhospitals.waypoints([messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()])
                            print len(ans)
                            k = 1
                            for i in ans:
                                message += str(k) + ". " +i + "\n"
                                k += 1
                            self.status = "continue"
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()

                        elif self.status == "complaint_location":
                            complaint.complaintLodge(messageProtocolEntity.getLatitude(),messageProtocolEntity.getLongitude(), self.url,self.caption)
                            self.status = "continue"
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()
                            message = "Complaint received. Thanks"

                        print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()

                    elif messageProtocolEntity.getMediaType() == "image":
                        if self.status == "complaint_image":
                            self.url = messageProtocolEntity.getMediaUrl()
                            self.caption = messageProtocolEntity.getCaption()
                            self.status = "complaint_location"
                            message = "Image received. Please send your location"

                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                            message,
                            to=messageProtocolEntity.getFrom())

                    self.toLower(receipt)
                    self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
