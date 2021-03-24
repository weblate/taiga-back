# -*- coding: utf-8 -*-
# Copyright (C) 2014-present Taiga Agile LLC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from typing import Any, Optional, Union

from django.db.models import Q

from .models import User


def get_user_by_username_or_email(username_or_email: str, extra_filters: dict[str, Any] = {}) ->  Optional[User]:
    qs = User.objects.filter(Q(username__iexact=username_or_email) |
                             Q(email__iexact=username_or_email),
                             **extra_filters)

    if len(qs) > 1:
        # NOTE: This is because Taiga was case sensitive for email and
        #       username in the pass
        qs = qs.filter(Q(username=username_or_email) |
                       Q(email=username_or_email))

    if len(qs) == 0:
        return None

    return  qs[0]
