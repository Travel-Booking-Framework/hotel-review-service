import grpc
from generated import hotel_pb2, hotel_pb2_grpc

class HotelClient:
    def get_hotel_details(self, hotel_id):
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = hotel_pb2_grpc.HotelServiceStub(channel)
            response = stub.GetHotelDetails(hotel_pb2.HotelDetailRequest(hotel_id=hotel_id))
            return response