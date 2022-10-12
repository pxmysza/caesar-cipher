from functionality.rot_factory import RotFactory
from functionality.rot import Rot47, Rot13


class TestRotFactory:

    def test_get_rot_returns_correct_class_instance(self):
        assert isinstance(RotFactory.get_rot("rot13", "text"), Rot13)
        assert isinstance(RotFactory.get_rot("rot47", "text"), Rot47)


