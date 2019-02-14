# PytgVoIP - Telegram VoIP Library for Python
# Copyright (C) 2019 bakatrouble <https://github.com/bakatrouble>
#
# This file is part of PytgVoIP.
#
# PytgVoIP is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PytgVoIP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with PytgVoIP.  If not, see <http://www.gnu.org/licenses/>.


from tgvoip.tgvoip import *
from tgvoip.tgvoip import __all__ as tgvoip_all
from tgvoip.service import VoIPService
from tgvoip.incoming_call import VoIPIncomingCall
from tgvoip.outgoing_call import VoIPOutgoingCall
from tgvoip.file_stream_call import VoIPFileStreamCallMixin, VoIPIncomingFileStreamCall, VoIPOutgoingFileStreamCall, \
    VoIPFileStreamService


__all__ = ['VoIPService', 'VoIPIncomingCall', 'VoIPOutgoingCall', 'VoIPFileStreamCallMixin',
           'VoIPIncomingFileStreamCall', 'VoIPOutgoingFileStreamCall', 'VoIPFileStreamService']
__all__ += tgvoip_all

__version__ = '0.0.1'
