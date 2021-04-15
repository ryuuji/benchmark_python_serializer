import json
import ujson
import pytest
import pickle
import zlib
import zstandard
import orjson
import msgpack
import simdjson


def load():
    with open('debug.json', 'r', encoding='utf-8') as f:
        data = f.read()
    return data


def load_as_json():
    return json.loads(load())


def encode_test(data):
    return data.encode('utf-8')


def compress_zlib(data):
    return zlib.compress(data)


def compress_zstd(data):
    cctx = zstandard.ZstdCompressor(level=5)
    return cctx.compress(data)


cctx2 = zstandard.ZstdCompressor(level=5)


def compress_zstd2(data):
    return cctx2.compress(data)


def test_loads_json(benchmark):
    data = load()
    ret = benchmark(json.loads, data)
    assert ret


def test_loads_ujson(benchmark):
    data = load()
    ret = benchmark(ujson.loads, data)
    assert ret


def test_loads_orjson(benchmark):
    data = load()
    ret = benchmark(orjson.loads, data)
    assert ret


def test_loads_msgpack(benchmark):
    data = msgpack.dumps(load_as_json())
    ret = benchmark(msgpack.loads, data)
    assert ret


def test_loads_simdjson(benchmark):
    data = load()
    ret = benchmark(simdjson.loads, data)
    assert ret


def test_dumps_json(benchmark):
    data = load_as_json()
    ret = benchmark(json.dumps, data)
    assert ret


def test_dumps_ujson(benchmark):
    data = load_as_json()
    ret = benchmark(ujson.dumps, data)
    assert ret


def test_dumps_orjson(benchmark):
    data = load_as_json()
    ret = benchmark(orjson.dumps, data)
    assert ret


def test_dumps_pickle(benchmark):
    data = load_as_json()
    ret = benchmark(pickle.dumps, data)
    assert ret


def test_dumps_msgpack(benchmark):
    data = load_as_json()
    ret = benchmark(msgpack.dumps, data)
    assert ret


def test_encode(benchmark):
    data = load()
    ret = benchmark(encode_test, data)
    assert ret


def test_compress_zlib(benchmark):
    data = load()
    ret = benchmark(compress_zlib, data.encode('utf-8'))
    assert ret


def test_compress_zstd(benchmark):
    data = load()
    ret = benchmark(compress_zstd, data.encode('utf-8'))
    assert ret


def test_compress_zstd2(benchmark):
    data = load()
    ret = benchmark(compress_zstd2, data.encode('utf-8'))
    assert ret


if __name__ == '__main__':
    data = load()
    print(len(data))
    x = compress_zlib(data.encode('utf-8'))
    print(len(x))
    x = compress_zstd(data.encode('utf-8'))
    print(len(x))
    pytest.main(['-v', __file__])
