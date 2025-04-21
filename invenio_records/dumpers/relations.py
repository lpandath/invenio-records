# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2020 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Relations dumper.

Dumper used to dump/load relations to/from a search engine body.
"""
from typing import TYPE_CHECKING, Any, Type

from ..dictutils import dict_lookup, dict_set
from .search import SearchDumperExt

if TYPE_CHECKING:
    from ..api import RecordBase
    from .base import _generic_data


class RelationDumperExt(SearchDumperExt):
    """Dumper for a relations field."""

    def __init__(self, key: str, fields: list[str] | None = None) -> None:
        """Initialize the dumper."""
        self.key = key
        self.fields = fields

    def dump(self, record: RecordBase, data: _generic_data) -> None:
        """Dump relations."""
        relations = getattr(record, self.key)
        relations.dereference(fields=self.fields)
        relation_fields = self.fields or relations
        for rel_field_name in relation_fields:
            rel_field = getattr(relations, rel_field_name)
            try:
                dict_set(data, rel_field.key, dict_lookup(record, rel_field.key))
            except KeyError:
                pass

    def load(self, data: _generic_data, record_cls: Type[RecordBase]) -> None:
        """Load relations."""
        # TODO: figure out what/how to load
        pass
