```python
from __future__ import generator_stop

from jinja2.runtime import (
    LoopContext,
    Macro,
    Markup,
    Namespace,
    TemplateNotFound,
    TemplateReference,
    TemplateRuntimeError,
    Undefined,
    concat,
    escape,
    identity,
    internalcode,
    markup_join,
    missing,
    str_join,
)

name = "home.jinja"


def root(context, missing=missing, environment=environment):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    cond_expr_undefined = Undefined

    if 0:
        yield None

    pass

    yield "This is a template\n\n"

    def macro():
        t_1 = []
        l_1_mytime = resolve("mytime")
        pass

        t_1.extend(
            (
                "\n<div>\n",
                escape(
                    (undefined(name="mytime") if l_1_mytime is missing else l_1_mytime)
                ),
                "\n",
                escape(
                    environment.getattr(
                        (
                            undefined(name="mytime")
                            if l_1_mytime is missing
                            else l_1_mytime
                        ),
                        "somethig",
                    )
                ),
                "\n</div>\n",
            )
        )

        return concat(t_1)

    caller = Macro(
        environment, macro, None, (), False, False, False, context.eval_ctx.autoescape
    )

    yield context.call(
        environment.extensions["misc.extensions.FragmentCacheExtension"]._cache_support,
        "sidebar1",
        5,
        caller=caller,
    )

    yield "\n\n"

    def macro():
        t_2 = []
        l_1_mytime = resolve("mytime")
        pass

        t_2.extend(
            (
                "\n<div>\n",
                escape(
                    (undefined(name="mytime") if l_1_mytime is missing else l_1_mytime)
                ),
                "\n</div>\n",
            )
        )

        return concat(t_2)

    caller = Macro(
        environment, macro, None, (), False, False, False, context.eval_ctx.autoescape
    )

    yield context.call(
        environment.extensions["misc.extensions.FragmentCacheExtension"]._cache_support,
        "sidebar2",
        5,
        caller=caller,
    )

    yield "\n\n"

    if True:
        pass
        yield "11"

    yield "\n\n"

    def macro():
        t_3 = []
        l_1_mytime = resolve("mytime")
        pass

        t_3.extend(
            (
                "\n<p>1</p>\n",
                escape(
                    (undefined(name="mytime") if l_1_mytime is missing else l_1_mytime)
                ),
                "\n<p>2</p>\n",
                escape(
                    (undefined(name="mytime") if l_1_mytime is missing else l_1_mytime)
                ),
                "\n<p>3</p>\n",
            )
        )

        return concat(t_3)

    caller = Macro(
        environment, macro, None, (), False, False, False, context.eval_ctx.autoescape
    )

    yield context.call(
        environment.extensions["misc.extensions.DelayedRenderingTag"]._cache_support,
        "render",
        None,
        caller=caller,
    )

    yield "\n\n\n"

    def macro():
        t_4 = []
        pass
        t_4.append(
            "\n",
        )
        return concat(t_4)

    caller = Macro(
        environment, macro, None, (), False, False, False, context.eval_ctx.autoescape
    )

    yield context.call(
        environment.extensions["misc.extensions.FragmentCacheExtension"]._cache_support,
        "something",
        5,
        caller=caller,
    )

    yield "\n\n"

    template = environment.get_template("outside.jinja", "home.jinja")

    for event in template.root_render_func(
        template.new_context(context.get_all(), True, {})
    ):

        yield event

    yield "\n\n<hr />\n"

    def macro():
        t_5 = []
        l_1_mytime = resolve("mytime")
        pass

        t_5.extend(
            (
                "\n<p>4</p>\n",
                escape(
                    (undefined(name="mytime") if l_1_mytime is missing else l_1_mytime)
                ),
                "\n<p>5</p>\n",
                escape(
                    (undefined(name="mytime") if l_1_mytime is missing else l_1_mytime)
                ),
                "\n<p>6</p>\n",
            )
        )

        return concat(t_5)

    caller = Macro(
        environment, macro, None, (), False, False, False, context.eval_ctx.autoescape
    )

    yield context.call(
        environment.extensions["misc.extensions.DelayedRenderingTag"]._cache_support,
        "render1",
        None,
        caller=caller,
    )

    yield "\n<hr />"


blocks = {}

debug_info = "3=12&5=18&6=20&3=25&10=27&12=33&10=38&16=40&18=44&20=50&22=52&18=57&27=59&30=69&33=73&35=79&37=81&33=86"

# Outside.jinja
from __future__ import generator_stop

from jinja2.runtime import (
    LoopContext,
    Macro,
    Markup,
    Namespace,
    TemplateNotFound,
    TemplateReference,
    TemplateRuntimeError,
    Undefined,
    concat,
    escape,
    identity,
    internalcode,
    markup_join,
    missing,
    str_join,
)

name = "outside.jinja"


def root(context, missing=missing, environment=environment):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    cond_expr_undefined = Undefined

    if 0:
        yield None

    pass

    yield "outnside\n"

    template = environment.get_template("other.jinja", "outside.jinja")

    for event in template.root_render_func(
        template.new_context(context.get_all(), True, {})
    ):

        yield event

    yield "\nstuff"


blocks = {}

debug_info = "2=12"


# Other.jinja
from __future__ import generator_stop

from jinja2.runtime import (
    LoopContext,
    Macro,
    Markup,
    Namespace,
    TemplateNotFound,
    TemplateReference,
    TemplateRuntimeError,
    Undefined,
    concat,
    escape,
    identity,
    internalcode,
    markup_join,
    missing,
    str_join,
)

name = "other.jinja"


def root(context, missing=missing, environment=environment):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    cond_expr_undefined = Undefined

    if 0:
        yield None

    pass

    yield "inside"


blocks = {}

debug_info = ""
```
