import mistune
from mistune.directives import DirectiveToc, DirectiveInclude
from mistune.plugins import (
    plugin_footnotes,
    plugin_strikethrough,
    plugin_table,
    plugin_url,
    plugin_task_lists,
    plugin_def_list,
    plugin_abbr,
)
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

from django import template
from django.db.models import Count, Q
from django.utils.safestring import mark_safe
from ..models import Post

register = template.Library()


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if info:
            lexer = get_lexer_by_name(info, stripall=True)
            formatter = html.HtmlFormatter()
            return highlight(code, lexer, formatter)
        return "<pre><code>" + mistune.escape(code) + "</code></pre>"


@register.filter(name="markdown")
def markdown_format(text):
    markdown = mistune.create_markdown(
        renderer=HighlightRenderer(),
        escape=False,
        plugins=[
            DirectiveToc(),
            DirectiveInclude(),  # toc支持
            plugin_footnotes,  # 注脚
            plugin_strikethrough,  # 删除线
            plugin_table,  # 表格
            plugin_url,  # 链接
            plugin_task_lists,  # 任务列表
            plugin_def_list,  # 自定义列表
            plugin_abbr,  # 缩写
        ],
    )
    content = markdown(text)
    return mark_safe(content)
