# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio2video.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61udio2video.proto\x12\x1avideo_from_audio_generator\"\"\n\x0c\x41udioRequest\x12\x12\n\naudio_data\x18\x01 \x01(\x0c\"#\n\rVideoResponse\x12\x12\n\nvideo_data\x18\x01 \x01(\x0c\"\x14\n\x12HealthCheckRequest\"%\n\x13HealthCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xf0\x01\n\x17VideoFromAudioGenerator\x12\x65\n\x0eVideoFromAudio\x12(.video_from_audio_generator.AudioRequest\x1a).video_from_audio_generator.VideoResponse\x12n\n\x0b\x43heckHealth\x12..video_from_audio_generator.HealthCheckRequest\x1a/.video_from_audio_generator.HealthCheckResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'audio2video_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_AUDIOREQUEST']._serialized_start=49
  _globals['_AUDIOREQUEST']._serialized_end=83
  _globals['_VIDEORESPONSE']._serialized_start=85
  _globals['_VIDEORESPONSE']._serialized_end=120
  _globals['_HEALTHCHECKREQUEST']._serialized_start=122
  _globals['_HEALTHCHECKREQUEST']._serialized_end=142
  _globals['_HEALTHCHECKRESPONSE']._serialized_start=144
  _globals['_HEALTHCHECKRESPONSE']._serialized_end=181
  _globals['_VIDEOFROMAUDIOGENERATOR']._serialized_start=184
  _globals['_VIDEOFROMAUDIOGENERATOR']._serialized_end=424
# @@protoc_insertion_point(module_scope)
