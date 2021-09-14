import operator
import uuid
from io import StringIO

from django.core.cache import cache
from jinja2 import nodes
from jinja2.ext import Extension
from jinja2.utils import contextfunction

TEMPLATE_DELIMITER = "TEST_TEMPLATE_DELIMITER"


class FragmentCacheExtension(Extension):
    tags = {"cache"}

    def __init__(self, environment):
        super().__init__(environment)

        environment.extend(fragment_cache_prefix="", fragment_cache=None)
        environment.fragment_cache = cache

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = [parser.parse_expression()]

        if parser.stream.skip_if("comma"):
            args.append(parser.parse_expression())
        else:
            args.append(nodes.Const(None))

        body = parser.parse_statements(["name:endcache"], drop_needle=True)

        return nodes.CallBlock(
            self.call_method("_cache_support", args), [], [], body
        ).set_lineno(lineno)

    def _cache_support(self, name, timeout, caller):
        """Helper callback."""
        cache_key = self.environment.fragment_cache_prefix + name
        value = self.environment.fragment_cache.get(cache_key)

        if value is None:
            value = caller()
            self.environment.fragment_cache.set(cache_key, value, timeout)

        return value


class RawOutputTag(Extension):
    TAG_NAME = "rawoutput"
    CLOSING_TAG_NAME = f"end{TAG_NAME}"

    tags = {TAG_NAME}

    def wrap_content(self, content):
        return f"<{TEMPLATE_DELIMITER}>{content}</{TEMPLATE_DELIMITER}"

    def parse(self, parser):
        print("Parsing")
        inner_tokens = list()

        found_last_token = False
        last_line_number = None
        collect_tokens = False

        for token in parser.stream:
            last_line_number = token.lineno

            if not collect_tokens and token.type == "block_end":
                collect_tokens = True
                continue

            if token.type == "name" and token.value == self.CLOSING_TAG_NAME:
                found_last_token = True
                del inner_tokens[-1]
                break

            if collect_tokens:
                inner_tokens.append(token)

        if not found_last_token:
            parser._fail_ut_eof(
                name=None,
                end_token_stack=[[f"name:{self.CLOSING_TAG_NAME}"]],
                lineno=last_line_number,
            )

        wrapped_content = self.wrap_content(
            "".join(token.value for token in inner_tokens)
        )

        output = nodes.Output()
        output.nodes = [nodes.TemplateData(wrapped_content)]

        return output


class DelayedRenderingTag(Extension):
    TAG_NAME = "staged_render"
    CLOSING_TAG_NAME = f"end{TAG_NAME}"

    tags = {TAG_NAME}

    def __init__(self, environment):
        super().__init__(environment)

        self._tag_data = dict()

    def save_content(self, content):
        pass

    def wrap_content(self, content_id, content):
        return (
            f"<{TEMPLATE_DELIMITER}:{content_id}>"
            f"{content}"
            f"</{TEMPLATE_DELIMITER}:{content_id}>"
        )

    def _old_parse(self, parser):
        print("Parsing")
        inner_tokens = list()

        found_last_token = False
        last_line_number = None
        collect_tokens = False

        for token in parser.stream:
            last_line_number = token.lineno

            if not collect_tokens and token.type == "block_end":
                collect_tokens = True
                continue

            if token.type == "name" and token.value == self.CLOSING_TAG_NAME:
                found_last_token = True
                del inner_tokens[-1]
                break

            if collect_tokens:
                inner_tokens.append(token)

        if not found_last_token:
            parser._fail_ut_eof(
                name=None,
                end_token_stack=[[f"name:{self.CLOSING_TAG_NAME}"]],
                lineno=last_line_number,
            )

        content_id = uuid.uuid4()
        wrapped_content = self.wrap_content(
            content_id, "".join(token.value for token in inner_tokens)
        )

        output = nodes.Output()
        output.nodes = [nodes.TemplateData(wrapped_content)]

        return output

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = [parser.parse_expression()]

        if parser.stream.skip_if("comma"):
            args.append(parser.parse_expression())
        else:
            args.append(nodes.Const(None))

        body = parser.parse_statements(
            [f"name:{self.CLOSING_TAG_NAME}"], drop_needle=True
        )

        return nodes.CallBlock(
            self.call_method("_cache_support", args), [], [], body
        ).set_lineno(lineno)

    def _cache_support(self, name, timeout, caller):
        """Helper callback."""
        timeout = 1
        key = self.environment.fragment_cache_prefix + name

        # try to load the block from the cache
        # if there is no fragment in the cache, render it and store
        # it in the cache.
        rv = self.environment.fragment_cache.get(key)
        if rv is not None:
            return rv
        rv = caller()
        self.environment.fragment_cache.set(key, rv, timeout)
        return rv
