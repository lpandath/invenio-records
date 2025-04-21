# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2022 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Indexed timestamp dumper.

Dumper used to dump/load the indexed time of a record to/from a search engine body.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

import arrow

from .search import SearchDumperExt

if TYPE_CHECKING:
    from ..api import RecordBase
    from .base import _generic_data


class IndexedAtDumperExt(SearchDumperExt):
    """Dumper for the indexed_at field."""

    def __init__(self, key: str = "indexed_at") -> None:
        """Initialize the dumper."""
        self.key = key

    def dump(self, record: RecordBase, data: _generic_data) -> None:
        """Dump relations."""
        data[self.key] = arrow.utcnow().isoformat()

    def load(self, data: _generic_data, record_cls: type[RecordBase]) -> None:
        """Load (remove) indexed data."""
        data.pop(self.key, None)
