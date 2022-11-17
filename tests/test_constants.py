import pytest
from constants import PredefinedVocabularity
class TestConstants():
    def test_instance_creation(self):
        insta = PredefinedVocabularity({}, {}, {})
        assert isinstance(insta, PredefinedVocabularity)

    def test_instance_creation_with_no_args(self):
        with pytest.raises(Exception):
            insta = PredefinedVocabularity()
        
    def test_base_filled_dct(self):
        # TODO: move fixtures to conftest
        name = {'name': 'name'}
        action = {'action': 'action'}
        command = {'command': {'command': 'command'}}
        
        true_dct = {'name': 'name', 'action': 'action', 'command': {'command': 'command'}}
        insta = PredefinedVocabularity(name, action, command)

        assert insta.base_dct_filled == true_dct