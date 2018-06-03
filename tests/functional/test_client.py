# -*- coding: utf-8 -*-
# Copyright (c) 2018 Jan Ferko <julyloov@gmail.com>
#
# this file is part of the project "Http Dustman" released under the "MIT" open-source license
import json
import httpretty

from dustman import HttpBinClient


@httpretty.httprettified
def test_httpbinclient_post():
    ("HttpBinClient.post() should return a dict with deserialized JSON data")

    # Given that I fake a response from httpbin.org
    httpretty.register_uri(
        httpretty.POST,
        'https://httpbin.org/post',
        body=json.dumps({
            "this": "is",
            "a fake": "JSON response"
        })
    )

    # And an instance of HttpBinClient
    client = HttpBinClient()

    # When I call .post()
    result = client.post()

    # Then it should return a dict
    result.should.equal({
        "this": "is",
        "a fake": "JSON response",
    })


@httpretty.httprettified
def test_httpbinclient_get_ip():
    ("HttpBinClient.ip() should return the origin ip address")

    # Given that I fake a response from httbin.org
    httpretty.register_uri(
        httpretty.GET,
        "https://httpbin.org/ip",
        body=json.dumps({
            "origin": "147.32.232.146"
        })
    )

    client = HttpBinClient()

    # When I call ip()
    result = client.ip()

    # Then it should return a IP address as string
    result.should.equal("147.32.232.146")
