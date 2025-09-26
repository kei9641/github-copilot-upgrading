from configparser import ConfigParser
from os.path import isfile

class DictMatch(object):

    def __init__(self, config=None, mapped_options={}, mapped_defaults={}):
        self.config = config
        self.mapped_options = mapped_options
        self.mapped_defaults = mapped_defaults

    def options(self):
        # If all fails we will always have default values
        configuration = self.defaults()

        # dict 타입 입력 처리
        if isinstance(self.config, dict):
            try:
                configuration = self.key_matcher(self.config, return_empty=True)
                if not configuration:
                    configuration = self.defaults(self.config)
                return configuration
            except Exception as error:
                raise OptionConfigurationError(error)

        # dict-like 객체(타입은 dict이 아니지만 키/값 지원)
        # 단, str/bytes/path-like은 제외
        if hasattr(self.config, '__getitem__') and not isinstance(self.config, (str, bytes)):
            try:
                configuration = self.key_matcher(self.config)
                return configuration
            except Exception as error:
                raise OptionConfigurationError(error)

        # 파일 경로(str, bytes, os.PathLike) 또는 None 처리
        import os
        if self.config is None or isinstance(self.config, (str, bytes, os.PathLike)):
            if self.config is None or not isfile(self.config):
                configuration = self.defaults()
                return configuration
            try:
                parser = ConfigParser()
                parser.read(self.config)
                file_options = parser.defaults()
                configuration = self.key_matcher(file_options)
            except Exception as error:
                raise OptionConfigurationError(error)
            return configuration

        # 그 외 타입은 기본값 반환
        configuration = self.defaults()
        return configuration


    def key_matcher(self, original, return_empty=False):
        converted_opts = {}

        for key, value in self.mapped_options.items():
            try:
                file_value = original[key]
                converted_opts[value] = file_value
            except KeyError:
                pass # we will fill any empty values later with config_defaults

        if len(converted_opts) == 0 and return_empty == True:
            return False
        try:
            configuration = self.defaults(converted_opts)
            return configuration
        except Exception as error:
            raise OptionConfigurationError(error)


    def defaults(self, config=None):
        """From the config dictionary it checks missing values and
        adds the defaul ones for them if any"""
        if config == None:
            return self.mapped_defaults

        for key in self.mapped_defaults.keys():
            try:
                config[key]
                if config[key] == '':
                    config[key] = self.mapped_defaults[key]
            except KeyError:
                config[key] = self.mapped_defaults[key]
        return config


class OptionConfigurationError(Exception):
    """Base class for exceptions in this module."""
    pass
