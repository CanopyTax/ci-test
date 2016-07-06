from source.core import decode


def test_decode():
    json_dict = decode("""
    {
        "array": [
            1,
            2,
            3
        ],
        "boolean": true,
        "null": null,
        "number": 123,
        "object": {
            "a": "b",
            "c": "d",
            "e": "f"
        },
        "string": "Hello World"
    }
    """
           )
    assert 'number' in json_dict
    assert json_dict['number'] == 123