import unittest
from data_validation_module import validate_album_data

class TestDataValidation(unittest.TestCase):
    def test_valid_album_data(self):
        # Test with valid album data
        album_data = {
            "album_name": "Sample Album",
            "artist": "Sample Artist",
            "release_date": "2022-01-01",
        }
        self.assertTrue(validate_album_data(album_data))

    def test_missing_album_name(self):
        # Test when album name is missing
        album_data = {
            "artist": "Sample Artist",
            "release_date": "2022-01-01",
        }
        self.assertFalse(validate_album_data(album_data))

    def test_missing_artist(self):
        # Test when artist is missing
        album_data = {
            "album_name": "Sample Album",
            "release_date": "2022-01-01",
        }
        self.assertFalse(validate_album_data(album_data))

    def test_invalid_release_date(self):
        # Test with an invalid release date
        album_data = {
            "album_name": "Sample Album",
            "artist": "Sample Artist",
            "release_date": "2022-99-99",  # Invalid date format
        }
        self.assertFalse(validate_album_data(album_data))

    def test_empty_data(self):
        # Test with empty data
        album_data = {}
        self.assertFalse(validate_album_data(album_data))

if __name__ == '__main__':
    unittest.main()
