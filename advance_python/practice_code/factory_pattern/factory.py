"""
This is a factory pattern class
for creating audio and video quality
based on the user input = low, high, master

# plan = approach
1. create a class for video_exporter and
    audio exporter.
2. write sub-class for both video and audio
    and inherit the master exporter to these
3. create factory_export class
4. create different quality exporter class
    and inherit the main factory_export.

"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """video exporter class"""

    @abstractmethod
    def prepare_export(self, video_data):
        """prepares export"""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """doing the export"""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(ABC):
    """video exporter class"""

    @abstractmethod
    def prepare_export(self, audio_data):
        """prepares export"""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """doing the export"""


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")


class ExporterFactory(ABC):

    @abstractmethod
    def get_video_exporter(self):
        """get the video exporter"""

    @abstractmethod
    def get_audio_exporter(self):
        """get the audio exporter"""


class LowQualityFactory(ExporterFactory):

    def get_video_exporter(self):
        return H264BPVideoExporter()

    def get_audio_exporter(self):
        return AACAudioExporter()


class HighQualityFactory(ExporterFactory):

    def get_video_exporter(self):
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self):
        return AACAudioExporter()


class MasterQualityFactory(ExporterFactory):

    def get_video_exporter(self):
        return LosslessVideoExporter()

    def get_audio_exporter(self):
        return WAVAudioExporter()


def get_exporter_factory():
    factories = {"low": LowQualityFactory(), "high": HighQualityFactory(), "master": MasterQualityFactory()}

    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")


def main(fac: ExporterFactory):
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_video_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    factory = get_exporter_factory()
    main(factory)
