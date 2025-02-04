# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/abstract_tag_pushed.py

This file declares the AbstractTagPushed class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/events

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
from pythoneda.shared import attribute, Event, primary_key_attribute
from pythoneda.shared.nix.flake import NixFlakeInput
from typing import List


class AbstractTagPushed(Event):
    """
    Base class for XTagPushed events.

    Class name: AbstractTagPushed

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        tag: str,
        commit: str,
        repositoryUrl: str,
        branch: str,
        repositoryFolder: str,
        committedChangesTaggedId: str = None,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new AbstractTagPushed instance.
        :param tag: The tag.
        :type tag: str
        :param commit: The hash of the commit.
        :type commit: str
        :param repositoryUrl: The repository url.
        :type repositoryUrl: str
        :param branch: The branch.
        :type branch: str
        :param repositoryFolder: The repository folder.
        :type repositoryFolder: str
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        self._tag = tag
        self._commit = commit
        self._repository_url = repositoryUrl
        self._branch = branch
        self._repository_folder = repositoryFolder
        super().__init__(previousEventIds, reconstructedId)

    @property
    @primary_key_attribute
    def tag(self) -> str:
        """
        Retrieves the tag.
        :return: Such information.
        :rtype: str
        """
        return self._tag

    @property
    @primary_key_attribute
    def commit(self) -> str:
        """
        Retrieves the commit.
        :return: Such information.
        :rtype: str
        """
        return self._commit

    @property
    @primary_key_attribute
    def repository_url(self) -> str:
        """
        Retrieves the repository url.
        :return: Such url.
        :rtype: str
        """
        return self._repository_url

    @property
    @attribute
    def branch(self) -> str:
        """
        Retrieves the branch.
        :return: Such information.
        :rtype: str
        """
        return self._branch

    @property
    @primary_key_attribute
    def repository_folder(self) -> str:
        """
        Retrieves the repository folder.
        :return: Such folder.
        :rtype: str
        """
        return self._repository_folder

    def matches_repository_folder(self, folder: str) -> bool:
        """
        Checks if this event is referring to given repository folder.
        :param folder: The folder to check.
        :type folder: str
        :return: True if the change is related to the repository folder; False otherwise.
        :rtype: bool
        """
        return self.repository_folder == folder

    def matches_input(self, target: NixFlakeInput) -> bool:
        """
        Checks if this event refers to given input.
        :param target: The input.
        :type target: pythoneda.shared.nix.flake.NixFlakeInput
        :return: True if the change is related to given input; False otherwise.
        :rtype: bool
        """
        return self.repository_url == target.url


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
