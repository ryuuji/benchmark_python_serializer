import json
import ujson
import pytest
import pickle
import zlib
import zstandard
import orjson
import msgpack


def loads_json():
    with open('search.json', 'r', encoding='utf-8') as f:
        return json.loads(f.read())


def loads_ujson():
    with open('search.json', 'r', encoding='utf-8') as f:
        return ujson.loads(f.read())


def loads_orjson():
    with open('search.json', 'rb') as f:
        return orjson.loads(f.read())


def dumps_json(data):
    return json.dumps(data)


def dumps_ujson(data):
    return ujson.dumps(data, ensure_ascii=False, sort_keys=False, escape_forward_slashes=False)


def dumps_orjson(data):
    return orjson.dumps(data)


def dumps_pickle(data):
    return pickle.dumps(data)


def dumps_msgpack(data):
    return msgpack.dumps(data)


def encode_test(data):
    return data.encode('utf-8')


def compress_zlib(data):
    return zlib.compress(data)


def compress_zstd(data):
    cctx = zstandard.ZstdCompressor(level=5)
    return cctx.compress(data)


def test_loads_json(benchmark):
    ret = benchmark(loads_json)
    assert ret


def test_loads_ujson(benchmark):
    ret = benchmark(loads_ujson)
    assert ret


def test_loads_orjson(benchmark):
    ret = benchmark(loads_orjson)
    assert ret


def test_dumps_json(benchmark):
    data = loads_json()
    ret = benchmark(dumps_json, data)
    assert ret


def test_dumps_ujson(benchmark):
    data = loads_json()
    ret = benchmark(dumps_ujson, data)
    assert ret


def test_dumps_orjson(benchmark):
    data = loads_json()
    ret = benchmark(dumps_orjson, data)
    assert ret


def test_dumps_pickle(benchmark):
    data = loads_json()
    ret = benchmark(dumps_pickle, data)
    assert ret


def test_dumps_msgpack(benchmark):
    data = loads_json()
    ret = benchmark(dumps_msgpack, data)
    assert ret


def test_encode(benchmark):
    data = loads_ujson()
    data = dumps_ujson(data)
    ret = benchmark(encode_test, data)
    assert ret


def test_compress_zlib(benchmark):
    data = loads_ujson()
    data = dumps_ujson(data)
    ret = benchmark(compress_zlib, data.encode('utf-8'))
    assert ret


def test_compress_zstd(benchmark):
    data = loads_ujson()
    data = dumps_ujson(data)
    ret = benchmark(compress_zstd, data.encode('utf-8'))
    assert ret


if __name__ == '__main__':
    data = loads_ujson()
    data = dumps_ujson(data)
    print(len(data))
    x = compress_zlib(data.encode('utf-8'))
    print(len(x))
    x = compress_zstd(data.encode('utf-8'))
    print(len(x))
    pytest.main(['-v', __file__])
