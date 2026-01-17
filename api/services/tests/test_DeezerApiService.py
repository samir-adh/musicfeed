from api.services.DeezerApiService import RecordData


class TestRecordData:
    def test_RecordData_create(self):
        record = RecordData(
            0,
            "title",
            "2025-01-01",
            "album"
        )

        assert record.record_id == 0
        assert record.title == "title"
        assert record.release_date == "2025-01-01"
        assert record.record_type == "album"