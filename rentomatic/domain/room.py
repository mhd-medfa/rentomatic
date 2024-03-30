import uuid
import dataclasses

@dataclasses.dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod
    def from_dict(self, init_dict):
        return self(**init_dict)

    def to_dict(self):
        # # Option 1: unpythonic
        # return {
        #         "code": self.code,
        #         "size": self.size,
        #         "price": self.price,
        #         "longitude": self.longitude,
        #         "latitude": self.latitude,
        #         }

        # Option 2:
        return dataclasses.asdict(self)


