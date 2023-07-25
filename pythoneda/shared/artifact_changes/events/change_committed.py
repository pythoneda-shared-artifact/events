"""
pythoneda/shared/artifact_changes/events/change_committed.py

This file declares the ChangeCommitted event.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact-changes/events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.event import Event
from pythoneda.shared.artifact_changes.change import Change
from pythoneda.value_object import primary_key_attribute
from typing import List

class ChangeCommitted(Event):
    """
    Represents the moment a new change has been committed.

    Class name: ChangeCommitted

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - pythoneda.shared.artifact_changes.events.CommitChangeRequested: The event this one is response to.
    """

    def __init__(
        self,
        change: Change,
        commitChangeRequestedId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new ChangeCommitted instance.
        :param change: The change information.
        :type change: pythoneda.shared.artifact_changes.change.Change
        :param commitChangeRequestedId: The id of the request event.
        :type commitChangeRequestedId: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event is being recostructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        previous_events = None
        if commitCangeRequestedId:
            previous_events = [commitChangeRequestedId]
        super().__init__(
            previous_events, reconstructedId, reconstructedPreviousEventIds
        )
        self._change = change

    @property
    @primary_key_attribute
    def change(self) -> Change:
        """
        Retrieves the change.
        :return: Such information.
        :rtype: pythoneda.shared.artifact_changes.change.Change
        """
        return self._change
